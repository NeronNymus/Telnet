#!/usr/bin/env python3

# Imports
import warnings
# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import os
import sys
import telnetlib

conn_timeout = 15

def main(remote_host, remote_port):

    # Open a Telnet connection
    tn = telnetlib.Telnet(remote_host, remote_port)
    print(f"\n[!] Connected to [{remote_host}:{remote_port}]\n")

    # login sequence
    username = "root"
    password = "adminHW"
    tn = connect_to_ip(remote_host, remote_port, username, password)

    command = "wap top"

    send_telnet_command(tn, command)

    # Close the connection
    if tn:
        tn.close()


def connect_to_ip(ip_address, port, username, password):
    print(f"\n[!] Trying to connect with the next details: \n"
          f"Port:\t{port} \n"
          f"IP:\t{ip_address} \n" + 
          f"-------------------------------------------------------------------------")

    cur = None

    try:
        tn = telnetlib.Telnet(ip_address, timeout=conn_timeout)  # Increased timeout
        output = tn.read_until(b"Username: ", timeout=conn_timeout)  # Increased timeout
        print("Received:", output.decode('ascii'))
        tn.write(username.encode('ascii') + b"\n")
        output = tn.read_until(b"Password: ", timeout=conn_timeout)  # Increased timeout
        print("Received:", output.decode('ascii'))
        tn.write(password.encode('ascii') + b"\n")

        print("[!] Successfully connected.")

        return tn  # Return the telnet object for further use

    except Exception as e:
        print(f"[#] Connection error: \n{e}")
        return None


def send_telnet_command(tn, command):
    tn.write(command)

    response = tn.read_some()
    print(response.decode('ascii', errors='replace'))


if __name__ == "__main__":
    # Parse arguments
    if len(sys.argv) != 3:
        print("Usage: ./telnet_client.py <remote_host> <remote_port>")
        sys.exit(0)

    remote_host = sys.argv[1]
    remote_port = int(sys.argv[2])

    main(remote_host, remote_port)