#!/usr/bin/env python3

import os
import sys
from scapy.layers.inet import IP, ICMP

# Add parent directory to Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Personal packages
from args.backend import connect_to_database
from args.backend_asyn import create_pool


# Main function
def main():

    conn = connect_to_database()


if __name__ == "__main__":
    main()

