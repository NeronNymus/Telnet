#!/usr/bin/env python3

import re
import datetime
from args.backend import start_pool
from multiprocessing import Value, Lock
from psycopg2.extras import execute_batch

from args.backend import start_pool
from args.connection import get_private_ip



# Function for processing the resultant masscan result
def process_masscan_result(file_name, connection_pool, source_ip):

    # Match the results
    pattern = re.compile(
        r"Timestamp:\s*(\d+)\s+Host:\s*([\d.]+)\s*\(\)\s*Ports:\s*(\d+)/(\w+)/(\w+)//(\w+)//"
    )


    with open(file_name, 'r') as file:
        cont = 1

        for line in file:
            match = pattern.search(line)
            if match:
                #print(f"FLAG: {match[0]}")
                timestamp, host, port, state, protocol, service = match.groups()

                # Format correctly
                dt_object = datetime.datetime.fromtimestamp(int(timestamp))
                timestamp = dt_object.strftime("%Y-%m-%d %H:%M:%S")
                port = int(port)

                # Get a connection from the pool
                connection = connection_pool.getconn()

                # Check if the record already exists
                select_query = """
                    SELECT COUNT(*) FROM masscan_results 
                    WHERE timestamp = %s AND host = %s
                """
                cursor = connection.cursor()
                cursor.execute(select_query, (timestamp, host))
                existing_records = cursor.fetchone()[0]

                if existing_records == 0:
                    # Insert the data into the PostgreSQL table
                    insert_query = """
                        INSERT INTO masscan_results (timestamp, host, port, state, protocol, service, source_ip)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(insert_query, (timestamp, host, port, state, protocol, service, source_ip))
                    connection.commit()
                    #print(f"Inserted: {timestamp}, {host}, {port}, {state}, {protocol}, {service}, {source_ip}")
                    print(f"[{cont}] Inserted.")
                else:
                    #print(f"Skipped duplicate: {timestamp}, {host}")
                    print(f"[{cont}] Skipped duplicate.")

                cursor.close()

                # Return the connection to the pool
                connection_pool.putconn(connection)

                #Print the extracted data
                #print(f"{timestamp}, {host}, {port}, {state}, {protocol}, {service}")
            else:
                # Print the line if the pattern does not match to debug
                print(f"Pattern not matched for line: {line}\n")

            cont += 1



# Function for processing each line of the masscan result
def process_masscan_result_line(cont, lock, batch, line, connection_pool, source_ip):
    
    # Added batch size for batching inserts
    batch_size = 1000  # Adjust batch size as needed

    # Match the results
    pattern = re.compile(
        r"Timestamp:\s*(\d+)\s+Host:\s*([\d.]+)\s*\(\)\s*Ports:\s*(\d+)/(\w+)/(\w+)//(\w+)//"
    )

    match = pattern.search(line)
    if match:
        timestamp, host, port, state, protocol, service = match.groups()

        # Format correctly
        dt_object = datetime.datetime.fromtimestamp(int(timestamp))
        timestamp = dt_object.strftime("%Y-%m-%d %H:%M:%S")
        port = int(port)

        # Get a connection from the pool
        connection = connection_pool.getconn()

        # Check if the record already exists
        select_query = """
            SELECT COUNT(*) FROM masscan_results 
            WHERE timestamp = %s AND host = %s
        """
        cursor = connection.cursor()
        cursor.execute(select_query, (timestamp, host))
        existing_records = cursor.fetchone()[0]


        if existing_records == 0:
            # Update the counter
            with lock:
                current_cont = cont.value
                cont.value += 1
                batch.append((timestamp, host, port, state, protocol, service, source_ip))

            if len(batch) >= batch_size:
                insert_batch(batch, connection_pool, batch_size)
                batch.clear()

            print(f"[{current_cont}] Inserted.")
        else:
            #print(f"Skipped duplicate: {timestamp}, {host}")
            print(f"[{current_cont}] Skipped duplicate.")

        cursor.close()

        # Return the connection to the pool
        connection_pool.putconn(connection)

    else:
        # Print the line if the pattern does not match to debug
        print(f"Pattern not matched for line: {line}\n")


def insert_batch(batch, connection_pool, batch_size):
    # Divide the batch into smaller chunks based on batch_size
    chunks = [batch[i:i + batch_size] for i in range(0, len(batch), batch_size)]

    insert_query = """
        INSERT INTO masscan_results (timestamp, host, port, state, protocol, service, source_ip)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (timestamp, host) DO NOTHING
    """

    connection = connection_pool.getconn()
    cursor = connection.cursor()

    # Insert each chunk separately
    for chunk in chunks:
        execute_batch(cursor, insert_query, chunk)  # Used execute_batch for batch insert

    connection.commit()
    cursor.close()
    connection_pool.putconn(connection)

