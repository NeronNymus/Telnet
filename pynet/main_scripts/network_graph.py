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

# Global Variables
octets = 4
octets_global = 0
difference_octets = 0

vector_global = [0] * octets
common_octets_list_global = list()
list_global = list()


# Main function
def main(csv_path, ips_path, common_octets):

    analysis_name = ips_path + ".analysis"

    #conn = connect_to_database()

    global octets
    global octets_global
    global vector_global
    global common_octets_list_global
    global difference_octets
    
    common_octets = int(common_octets) # Cast 'str' to 'int'
    difference_octets = octets - common_octets
    vector_local = [0] * octets

    
    list_of_lists = list()
    common_octets_list = list() # Store common octets
    

    # Read the ips
    cont = 1
    for line in read_large_file(ips_path):

        # Assign the octect values to an array
        splitted = line.strip().split('.')
        for i in range(octets):
            vector_global[i] = splitted[i]


        # Count the number of same octects to the last one
        intersect_octects = 0
        for i in range(octets):
            if vector_local[i] == vector_global[i]:
                intersect_octects += 1

        # Compare the intersected octets respective to the previous row
        if intersect_octects >= common_octets - difference_octets:
            if octets_global - intersect_octects == difference_octets:
                list_of_lists.append(common_octets_list)
                common_octets_list = []  # Reset the list for new group

            # Prepare the ip and append it to the common_octets_list
            ip = '.'.join(vector_global)
            common_octets_list.append(ip) # Append the ip


        # Update the new octects preparing the next loop
        for i in range(octets):
            vector_local[i] = vector_global[i]

        # Update the octets_global
        octets_global = intersect_octects
        
        cont += 1

    # Append the last list
    if common_octets_list:
        list_of_lists.append(common_octets_list)
        common_octets_list = []  # Reset the list for new group

    # Print the list of lists for verification
    sizes_list = list()
    for i, item in enumerate(list_of_lists):
        # Prepare data for appending into the sizes_list
        length = len(item)

        if item:
            split = item[0].split('.')
            prefix = '.'.join(split[:-difference_octets])

            # Append
            sizes_list.append((prefix,length))

    # Sort the sizes_list by the size value (second element of the tuple)
    sizes_list_sorted = sorted(sizes_list, key=lambda item: item[1])

    # Print the subnetworks
    #for i, item in enumerate(list_of_lists):
    #    print(f"\n[{i}] -> {item}")


    # Loop thorugh the sizes list data
    with open(analysis_name, 'a') as file:
        for i, item in enumerate(sizes_list_sorted):
            prefix = item[0]
            size = item[1]

            print(f"\nList ({i+1}) Prefix: {prefix} Size: {size}")
            file.write(f"{prefix},{size}\n") # Write to the file for further analysis


def loop_scans(csv_path, common_octets):
    hard_scan_dir = os.path.abspath("../../scans/crawling/ips_up_port_23_10.0.0.0_8")

    #print(hard_scan_dir)
    #print(len(os.listdir(hard_scan_dir))) 

    base_names = sorted (os.listdir(hard_scan_dir))

    for base_name in base_names:
        if 'clean' in base_name:
            scan_name = hard_scan_dir + "/" + base_name
            analysis_name = scan_name + ".analysis"
            print(analysis_name)

            main (csv_path, scan_name, common_octets)



if __name__ == "__main__":
    # Receives files as arguments from the console
    parser = argparse.ArgumentParser(description="Process a CSV file and an IPs file.")
    parser.add_argument('csv_path', type=str, help="Path to the CSV file")
    parser.add_argument('ips_path', type=str, help="Path to the IPs file")
    parser.add_argument('common_octets', type=str, help="Number of common octets")
    
    args = parser.parse_args()

    #main(args.csv_path, args.ips_path, args.common_octets)
    loop_scans(args.csv_path, args.common_octets)
