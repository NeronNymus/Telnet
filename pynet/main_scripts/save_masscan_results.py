#!/usr/bin/env python3

# This code serves for importing the masscan results into the PosgreSQL database.
# [!] Parent directory must be pynet.
# Example execution of this script:
# python3 main_scripts/save_masscan_results.py -iL /home/grimaldi/Bash/Telnet/scans/crawling/ips_up_port_23_10.0.0.0_8/ips_up_port_23_10.0.0.0_8.2 -t 20

import re
import os
import sys
import time
import argparse
import concurrent.futures
from natsort import natsorted
from multiprocessing import Value, Lock



# Add parent directory to Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
parent_dir2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

# Personal packages
from utils.colors import Colors
from args.connection import get_private_ip
from args.backend import start_pool, connect_to_database
from etl.etl_masscan import process_masscan_result, process_masscan_result_line

# Start a pool for connections to the backend
threads = 10 # default value

# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Script for loading the masscan results into the database.")
    parser.add_argument("-iL", "--ip_list", help="\t\tPath to a file containing the masscan results to import.")
    parser.add_argument("-t", "--threads", type=int, help="\t\tNumber of threads for concurrent connection to the database.")
    return parser.parse_args()



# Main function
def process_bulk_files():

    # Path to the directory containing 
    scans_dir = os.path.abspath(parent_dir2 + "/scans/crawling/ips_up_port_23_10.0.0.0_8")
    scans_dir = "/home/grimaldi/Bash/Telnet/scans/crawling/ips_up_port_23_10.0.0.0_8"

    files_list = list()


    # Add the files to a list excluding a certain regular pattern
    exclude_pattern = re.compile(r'join|clean|paused.conf')
    for file_name in os.listdir(scans_dir):
        if not exclude_pattern.search(file_name):
            file_path = os.path.join(scans_dir, file_name)
            if os.path.isfile(file_path):
                files_list.append(file_path)
                #print(file_path)


    # Sort and print
    #files_list = natsorted(files_list)

    # Use ThreadPoolExecutor to process files in parallel
    #with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    #    executor.map(process_file, files_list)

    # Close all the connections of the pool
    connection_pool.closeall()

    
def load_file(file_name, threads, source_ip):

    connection_pool = start_pool(threads, threads)

    start_time = time.time() # Start measuring the time

    # Process each file
    process_masscan_result(file_name, connection_pool, source_ip)

    end_time = time.time() # End measuring the time
    print(f"\nParallel processing time: {end_time - start_time} seconds")

    # Close all the connections of the pool
    connection_pool.closeall()

# Alternative loading file
def load_file_parallel(file_name, threads, source_ip):
    connection_pool = start_pool(threads, threads+1)
    batch_size = 1000
    batch = list()

    cont = Value('i', 1)
    lock = Lock()

    start_time = time.time()  # Start measuring the time

    with open(file_name, 'r') as file:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(process_masscan_result_line, cont, lock, batch, line, connection_pool, source_ip, batch_size) for line in file]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # wait for all threads to complete

    end_time = time.time()  # End measuring the time
    print(f"\nParallel processing time: {end_time - start_time} seconds")

    # Insert any remaining entries in the batch
    if batch:
        insert_batch(batch, connection_pool, batch_size)

    # Close all the connections of the pool
    connection_pool.closeall()



if __name__ == "__main__":
    # Receive the arguments
    args = parse_arguments()
    file_name = args.ip_list
    threads = int(args.threads)

    # Get the IP of the current interface
    source_ip = get_private_ip()

    #process_bulk_files()
    load_file (file_name, threads, source_ip)
    #load_file_parallel (file_name, threads, source_ip)
