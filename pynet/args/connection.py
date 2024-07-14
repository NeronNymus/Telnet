#!/usr/bin/env python3

import sys
import telnetlib
import psycopg2
import socket
from psycopg2 import pool
from datetime import datetime

# Personal packages
from utils.colors import Colors

conn_timeout = 15

def connect_to_ip(conn, source_ip, ip_address, username, password, port):
    print(Colors.BOLD_WHITE + f"\n[!] Trying to connect with the next details: \n"
          f"Port:\t{port} \n"
          f"IP:\t{ip_address} \n" + 
          f"-------------------------------------------------------------------------" + Colors.R)

    # Record the start time before attempting the connection
    start_time = datetime.now()

    cur = None

    try:
        tn = telnetlib.Telnet(ip_address, timeout=conn_timeout)  # Increased timeout
        output = tn.read_until(b"Username: ", timeout=conn_timeout)  # Increased timeout
        print("Received:", output.decode('ascii'))
        tn.write(username.encode('ascii') + b"\n")
        output = tn.read_until(b"Password: ", timeout=conn_timeout)  # Increased timeout
        print("Received:", output.decode('ascii'))
        tn.write(password.encode('ascii') + b"\n")

        print(Colors.GREEN + "[!] Successfully connected." + Colors.R)

        # Calculate the elapsed time
        elapsed_time = datetime.now() - start_time
        print(Colors.ORANGE + f"[!] Elapsed time: {elapsed_time}" + Colors.R)

        insert_connection_status(conn, source_ip, ip_address, elapsed_time, 'Success')

        return tn  # Return the telnet object for further use

    except Exception as e:
        print(Colors.RED + f"[#] Connection error: \n{e}" + Colors.R)

        # Calculate the elapsed time even in case of connection error
        elapsed_time = datetime.now() - start_time
        print(f"[!] Elapsed time: {elapsed_time}")

        #insert_connection_status(conn, source_ip, ip_address, elapsed_time, 'Timeout')
        insert_connection_status(conn, source_ip, ip_address, elapsed_time, str(e))

        return None


# Receives a boolean status and updates the backend
def insert_connection_status(conn, source_ip, ip_address, elapsed_time, status):
    cur = None
    try:
        cur = conn.cursor()

        # Calculate elapsed time in seconds (total_seconds())
        elapsed_seconds = elapsed_time.total_seconds()

        # Convert elapsed_seconds to INTERVAL type with seconds precision
        elapsed_interval = f"{int(elapsed_seconds)} seconds"

        # Define the SQL statement to insert the connection status, source_ip, elapsed time in seconds, and timestamp
        sql = "INSERT INTO connection_history (source_ip, ip_address, connection_status, elapsed_time, timestamp) VALUES (%s, %s, %s, %s::INTERVAL, %s)"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Execute the SQL statement with the parameters
        cur.execute(sql, (source_ip, ip_address, status, elapsed_interval, timestamp))

        conn.commit()  # Commit the transaction

        print(Colors.GREEN + f"[!] Connection status inserted for IP address {ip_address}" 
                + "\n-------------------------------------------------------------------------\n"
                + Colors.R)

    except psycopg2.Error as e:
        print(Colors.RED + f"Error inserting connection status: {e}" + Colors.R)

    finally:
        if cur:
            cur.close()

def get_private_ip():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to a public DNS server
        s.connect(('8.8.8.8', 80))
        # Get the local IP address assigned by the OS
        private_ip = s.getsockname()[0]
    except Exception as e:
        print(Colors.RED + f"Error getting private IP: {e}" + Colors.R)
        private_ip = None
    finally:
        # Close the socket
        s.close()
    return private_ip



def send_command(tn, command):
    try:
        tn.write(command.encode('ascii') + b"\n")
        output = tn.read_until(b"Telnet", timeout=5)
        return output.decode('ascii')
    except Exception as e:
        print(Colors.RED + f"Error sending command: {e}" + Colors.R)
        return None
