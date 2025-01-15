#!/usr/bin/env python3

import os
import re
import sys
import psycopg2
from psycopg2 import pool
from natsort import natsorted
from subprocess import run, PIPE
from datetime import datetime, timedelta

# Personal packages
from utils.colors import Colors

# Pass environment variables
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


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
def conn_simple():
    params = get_db_params()
    try:
        conn = psycopg2.connect(**params)
        print(Colors.GREEN + "[*] Connection successful to database." + Colors.R)
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
        INSERT INTO wap_devices_live (parent_ipv4_address, child_ipv4_address, mac_vendor, mac_address, timestamp)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Insert each device
        for device in devices:
            values = (device['parent_ipv4_address'], device['ip'], device['mac_vendor'], device['mac'], device['timestamp'])
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

# Regular expression patterns for IP and MAC validation
def is_valid_ip(ip):
    """Check if a given string is a valid IPv4 address."""
    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    return re.match(ip_pattern, ip) is not None

def is_valid_mac(mac):
    """Check if a given string is a valid MAC address."""
    mac_pattern = r"([0-9a-fA-F]{2}[:.-]){5}[0-9a-fA-F]{2}"
    return re.match(mac_pattern, mac) is not None

# Function to process the received data and extract devices
def telnet_process_ips(received_data, remote_ip):
    # Decode bytes to string for easier manipulation
    data = received_data.decode("utf-8")

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
                    "ip": ip,
                    "mac_vendor": mac_vendor,
                    "mac": mac,
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

        return devices
    else:
        print("No WAP> prompt found")
        return []
