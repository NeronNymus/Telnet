#!/usr/bin/env python3

# The purpose of this script is to save important responses data into the backend.

import os
import re
import sys
import csv
import psycopg2
from psycopg2 import sql
from psycopg2 import pool
from natsort import natsorted
from subprocess import run, PIPE
from datetime import datetime, timedelta
from psycopg2.extras import execute_values

# Personal packages
from utils.colors import Colors

# Pass environment variables
from dotenv import load_dotenv


# Load environment variables from .env file
#load_dotenv(".env2")

# Database connection parameters using environment variables
DB_HOST     = os.getenv('DB_HOST')
DB_NAME     = os.getenv('DB_NAME')
DB_USER     = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT     = os.getenv('DB_PORT')

# Database connection parameters
def get_db_params():
    return {
        "dbname": os.getenv('DB_NAME'),
        "user": os.getenv('DB_USER'),
        "password": os.getenv('DB_PASSWORD'),
        "host": os.getenv('DB_HOST'),
        "port": os.getenv('DB_PORT')
    }

# Initialize the connection pool
def start_pool(min_connections, max_connections):
    global DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

    connection_pool = psycopg2.pool.SimpleConnectionPool(
        min_connections,  # minimum number of connections
        max_connections,  # maximum number of connections
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )
    return connection_pool


def connect_to_database(connection_pool):
    try:
        conn = connection_pool.getconn()
        
        if conn:
            print(Colors.ORANGE + "[!] Connected to the database.\n" + Colors.R)
            return conn
        else:
            print(Colors.RED + "[#] No available connections in the pool." + Colors.R)
            return None
    except psycopg2.Error as e:
        print(Colors.RED + f"[#] Error connecting to PostgreSQL:\n{e}" + Colors.R)
        return None


# Connect to the database
def conn_simple(env_var=".env"):
    # Clear existing environment variables related to the database
    for key in list(os.environ.keys()):
        if key.startswith("DB_"):  # Only remove database-related variables
            del os.environ[key]
    
    # Load environment variables from the specified .env file
    load_dotenv(env_var)

    # Database connection parameters using environment variables
    DB_HOST     = os.getenv('DB_HOST')
    DB_NAME     = os.getenv('DB_NAME')
    DB_USER     = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_PORT     = os.getenv('DB_PORT')

    # Define parameters for the connection
    params = {
        "host": DB_HOST,
        "dbname": DB_NAME,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "port": DB_PORT,
    }
    
    try:
        conn = psycopg2.connect(**params)
        #print(Colors.GREEN + "[*] Connection successful to database." + Colors.R)
        return conn
    except Exception as e:
        print(Colors.RED + f"Unable to connect to the database: {e}" + Colors.R)
        return None


# Function to query the database
def query(conn, sql_query):
    if not conn:
        return

    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows
    except psycopg2.Error as e:
        print(f"[x] Error querying the database.\n{e}")
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()


