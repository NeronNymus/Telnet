#!/usr/bin/env python3 

# This script works for splitting a file into a determine number of files

import os
import sys
import ipaddress

def split_file(file_path, number_parts):
    print(file_path)
    print(number_parts)

def validate_cidr_block(cidr_block):
    try:
        # Try to create an ip_network object; if it's invalid, it will raise a ValueError
        ipaddress.ip_network(cidr_block)
        return True
    except ValueError:
        return False

def write_ips_to_file(cidr_blocks, output_path):
    with open(output_path, 'w') as out_file:
        for ip_range in cidr_blocks:
            network = ipaddress.ip_network(ip_range)
            for ip in network.hosts():  # Use hosts() to skip network and broadcast addresses
                out_file.write(str(ip) + '\n')


if __name__ == "__main__":

    # Zombies path must contain an IP address of zombie per line
    if len(sys.argv) != 4:
        print("[!] Usage: python3 splitting.py <zombies_path> <IP_ranges_path> <output_ips_path>")
        sys.exit(0)

    # Receives valid paths
    zombie_path = sys.argv[1]
    ip_ranges_path = sys.argv[2]
    output_path = sys.argv[3]
    if os.path.exists(zombie_path) is False or os.path.exists(ip_ranges_path) is False: 
        print(f"[!] Some path doesn't exist")
        sys.exit(0)

    # Validate the provided ip_ranges are valid CIDR blocks
    hosts_count = 0
    valid_cidr_blocks = []
    with open(ip_ranges_path, 'r') as file:
        for ip_range in file:
            ip_range = ip_range.rstrip("\n")
            if not validate_cidr_block(ip_range):
                print(f"[!] Error: '{ip_range}' is not a valid CIDR block.")
            else:
                valid_cidr_blocks.append(ip_range)
                hosts_count += ipaddress.ip_network(ip_range).num_addresses - 2

    # Write IP addresses to the output file
    write_ips_to_file(valid_cidr_blocks, output_path)

    print(f"[1] Total Hosts in the IP ranges listed:\n\t[{hosts_count}]")
    print(f"[2] All IPs have been written to:\n\t'{output_path}'.")

    # Calculate number of zombies
    zombies = 0
    with open(zombie_path, 'r') as file:
        for line in file:
            zombies += 1
    print(f"\n[3] Total Zombies:\n\t[{zombies}]")

    ips_per_zombie = round(hosts_count / zombies, 2)
    print(f"\n[4] Total Hosts per Zombie:\n\t[{ips_per_zombie}]")


    #split_file(zombie_path, number_parts)
