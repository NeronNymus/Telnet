#!/usr/bin/env python3

import os
import sys
import psycopg2

# Personal packages
from args.connection import connect_to_ip, send_command
from utils.colors import Colors


# Database connection parameters using environment variables
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')

# Initialize the connection pool
def start_pool(min_connections, max_connections):
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


def connect_to_database():
    try:
        print("DB_HOST: " + str(DB_HOST))
        print("DB_PORT: " + str(DB_PORT))
        #conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)

        conn = connection_pool.getconn()
        
        if conn:
            print(Colors.ORANGE + "[!] Connected to the database." + Colors.R)
            return conn
        else:
            print(Colors.RED + "[#] No available connections in the pool." + Colors.R)
            return None
    except psycopg2.Error as e:
        print(Colors.RED + f"[#] Error connecting to PostgreSQL:\n{e}" + Colors.R)
        return None


def exec_ifconfig(conn, ip, tn, command):

    if command == 'ifconfig':
        if tn:
            output = send_command(tn, command)
            if output:
                print(output)
                if conn:
                    save_ifconfig(conn, ip, output)
            else:
                print(Colors.RED + "[#] Failed to execute command.\n" + Colors.R)
            tn.close()
        else:
            print(Colors.RED + "\n[#] Failed to connect.\n" + Colors.R)


def check_existing_record(conn, ip, command):
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT * FROM ifconfig_results
            WHERE ip_address = %s
        """, (ip,))

        existing_record = cursor.fetchone()

        return existing_record is not None
    except psycopg2.Error as e:
        print("Error:", e)
        return False



# Function to save ifconfig data to the database
def save_ifconfig(conn, ip, data):
    try:
        cursor = conn.cursor()
        # Create table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ifconfig_results (
                id SERIAL PRIMARY KEY,
                ip_address TEXT,
                output TEXT UNIQUE
            )
        """)
        # Insert data into the table if it's not a duplicate
        cursor.execute("""
            INSERT INTO ifconfig_results (ip_address, output)
            SELECT %s, %s WHERE NOT EXISTS (
                SELECT 1 FROM ifconfig_results WHERE output = %s
            )
        """, (ip, data, data))
        conn.commit()

        if cursor.rowcount > 0:
            print(Colors.GREEN + "[!] Data saved to the database." + Colors.R) 
        else:
            print(Colors.GREEN + "[!] Data already exists in the database. Skipped insertion." + Colors.R)
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if cursor:
            cursor.close()
