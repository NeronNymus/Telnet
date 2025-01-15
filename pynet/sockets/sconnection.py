#!/usr/bin/env python3

# This script perform telnet remote_sockets using socket instead of telnetlib.
# The intention is to execute command sequences quickly.
# Save logs and analyze output for creation of more command sequences.

import sys
import csv
import time
import socket
from datetime import datetime

# Personal packages
from utils.colors import Colors
from commands.telnet_combinations import auth_request2
from backend.backend import telnet_process_ips

auth_timeout = 1
commands_timeout = 1
remote_sockets = list()

EOF     = b'\x04'   # End of File  [004]
ENTER   = b'\r\x00' # Enter Key    [013]

# Default credentials
username = b'root\r\n'
password = b'adminHW\r\n'

global_error = False

# Return a socket with the telnet session
def telnet_auth_sequence(remote_host, remote_port, credentials_path, log_output=None, max_retries=5, detail=True):

    global global_error
    global auth_timeout
    global commands_timeout
    global username, password

    # Import credentials distinct to defaults one when specified
    if not credentials_path.endswith('default.csv'):
        with open(credentials_path, 'r') as file:
            for line in file:
                items = line.split(',')
                
            username = items[0] + '\r\n'
            password = items[1].rstrip() + '\r\n'
            username = username.encode()
            password = password.encode()


    # Record the start time before attempting the remote_socket
    start_time = datetime.now()

    remote_socket = None
    try:
        # connect to the remote host
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        for i in range(0, max_retries):
            try:
                remote_socket.settimeout(auth_timeout)
                remote_socket.connect((remote_host, remote_port))

                # Add the remote socket to the list
                remote_sockets.append(remote_socket)
            except:
                continue

    except Exception as e:
        global_error = True
        if detail:
            print(Colors.RED + f"[x] Error XYZ:\t\t{e}" + Colors.R)
        return

    # Execute login command sequence
    #login_sequence = [username, password, ENTER]
    login_sequence = [username, password]

    # Another version for negotiation tries before login sequence
    #negotiation     = [ENTER, auth_request2]
    #login_sequence  = negotiation + login_sequence
    #login_sequence  = login_sequence + negotiation

    # Receive response
    response = socket_send_sequence(remote_socket, login_sequence, auth_timeout, True, log_output)

    # Calculate the elapsed time even in case of remote_socket error
    elapsed_time = datetime.now() - start_time

    # Properly cast the variable
    if type(response) is bytes:
        response = response.decode('latin')

    if "Last login" in response:
        login_data = [ remote_host, remote_port, elapsed_time, datetime.now() ]
        login_log(login_data)   # Data is logged into a file

        if detail:
            print(Colors.GREEN + f"[!] Successful Telnet Session to [{remote_host}:{remote_port}]" + Colors.R)
            print(Colors.GREEN + "---------------------------------------------------------------------" + Colors.R)
        global_error = False
    else:
        if detail:
            print(Colors.RED + f"[x] Failed Telnet Session to [{remote_host}:{remote_port}]" + Colors.R)
        global_error = True
        return remote_socket


    if detail:
        print(Colors.ORANGE + f"[!] Elapsed time: {elapsed_time}" + Colors.R)

    # Final return
    return remote_socket

# Take a list of login data and log it for further import into a database
def login_log(login_data, log_file='new_logins.csv'):
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(login_data)


# This methods doesn't include a timeout, it waits for all the data to be received
def socket_receive_all(remote_socket, byte_size=4096, end_marker=b"WAP>", timeout=5):
    buffer = b''
    start_time = time.time()

    try:
        while True:
            data = remote_socket.recv(byte_size)
            if not data:
                break

            buffer += data

            # Check for end marker indicating the server finished its response
            if end_marker in buffer:
                break

            # Reset the timeout if data is still being received
            start_time = time.time()

            # Break if no data has been received for the timeout duration
            if time.time() - start_time > timeout:
                break
    except Exception as e:
        pass  # Handle any exception if necessary (don't print in this case)

    return buffer


