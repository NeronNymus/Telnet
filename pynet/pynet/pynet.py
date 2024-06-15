#!/usr/bin/env python3

import os
import sys
import time
import argparse


# Personal packages
from utils.colors import Colors
from args.connection import connect_to_ip, send_command, get_private_ip
from args.backend import connect_to_database, save_ifconfig, exec_ifconfig, check_existing_record
#from args.backend_asyn import exec_ifconfig, save_ifconfig


# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="PyNet - A Python-based tool for telnet and network operations.")
    parser.add_argument("-iL", "--ip_list", help="\t\tPath to a file containing a list of IP addresses or hostnames, one per line.")
    parser.add_argument("-i", "--ip", help="\t\tTarget IP address or hostname.")
    parser.add_argument("-p", "--port", default=23, type=int, help="\t\tTarget port (default is 23 for Telnet).")
    parser.add_argument("-u", "--username", help="\t\tUsername for authentication.")
    parser.add_argument("-pw", "--password", help="\t\tPassword for authentication.")
    parser.add_argument("-l", "--login", help="\tSimply login on the target system using 'True'.")
    parser.add_argument("-c", "--command", help="\tCommand to execute on the target system.")
    return parser.parse_args()


# Main function
def main():

    # Parse command-line arguments
    args = parse_arguments()

    # Connect to the database
    conn = connect_to_database()

    # Fetch the private ip of host running this python script
    source_ip = get_private_ip()

    # Check if -iL or -i is provided
    if args.ip_list:
        ip_list_path = args.ip_list
        # Read the IP list file and iterate through the IP addresses
        with open(ip_list_path, 'r') as file:
            ip_addresses = file.read().splitlines()
        
        print(args.login)

        ip_cont = 1
        ip_cont_2 = 1
        for ip in ip_addresses:

            # Simply perform a telnet connection.
            if args.login == 'True':
                print(Colors.BOLD_WHITE + f"\n[{ip_cont}] [{ip_cont_2}] Processing IP: {ip}" + Colors.R)
                tn = connect_to_ip(conn, source_ip, ip, args.username, args.password, args.port) # Perform a telnet connection 

            #if not check_existing_record(conn, ip, args.command):
                #pass
                #print(f"\n[{ip_cont}] [{ip_cont_2}] Processing IP: {ip}")
                #tn = connect_to_ip(conn, source_ip, ip, args.username, args.password, args.port) # Perform a telnet connection 

                # Execute commands in sequence using the same connection
                #exec_ifconfig (conn, ip, tn, args.command)
                
                # Create a connection pool
                #pool = await create_pool()

                # Asynchronous
                #await exec_ifconfig(pool, ip, tn, command)

            #else:
                #print(f"\n[{ip_cont}] [{ip_cont_2}] Record already exists for IP:", ip)
                #ip_cont_2 += 1

            ip_cont += 1

    elif args.ip:
        print(f"\nProcessing IP: {args.ip}")
        exec_ifconfig (conn, args.ip, tn, args.command)
    else:
        print("Error: Please provide either -iL or -i option to specify the target IP(s).")


if __name__ == "__main__":
    main()