# Function to insert devices list into the database
def insert_devices(devices, conn):
    if not conn:
        print("No database connection.")
        return

    cursor = None
    try:
        cursor = conn.cursor()

        # SQL query to insert data into the wap_devices table
        insert_query = """
        INSERT INTO wap_devices_live (parent_ipv4_address, child_id, child_ipv4_address, mac_vendor, mac_address, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        # Insert each device
        for device in devices:
            values = (device['parent_ipv4_address'], device['child_id'], device['ip'], device['mac_vendor'], device['mac'], device['timestamp'])
            cursor.execute(insert_query, values)

        # Commit the transaction after all insertions
        conn.commit()

        # Print the success message
        print(Colors.GREEN + f"{len(devices)} devices inserted successfully." + Colors.R)

        # Confirm insertion by checking the table (optional)
        query_check = "SELECT COUNT(*) FROM wap_devices WHERE parent_ipv4_address = %s"
        cursor.execute(query_check, (devices[0]['parent_ipv4_address'],))  # Use the parent_ip for query
        result = cursor.fetchone()
        if result[0] == len(devices):
            print(f"Confirmed: All {len(devices)} devices have been inserted successfully.")
        else:
            print("[x] Warning: The number of inserted devices does not match the expected count.")

    except psycopg2.Error as e:
        print(f"[x] Error inserting data into the database.\n{e}")
        conn.rollback()  # Rollback the transaction in case of error

    finally:
        if cursor:
            cursor.close()




# Take a list of login data and log it and import into a database
def login_log(login_data, log_number=10, insert_db=True):

    log_file = f"new_logins/new_logins{log_number}.csv"
    
    # Log the data to the CSV file
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(login_data)

    # Insert the data into the database
    if insert_db:
        conn = conn_simple()
        if conn:
            try:
                with conn.cursor() as cur:
                    insert_query = sql.SQL("""
                        INSERT INTO login_registry (ipv4_address, response_time, timestamp, success)
                        VALUES (%s, %s, %s, %s)
                    """)
                    cur.execute(insert_query, login_data)
                    conn.commit()
                    print(f"{Colors.GREEN}[+] Login data inserted into database:{Colors.R}\n{login_data}")
            except Exception as e:
                print(f"{Colors.RED}[-] Failed to insert data into database:{Colors.R} {e}")
                conn.rollback()
            finally:
                #print(f"{Colors.GREEN}[!] Closing connection to the database.{Colors.R}")
                conn.close()
        else:
            print(f"{Colors.RED}[-] Could not connect to the database.{Colors.R}")


def import_login_logs(log_file='new_logins.csv', chunk_size=500):
    registries = []
    conn = None
    invalid_records = []

    def is_valid_timestamp(ts):
        try:
            # Check if the timestamp is valid
            datetime.strptime(ts, "%Y-%m-%d %H:%M:%S.%f")
            return True
        except ValueError:
            return False

    try:
        # Establish a database connection
        conn = conn_simple()
        conn.autocommit = False  # Use transactions for chunked inserts
        cursor = conn.cursor()
        print("Database connection established successfully.")
        
        # Read the log file and prepare registries
        with open(log_file, 'r') as file:
            cont = 1
            for login in file:
                login = login.rstrip()
                registry = login.split(',')

                # Validate record length
                if len(registry) != 4:
                    print(f"[!] Skipping record with invalid length ({len(registry)}): {login}")
                    invalid_records.append(login)
                    continue

                ipv4_address, port, response_time, timestamp = registry

                # Validate timestamp
                if not is_valid_timestamp(timestamp):
                    print(f"[!] Skipping record with invalid timestamp: {login}")
                    invalid_records.append(login)
                    continue
                
                registries.append((ipv4_address, response_time, timestamp, True))
                
                # Insert in chunks
                if len(registries) >= chunk_size:
                    query = """
                    INSERT INTO login_registry (ipv4_address, response_time, timestamp, success)
                    VALUES %s
                    ON CONFLICT (ipv4_address, timestamp) DO NOTHING;
                    """
                    execute_values(cursor, query, registries)
                    print(f"[!][{cont * chunk_size}]")
                    cont += 1
                    conn.commit()  # Commit after each chunk
                    registries = []  # Reset the list after inserting a chunk
            
            # Insert any remaining registries
            if registries:
                print(f"Inserting {len(registries)} remaining records into the database...")
                query = """
                INSERT INTO login_registry (ipv4_address, response_time, timestamp, success)
                VALUES %s
                ON CONFLICT (ipv4_address, timestamp) DO NOTHING;
                """
                execute_values(cursor, query, registries)
                print(f"Inserted {len(registries)} remaining records successfully.")
                conn.commit()
        
        print("All records have been committed successfully.")

    except Exception as e:
        if conn:
            conn.rollback()  # Rollback in case of an error
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")

        # Log invalid records
        if invalid_records:
            print(f"[!] Skipped {len(invalid_records)} invalid records.")
            with open('invalid_records.log', 'w') as log_file:
                log_file.write("\n".join(invalid_records))
            print("[!] Invalid records have been logged to 'invalid_records.log'.")


# Regular expression patterns for IP and MAC validation
def is_valid_ip(ip):
    """Check if a given string is a valid IPv4 or IPv6 address."""
    # IPv4 pattern
    ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    # IPv6 pattern
    ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    
    return re.match(ipv4_pattern, ip) is not None or re.match(ipv6_pattern, ip) is not None

def is_valid_mac(mac):
    """Check if a given string is a valid MAC address."""
    mac_pattern = r"([0-9a-fA-F]{2}[:.-]){5}[0-9a-fA-F]{2}"
    return re.match(mac_pattern, mac) is not None

# Another implementation for extracting the connected devices to a network in Live
def extract_ips(received_data, remote_ip):
    """
    Extracts IP addresses from the 'ip neigh' command output.
    
    :param received_data: The raw bytes received from the WAP device.
    :param remote_ip: The parent IPv4 address.
    :return: A list of extracted IP addresses (both IPv4 and IPv6) that are reachable.
    """
    data = received_data.decode("utf-8")
    
    # Updated regex pattern to capture both IPv4 and IPv6, and check for 'reachable' status
    pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+|\S+:[0-9a-fA-F]+) dev \S+ lladdr (\S+).*nud (reachable).*")
    
    # Find all matches in the received data
    matches = pattern.findall(data)

    if not matches:
        print("[!] No reachable IP/MAC addresses found in the received data.")
        return []
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Format extracted IPs into a structured list
    devices = [{
        "parent_ipv4_address": remote_ip,
        "child_id": 0,
        "ip": ip,
        "mac_vendor": "",
        "mac": mac.upper(),
        "timestamp": timestamp
    } for ip, mac, reachable in matches]

    # Print extracted IPs for debugging
    for device in devices:
        print(f"{device}")
    print()
    
    # Insert devices into the database
    conn = conn_simple()
    insert_devices(devices, conn)
    
    return devices

# Function to process the received data and extract devices
def process_ips(received_data, remote_ip):
    # Decode bytes to string for easier manipulation
    data = received_data.decode("utf-8")

    #print(f"\n[!] Received data\t{data}")

    # Look for the first occurrence of "WAP>" prompt and split data accordingly
    prompt_index = data.find("WAP>")

    if prompt_index != -1:
        # Extract the portion before the first WAP> prompt (i.e., device data)
        data_before_prompt = data[:prompt_index]

        # Split data into individual lines
        lines = data_before_prompt.strip().split('\r\n')

        # List to store the devices
        devices = []

        # Get current timestamp with precision to year, month, day, hour, minute
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Iterate over each line to process the device data
        for line in lines:
            # Regular expression pattern to capture the fields for each device
            pattern = r"(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)"

            # Find match for the current line
            match = re.match(pattern, line)
            if match:
                # Extract fields from the match
                index, user, ip, mac_vendor, mac, expire_time = match.groups()

                # Check if the 'ip' field is a valid IP, if not, it's likely a MAC address
                if not is_valid_ip(ip) and is_valid_mac(ip):
                    ip, mac = mac, ip  # Swap IP and MAC if IP is invalid

                # Check if MAC is valid
                if not is_valid_mac(mac):
                    mac = "Invalid MAC"  # Or handle it as needed

                # Create device dictionary
                device = {
                    "parent_ipv4_address": remote_ip,
                    "child_id": int(index),
                    "ip": ip,
                    "mac_vendor": mac_vendor,
                    "mac": mac.upper(),
                    "timestamp": timestamp
                }

                # Add to devices list
                devices.append(device)

        # Insert devices into the database
        conn = conn_simple()
        insert_devices(devices, conn)

        # Print the devices for debugging
        for device in devices:
            print(device)
        print()

        return devices
    else:
        print("No WAP> prompt found")
        return []


def process_ssid(received_data, remote_ip):

    # Extract SSID data using regex
    ssid_pattern = re.compile(
        r"SSID Index\s*:\s*(\d+).*?"
        r"SSID\s*:\s*(.+?)\r\n"
        r"BSSID\s*:\s*([\w:]+).*?"
        r"Status\s*:\s*(\w+)",
        re.DOTALL
    )
    
    ssid_entries = []
    for match in ssid_pattern.finditer(received_data.decode('utf-8')):
        ssid_index = int(match.group(1))
        ssid_name = match.group(2).strip()
        bssid = match.group(3).strip()
        status = match.group(4).strip()
        connection_status = status.lower() == "up"
        ssid_entries.append((ssid_index, remote_ip, ssid_name, bssid, connection_status))

    # Insert unique entries into the database
    conn = conn_simple()
    cursor = conn.cursor()
    for entry in ssid_entries:
        try:
            cursor.execute(
                """
                INSERT INTO wifi_ssid_info (ssid_index, parent_ipv4_address, ssid_name, bssid, connection_status, timestamp)
                VALUES (%s, %s, %s, %s, %s, NOW())
                ON CONFLICT (ssid_name, bssid) DO NOTHING;
                """,
                entry
            )
        except psycopg2.Error as e:
            print(f"Database error: {e}")
    
    conn.commit()
    print(Colors.GREEN + "[!] SSID data successfully inserted into the database." + Colors.R)
    cursor.close()
    if conn:
        conn.close()


def process_public_ips(received_data, remote_ip):
    print(f"Data received by the backend\n{received_data}")


# Register the updated telnet password
def update_telnet_pass(response, remote_ip, log_number):

    log_file = f"changed_telnet_pass{log_number}.csv"

    password = 'EGflFhmzQUnTc8gJlku/'  # fixed password in your query
    timestamp = datetime.date.today()
    already_changed = True

    # 1. Log the data to the CSV file first
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([remote_ip, password, already_changed, timestamp])

    # Perform the equivalent into database
    conn = conn_simple()
    cursor = conn.cursor()

    try:
        # Attempt to update the existing row
        update_query = """
        UPDATE telnet_pass
        SET already_changed = true
        WHERE ipv4_address = %s;
        """
        cursor.execute(update_query, (remote_ip,))

        # If no rows were updated, perform insert
        if cursor.rowcount == 0:
            insert_query = """
            INSERT INTO telnet_pass (ipv4_address, password, already_changed, timestamp)
            VALUES (%s, 'EGflFhmzQUnTc8gJlku/', true, CURRENT_DATE);
            """
            cursor.execute(insert_query, (remote_ip,))

        conn.commit()
        print(f"{Colors.BOLD_WHITE}[!] Telnet password changed for {Colors.GREEN}{remote_ip}{Colors.R}")

    except Exception as e:
        print(f"{Colors.RED}[-] Error updating or inserting for {remote_ip}: {e}{Colors.R}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    import_login_logs()
