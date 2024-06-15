#!/usr/bin/env python3

# This python program is for modeling IP's from the botnet

import os
import sys
import csv
import argparse

# Add parent directory to Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Personal packages
from utils.reading import *
from graphing.graph_functions import *

#from args.backend import connect_to_database
#from args.backend_asyn import create_pool


# Main function
def main(csv_path, ips_path):

    #conn = connect_to_database()

    # Call the graph function
    G = directed_graph(csv_path)
    #print(G.edges)

    # Draw the graph
    draw_graph(G)
    #draw_graph2(G)


    # Read the ips
    #for line in read_large_file(ips_path):
    #    print(line)


if __name__ == "__main__":
    # Receives files as arguments from the console
    parser = argparse.ArgumentParser(description="Process a CSV file and an IPs file.")
    parser.add_argument('csv_path', type=str, help="Path to the CSV file")
    parser.add_argument('ips_path', type=str, help="Path to the IPs file")
    
    args = parser.parse_args()

    main(args.csv_path, args.ips_path)
