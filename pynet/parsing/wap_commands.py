#!/usr/bin/env python3

# This script serve for parsing output from the WAP commands.

import re
from utils.colors import Colors
from sockets.sconnection import socket_send_data, socket_receive_all

# global variable paths
paths = list()


def log_response(response, log_output):
    if log_output:
        # Write decoded output to a log
        with open(log_output, 'a') as file:
            print(Colors.GREEN + "[<==] Received:" + Colors.R + f"\n{response}\n")
            print(Colors.GREEN + "---------------------------------------------------------------------" + Colors.R)

            file.write(response)
            print(Colors.BOLD_WHITE + "[!] Logged output into:"+ Colors.ORANGE + f"\n{log_output}" + Colors.R)

        # Close the file properly
        file.close()

    return response


def log_list(mylist, log_paths):
    if log_paths and len(mylist) != 0:
        with open(log_paths, 'a') as file:
            for item in mylist:
                file.write(item + "\n")
                #print(Colors.BOLD_WHITE + "[!] Logged output into:"+ Colors.ORANGE + f"\n{log_paths}" + Colors.R)

        file.close()



## pseudo ls implemented using 'wap top'
def ls(remote_socket, wap_path, format=1):
    
    ls_command = f"wap list format {format} path {wap_path}\r\n"
    ls_command = ls_command.encode('ascii')
    print(ls_command)

    response = socket_send_data(remote_socket, ls_command, True)
    #response = socket_receive_all(remote_socket)
    response = response.decode('latin')

    return response


def get_directories(wap_path, response, log_paths):
    """
    Parses the response from the 'ls' command to extract directory paths.
    """
    global paths

    lines = response.splitlines()
    for line in lines:
        if line.startswith("dr"): #or line.startswith("lr"):
            parts = line.split()
            # The directory name is the last part of the line
            path = parts[-1]
            if path == "/bin/busybox.nosuid" or path == "/sbin/busybox.suid":
                path = parts[-2]
            
            if wap_path.endswith("/"):
                paths.append(wap_path +  path)
            elif path.startswith("/"):
                paths.append(wap_path +  path)
            else:
                paths.append(wap_path +  "/" + path)

    return paths


def pseudo_tree(remote_socket, wap_path, max_depth, log_output=None, log_paths=None, current_depth=1, format=1):
    """
    Recursively lists directories and subdirectories up to max_depth.
    """

    global paths
    if current_depth > max_depth:
        return

    # Receive ls response and logged into output
    response = ls(remote_socket, wap_path, format)
    response = log_response(response, log_output)

    # Receive directory paths and logged it
    paths = get_directories(wap_path, response, log_paths)
    paths_backup = paths
    log_list(paths_backup, log_paths)

    for path in paths:
        pseudo_tree(remote_socket, path, max_depth, log_output, log_paths, current_depth + 1, format)
    

if __name__ == "__main__":
    response = """dr-xr-xr-x 2	root root	7264	2023-10-20 10:26:01 bin
    dr-xr-x--- 2	root root	3	2023-10-20 10:26:01 boot
    drwxr-xr-x 5	root root	3040	1970-01-01 00:00:00 dev
    dr-xr-xr-x 17	root root	919	2023-10-20 10:26:01 etc
    dr-xr-x--- 13	srv_web service	278	2023-10-20 10:26:01 html
    lrwxrwxrwx 1	root root	19	2023-10-20 10:26:01 init -> /bin/busybox.nosuid
    dr-xr-xr-x 7	root root	10916	2023-10-20 10:26:01 lib
    dr-xr-xr-x 3	root root	28	2023-10-20 10:26:01 libexec
    lrwxrwxrwx 1	root root	19	2023-10-20 10:26:01 linuxrc -> /bin/busybox.nosuid
    drwxr-xr-x 6	root root	120	1970-01-01 00:00:01 mnt
    dr-xr-xr-x 189	root root	0	1970-01-01 00:00:01 proc
    drwx------ 2	root root	3	2023-10-20 10:26:01 root
    dr-xr-xr-x 2	root root	846	2023-10-20 10:26:01 sbin
    dr-xr-xr-x 4	root root	41	2023-10-20 10:26:01 share
    dr-xr-xr-x 12	root root	0	1970-01-01 00:00:01 sys
    drwxrwxrwx 7	root root	200	2024-07-31 23:06:35 tmp 
    dr-xr-xr-x 10	root root	114	2023-10-20 10:26:01 usr
    drwxrwxrwx 41	root root	3820	2024-08-01 03:45:41 var

    success!"""


    print(response)
    print()

    wap_path = "/"
    paths = get_directories(wap_path, response)

    for path in paths:
        print(path)
