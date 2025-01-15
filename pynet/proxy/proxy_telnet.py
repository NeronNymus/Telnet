#!/usr/bin/env python3

# This specific proxy is tailored for port 23 Telnet service

import sys
import time
import socket
import signal
import threading
from itertools import cycle

# Global variable to track client sockets
client_sockets = []
remote_sockets = []
server = None

timeout = 2

# Signal handler function to catch Ctrl+C
def signal_handler(sig, frame):
    print("\n\n[!] Exiting gracefully...")

    # Close all open client sockets
    for client_socket in client_sockets:
        client_socket.close()

    for remote_socket in remote_sockets:
        remote_socket.close()

    # Close the server bind port
    if server:
        server.close()

    sys.exit(0)

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

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

# Example commands
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


def server_loop(local_host, local_port, remote_host, remote_port):

    global server

    # Establish the socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host, local_port))
    except:
        print("[x] Failed to listen on %s:%d" % (local_host, local_port))
        sys.exit(0)

    print("[!] Listening on %s:%d\n" % (local_host, local_port))

    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        # Print out the local connection information
        print("[->] Received incoming connection from %s:%d" % (addr[0], addr[1]))

        # Add the remote socket to the list
        client_sockets.append(client_socket)

        # Start a thread to talk to the remote host
        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket, remote_host, remote_port))
        proxy_thread.start()


def auth_sequence(client_socket, remote_host, remote_port):

    remote_socket = None
    try:
        # connect to the remote host
        print(f"[!] Trying connect to remote host [{remote_host}:{remote_port}]")
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_socket.connect((remote_host, remote_port))
        print(f"[!] Remote socket established: [{remote_host}:{remote_port}]\n")

        # Add the remote socket to the list
        remote_sockets.append(remote_socket)

    except Exception as e:
        print(f"[x] Error XYZ:\n{e}\n")
        return

    print("---------------------------------------------------------------------")
    # Send EOF in the first request
    proxy_command(remote_socket, client_socket, EOF)

    print("---------------------------------------------------------------------")
    # Now send 'root\r\n' to server
    username = b'root\r\n'
    #proxy_command(remote_socket, client_socket, username)

    print("[==>]\tSending [USERNAME] of %d bytes from this [proxy]  to [server] telnet.\n" % (len(username)))
    remote_socket.sendall(username)
    time.sleep(timeout)
    response = remote_socket.recv(4096)
    print(f"[<==] Received:\n{response}\n")

    # Redirect response to of previous command to client serving as proxy
    print("[<==]\tSending [RESPONSE] of %d bytes from this [proxy]  to [client] telnet.\n" % (len(response)))
    client_socket.sendall(response)
    time.sleep(timeout)
    print("---------------------------------------------------------------------")

    # Now send 'adminHW\r\n' to server
    passphrase = b'adminHW\r\n'
    print("[==>]\tSending [PASSPHRASE] of %d bytes from this [proxy]  to [server] telnet.\n" % (len(passphrase)))
    remote_socket.sendall(passphrase)
    time.sleep(timeout)
    response = remote_socket.recv(4096)
    print(f"[<==] Received:\n{response}\n")

    ## Redirect response
    print("[<==]\tSending [RESPONSE] of %d bytes from this [proxy] to [client] telnet.\n" % (len(response)))
    client_socket.sendall(response)
    time.sleep(timeout)
    print("---------------------------------------------------------------------")

    # Send ENTER
    print("[==>]\tSending [ENTER] of %d bytes from this [proxy]  to [server] telnet.\n" % (len(EOF)))
    remote_socket.sendall(ENTER)
    time.sleep(timeout)
    response = remote_socket.recv(1024)
    print(f"[<==] Received:\n{response}\n")
    
    ## Redirect '\r\nWAP' response to client
    print("[<==]\tSending [RESPONSE] of %d bytes from this proxy to [client] telnet.\n" % (len(response)))
    client_socket.sendall(response)
    print("---------------------------------------------------------------------")

    
    # Send commands and print responses
    #for command in commands:
    #    proxy_command(remote_socket, client_socket, command)

    # Final return
    return remote_socket


def proxy_command(remote_socket, client_socket, command, nbytes=4096):
    print(f"[==>]\tSending [{command}] of %d bytes from this [proxy]  to [server] telnet.\n" % (len(command)))
    remote_socket.sendall(command)
    time.sleep(timeout)
    response = remote_socket.recv(nbytes)
    print(f"[<==] Received:\n{response}\n")

    ## Redirect response to client
    print("[<==]\tSending [RESPONSE] of %d bytes from this proxy to [client] telnet.\n" % (len(response)))
    client_socket.sendall(response)
    time.sleep(timeout)



