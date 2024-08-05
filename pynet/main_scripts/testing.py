#!/usr/bin/env python3

import os
import sys
from scapy.layers.inet import IP, ICMP

# Add parent directory to Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Personal packages
from args.backend import connect_to_database
from pings.listener import *


# Main function
def main():

    #conn = connect_to_database()


    # Create a mock ICMP packet
    #private_ip="10.39.84.122"
    destination_ip="192.168.100.233"
    mock_packet = IP(dst=destination_ip) / ICMP()

    # Call the listener function
    packet_callback(mock_packet)



if __name__ == "__main__":
    main()

