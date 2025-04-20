#!/usr/bin/env python3

# This script is to perform database connections to different sources
# for analyzing the backend data.

import sys
import argparse

# Import personal packages
from utils.colors import Colors
from backend.backend import conn_simple, query

# Pass environment variables
from dotenv import load_dotenv



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
    print("python3 pynet_analysis.py -a 1\t\t(Perform first analysis on backend)")
    print("python3 pynet_analysis.py -e\t\t(Show this examples message)")
    print("python3 pynet_analysis.py -h\t\t(Show help message)")
    sys.exit(0)


# Perform analysis with custom query
def analysis1():
    # Load environment variables from .env file
    load_dotenv(".env")

    # Create connection
    conn = conn_simple()

    sql_query1 = """
    SELECT DISTINCT mac_vendor
    FROM wap_devices_live;
    """
    results1 = query(conn, sql_query1)

    sql_query2 = """
    SELECT DISTINCT mac_vendor
    FROM wap_devices_live;
    """
    results2 = query(conn, sql_query2)

    # Join results
    all_results = results1 + results2

    cont = 1
    for result in all_results:
        print(result)
        cont+=1

    print(f"[!] Total registries:\t{cont}")

    if conn:
        print(Colors.GREEN + "[*] Connection to database closed successfully" + Colors.R)
        conn.close()



def analysis2():
    # Create connection
    conn = conn_simple(".env2")

    sql_query1 = """
    SELECT DISTINCT mac_address
    FROM scan_results;
    """
    results1 = query(conn, sql_query1)

    sql_query2 = """
    SELECT DISTINCT mac_address
    FROM mac_aliases;
    """
    results2 = query(conn, sql_query2)

    results1 += results2

    # Create connection
    conn = conn_simple(".env")

    sql_query3 = """
    SELECT parent_ipv4_address, child_id, child_ipv4_address, mac_vendor, mac_address
    FROM wap_devices
    LIMIT 100;
    """
    results3 = query(conn, sql_query3)


    cont = 1
    for result in results3:
        print(result[0])
        cont+=1

    print(Colors.BOLD_WHITE + f"[!] Total registries:\t{cont}" + Colors.R)

    if conn:
        print(Colors.GREEN + "[*] Connection to database closed successfully" + Colors.R)
        conn.close()


# This methods tries to find matches with known SSID from ocr results
def analysis3():
    known_ssids = "/mnt/Kali/home/grimaldi/Bash/Telnet/analysis/SSID/point_SSID"
    
    ssids_list = []
    with open(known_ssids, 'r') as file:
        for ssid in file:
            ssid = ssid.rstrip()
            ssids_list.append(ssid)

    # Ensure the list is non-empty
    if not ssids_list:
        print("No SSIDs found in the file.")
        return []

    # Sanitize and format SSIDs for SQL
    sanitized_ssids = [f"'{ssid.replace('\'', '\'\'')}'" for ssid in ssids_list]
    ssids_condition = ", ".join(sanitized_ssids)

    sql_query = f"""
        SELECT *
        FROM wifi_ssid_info
        WHERE ssid_name IN ({ssids_condition});
    """

    # Create connection
    conn = conn_simple(".env")

    # Execute the query
    results = query(conn, sql_query)
    
    # Process results
    print(Colors.GREEN + "Matching SSIDs with Details:" + Colors.R)
    for row in results:
        print(row)

    return results


if __name__ == "__main__":

    # Parse command-line arguments
    args = parse_arguments()

    if args.examples:
        show_examples()

    elif args.analysis:


        if args.analysis == 1:
            analysis1()

        elif args.analysis == 2:
            analysis2()

        elif args.analysis == 3:
            analysis3()