def proxy_handler(client_socket, remote_host, remote_port):

    remote_socket = auth_sequence(client_socket, remote_host, remote_port)

    print("---------------------------------------------------------------------")
    print("[!!!] Begins dynamic code!")

    while True:

        print("---------------------------------------------------------------------")
        print(f"[!]\tListening for data from localhost...")
        try:

            # This is the problematic code
            client_buffer = receive_large_buffer(client_socket, 1024, timeout)

            # send it to our request handler 
            client_buffer = request_handler(client_buffer)
            #client_buffer = help_handler(client_buffer)

            print(f"\n[==>]\tClient Buffer:\n{client_buffer}\n")

            if len(client_buffer):
                print("[==>]\tSending %d bytes from [proxy host] to [remote target].\n" % (len(client_buffer)))

                # Send to the remote host the client_buffer
                remote_socket.sendall(client_buffer)

                #remote_buffer = remote_socket.recv(8192)
                remote_buffer = receive_large_buffer(remote_socket, 8192, 5)

                if remote_buffer != b'':

                    print("---------------------------------------------------------------------")
                    print("[<==]\tReceived %d bytes from remote socket." % (len(remote_buffer)))
                    print(remote_buffer)
                    print()

                    print("[<==]\tReceived %d bytes from remote socket to client." % (len(remote_buffer)))
                    client_socket.sendall(remote_buffer)

                    continue
            
            continue    # Repeat the loop

        except Exception as e:
            print(f"\n[!]\tError xyz:\n{e}\n")
            break

        # if no more data on either side, close the connections
        if not len(client_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print("[!] No more data. Closing the connections.")

            break


def receive_large_buffer(remote_socket, buffer_size=8192, timeout=10):
    buffer = b""
    remote_socket.settimeout(timeout)

    try:
        while True:
            data = remote_socket.recv(buffer_size)
            if not data:
                break
            buffer += data
    except socket.timeout:
        pass
    except Exception as e:
        print(f"Error receiving data: {e}")

    return buffer


# Ctrl+C singal
def exec_ctrl_c(buffer):
    buffer = IAC + IP + IAC + DO + '\x06'
    return buffer


# Returns a list with commands from a file 
def list_help_commands():
    
    # Include hardcoded path for the commands
    commands_path = "/mnt/Kali/home/grimaldi/Bash/Telnet/commands/commands.md"

    # A list to store available commands
    available_commands = list()

    with open(commands_path, 'r') as commands_file:
        for command in commands_file:
            #print(command)
            command = command[:-1]
            available_commands.append(command)

    return available_commands

# Defines a global list
available_commands = list_help_commands()
del available_commands[0]
command_iterator = cycle(available_commands)


def help_handler(buffer):

    command = next(command_iterator)

    try:
        
        # Convert the command string with escaped characters to bytes
        command_bytes = bytes(command, 'latin1').decode('unicode_escape').encode('latin1')
        
        # Append the necessary newline characters for Telnet
        buffer = command_bytes + b' ? \r\n'
        print(f"[==>] Sending this buffer instead:\n{buffer}\n")
        return buffer

    except Exception as e:
        print(f"Error: \n{e}")
        return buffer


# modify content
def request_handler(buffer):

    print(f"[==>] Payload for sending:\n{buffer}")
    value = input("\n[!] Do you want to preserve it? [y/n] ")

    if value.lower() == "y":
        return buffer

    elif value.lower() == "n":
        print("[!] Modify payload sent to the server. Then press Ctrl+D to send it:\n")
        try:
            #get_help_messages()

            # Read the command input until EOF (Ctrl+D / Ctrl+Z)
            command = sys.stdin.read().strip()
            print()
            
            # Convert the command string with escaped characters to bytes
            command_bytes = bytes(command, 'latin1').decode('unicode_escape').encode('latin1')
            
            # Append the necessary newline characters for Telnet
            buffer = command_bytes #+ b'\r\n'
            #buffer = command_bytes + ENTER

            #buffer = hex_to_bytes(command)

            return buffer
        except Exception as e:
            print(f"Error: \n{e}")
            return buffer


def hex_to_bytes(command):
    # Remove the \x notation
    command = command.replace('\\x', '')

    # Convert to bytes
    command = bytes.fromhex(command)

    return command


# modify content
def response_handler(buffer):
    return buffer


def send_EOF(remote_socket):

    # Equivalent to Ctrl+D
    client_buffer = EOF                 
    print("[==>] Sending EOF to remote host\n")
    remote_socket.sendall(client_buffer)
    
    # Receive the frist response
    remote_buffer = remote_socket.recv(4096)

    print("[<==]\tReceived %d bytes from remote socket." % (len(remote_buffer)))
    print(remote_buffer)


def receive_first(remote_socket):
    # Receive banner first
    remote_buffer = remote_socket.recv(4096)

    print("[<==]\tReceived %d bytes from remote socket.\n" % (len(remote_buffer)))
    print(remote_buffer)

    # Equivalent to Ctrl+D
    time.sleep(1)
    print("[==>] Sending EOF to remote host\n")
    remote_socket.sendall(EOF)

    # Receive banner first
    remote_buffer = remote_socket.recv(4096)

    print("[<==]\tReceived %d bytes from remote socket." % (len(remote_buffer)))
    print(remote_buffer)


# print traffic content
FILTER=''.join([(len(repr(chr(x)))==3) and chr(x) or '.' for x in range(256)])
def hexdump(src, length=16):
    N=0; result=''
    while src:
       s,src = src[:length],src[length:]
       hexa = ' '.join(["%02X"%ord(x) for x in s])
       s = s.translate(FILTER)
       result += "%04X   %-*s   %s\n" % (N, length*3, hexa, s)
       N+=length
    return result


def main():

    # Simple command-line parsing here
    if len(sys.argv[1:]) != 4:
        print("Usage: ./proxy.py [remotehost] [remote_port] [localhost] [localport]")
        print("Example:\n./proxy_telnet.py 192.168.100.1 23 127.0.0.1 9000")
        sys.exit(0)

    # Setup local listening parameters
    local_host = sys.argv[3]
    local_port = int(sys.argv[4])

    # Setup remote target
    remote_host = sys.argv[1]
    remote_port = int(sys.argv[2])

    # spin up our listening socket
    server_loop(local_host, local_port, remote_host, remote_port)


if __name__ == "__main__":
    main()
