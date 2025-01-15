#!/usr/bin/env python3

# This script is for performing analysis on the backend data.

import sys
import argparse

# Import personal packages
from utils.colors import Colors
from backend.backend import conn_simple

# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="PyNet - A Python-based tool for backend analysis of telnet command results.")
    parser.add_argument("-a", "--analysis", default=1, type=int, help="\t\t(Which analysis number must be performed).")
    parser.add_argument("-e", "--examples", action='store_true', help="\t\tShow execution examples")
    return parser.parse_args()


# Execution examples
def show_examples():
    print()
    print(Colors.ORANGE + "[!] Command examples: " + Colors.R)
    print("python3 pynet_analysis.py -a 1\t\t(Perform first analysis)")
    print("python3 pynet_analysis.py -e\t\t(Show this examples message)")
    print("python3 pynet_analysis.py -h\t\t(Show help message)")
    sys.exit(0)


if __name__ == "__main__":

    # Parse command-line arguments
    args = parse_arguments()

    if args.examples:
        show_examples()
