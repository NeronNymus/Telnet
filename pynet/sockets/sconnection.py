#!/usr/bin/env python3

# This script perform telnet remote_sockets using socket instead of telnetlib.
# The intention is to execute command sequences quickly.
# Save logs and analyze output for creation of more command sequences.

import sys
import time
import socket
from datetime import datetime

# Personal packages
from utils.colors import Colors

auth_timeout = 0.3
remote_sockets = list()

EOF     = b'\x04'   # End of File  [004]
ENTER   = b'\r\x00' # Enter Key    [013]

username = b'root\r\n'
password = b'adminHW\r\n'

global_error = False


# Return a socket with the telnet session
def telnet_auth_sequence(remote_host, remote_port, log_output=None):

    global global_error

    # Record the start time before attempting the remote_socket
    start_time = datetime.now()

    remote_socket = None
    try:
        # connect to the remote host
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_socket.settimeout(1)
        remote_socket.connect((remote_host, remote_port))
        #print(Colors.BOLD_WHITE + f"[!] Remote socket established: [{remote_host}:{remote_port}]" + Colors.R)

        # Add the remote socket to the list
        remote_sockets.append(remote_socket)

    except Exception as e:
        global_error = True
        print(Colors.RED + f"[x] Error XYZ:\t\t{e}" + Colors.R)
        return

    # Execute login command sequence
    login_sequence = [username, password, ENTER]
    response = socket_send_sequence(remote_socket, login_sequence, auth_timeout, False, log_output)

    # Calculate the elapsed time even in case of remote_socket error
    elapsed_time = datetime.now() - start_time


    #if "Last login" in response.decode('latin'):
    if "Last login" in response:
        print(Colors.GREEN + f"[!] Successful Telnet Session to [{remote_host}:{remote_port}]" + Colors.R)
        print(Colors.GREEN + "---------------------------------------------------------------------" + Colors.R)
        global_error = False
    else:
        print(Colors.RED + f"[x] Failed Telnet Session to [{remote_host}:{remote_port}]" + Colors.R)
        global_error = True


    print(Colors.ORANGE + f"[!] Elapsed time: {elapsed_time}" + Colors.R)
    #if global_error == False:
    #    print(Colors.GREEN + "---------------------------------------------------------------------" + Colors.R)
    #else:
    #    print(Colors.RED + "---------------------------------------------------------------------" + Colors.R)

    # Final return
    return remote_socket


# For sending single commands
def socket_send_data(remote_socket, data, timeout=1, detail=False, max_retries=5):

    remote_socket.sendall(data)

    response = b''
    for i in range(max_retries):
        try:
            response += remote_socket.recv(1024)
            time.sleep(timeout) # Sleep time for receiving all the response
            break
        except:
            continue

    if detail == True:
        print(Colors.GREEN + "[<==] Received:" + Colors.R + f"\n{response}\n")
        print(Colors.GREEN + "---------------------------------------------------------------------" + Colors.R)

    return response


# For sending list of commands. It is possible to save the output log
# timeout works for each command in the provided commands list
def socket_send_sequence(remote_socket, commands, timeout=1, detail=False, log_output=None):

    global global_error

    cont = 1
    response = b''
    for command in commands:
        if detail:
            print(Colors.BOLD_WHITE + f"[{cont}] Sending this command:" + Colors.ORANGE + f"\n{command}\n" + Colors.R)

        response += socket_send_data(remote_socket, command, timeout, detail)
        cont += 1

    # Write decoded output to a log
    with open(log_output, 'a') as file:
        response = response.decode('latin') #+ "\n"
        #response = response.decode('ascii') + "\n"
        file.write(response)
        print(Colors.BOLD_WHITE + "[!] Logged output into:"+ Colors.ORANGE + f"\n{log_output}" + Colors.R)
        if global_error == True:
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

    if remote_socket:
        remote_socket.sendall(command)

        # Doesn't wait for a response and maintain active the socket
        print(Colors.GREEN + "[!] Maintaining remote telnet session ACTIVE...." + Colors.R)
        while remote_socket:
            time.sleep(1)




# This method is for sending the command and waiting for the response
# all the necessary time
def socket_send_commands(remote_socket, commands, timeout, detail=False):    # There's not a timeout here

    cont = 1
    response = b''
    for command in commands:
        if detail:
            print(Colors.BOLD_WHITE + f"[{cont}] Sending this command:" + Colors.ORANGE + f"\n{command}\n" + Colors.R)
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