def socket_send_data(remote_socket, command, timeout=5, detail=False, max_retries=5):
    global global_error

    if remote_socket is None or remote_socket.fileno() == -1:
        if detail:
            print("[!] Socket closed.")
        global_error = True
        return b''

    # Attempt to send the command
    for _ in range(max_retries):
        try:
            remote_socket.sendall(command)
            break
        except Exception as e:
            print(f"[!] Error sending command: {e}")
            continue

    # Fetch remote IP address
    remote_ip = None
    try:
        remote_ip = remote_socket.getpeername()[0]
    except Exception as e:
        print(f"[!] Error fetching remote IP: {e}")

    # Define command-specific actions
    decoded_command = command.rstrip().decode()
    switch = {
        "ip neigh": {
            "expected_pattern": b"ip neigh",
            "handler": lambda response: telnet_process_ips(response, remote_ip),  # Pass remote IP to handler
        },
    }

    # Get the expected pattern and handler
    action = switch.get(decoded_command, {})
    expected_pattern = action.get("expected_pattern", None)
    handler = action.get("handler", None)

    # Initialize response variables
    response = b''
    start_time = time.time()

    while True:
        chunk = socket_receive_all(remote_socket, timeout=timeout)
        response += chunk

        # Check if the expected pattern is found and if the response ends with "WAP>"
        if expected_pattern and expected_pattern in response and response.endswith(b"WAP>"):
            if detail:
                print(Colors.GREEN + "[*] Expected pattern detected for database import!" + Colors.R)
            # Call the handler only when the response ends with "WAP>"
            if handler:
                handler(response)
            break

        # Timeout condition (no response received within timeout duration)
        if time.time() - start_time > timeout:
            break

    # Log the response
    print(response)
    return response


# For sending list of commands. It is possible to save the output log
# timeout works for each command in the provided commands list
def socket_send_sequence(remote_socket, commands, timeout=1, detail=True, log_output=None, delay=2):
    global global_error


    response = b''

    if not remote_socket:
        return response

    cont = 1
    for command in commands:
        if detail and global_error is False:
            pass
            print(Colors.BOLD_WHITE + f"[{cont}] Sending this command:" + Colors.ORANGE + f"\n[==>] Sending:\n{command}\n" + Colors.R)

        # Send the data to remote socket
        if global_error is False:
            response += socket_send_data(remote_socket, command, timeout, detail)

        time.sleep(delay)
        cont += 1

    if log_output:
        # Write decoded output to a log
        with open(log_output, 'a') as file:
            response = response.decode('latin') #+ "\n"
            #response = response.decode('ascii') + "\n"
            file.write(response)
            if log_output:
                pass
                print(Colors.BOLD_WHITE + "[!] Logged output into:"+ Colors.ORANGE + f"\n{log_output}" + Colors.R)
            if global_error == True and detail:
                print(Colors.RED + "---------------------------------------------------------------------" + Colors.R)
                global_error = False # refresh the boolean

        # Close the file properly
        file.close()

    return response




# This method is for sending a single command that doesn't finish and we need to maintain
# Per example, executing a ping on the remote telnet
def socket_send_command(remote_socket, command, detail=False):
    if detail:
        print(Colors.BOLD_WHITE + f"[!] Sending this command, no waiting response:" + Colors.ORANGE + f"\n{command}\n" + Colors.R)
        pass

    if remote_socket is None or remote_socket.fileno() == -1:
        print("[!] Socket closed.")
        pass
    else:
        remote_socket.sendall(command)

        # Doesn't wait for a response and maintain active the socket
        if detail:
            print(Colors.GREEN + "[!] Maintaining remote telnet session ACTIVE...." + Colors.R)
        pass
        while remote_socket:
            time.sleep(1)


# This method is for sending the command and waiting for the response
# all the necessary time
def socket_send_commands(remote_socket, commands, timeout, detail=True):    # There's not a timeout here

    cont = 1
    response = b''
    for command in commands:
        if detail:
            print(Colors.BOLD_WHITE + f"[{cont}] Sending this command:" + Colors.ORANGE + f"\n{command}\n" + Colors.R)
            pass
        remote_socket.sendall(command)

        response = receive_from(remote_socket, timeout)

        if detail == True:
            print(Colors.GREEN + "[<==] Received:" + Colors.R + f"\n{response}\n")
            print(Colors.GREEN + "---------------------------------------------------------------------" + Colors.R)

        cont+=1

    return response


def receive_from(remote_socket, timeout):
    buffer = ""
    # we set a 2 second timeout, depending on your target this may need to be adjusted
    remote_socket.settimeout(timeout)

    try:
        # keep reading into the buffer until there's no more data
        # or we timeout
        while True:
            data = remote_socket.recv(4096)

            if not data:
                break

            buffer += data
    except:
        pass

    return buffer

