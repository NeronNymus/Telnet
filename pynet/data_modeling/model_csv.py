#/usr/bin/env python3

# This is a script for modeling and analyzing data from the telnet sessions.

import sys
import csv


cont = 0

if __name__ == "__main__":
    # First, check that the file argument is provided
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <csv_file>")
        sys.exit(1)
        
    # Receive the arguments
    script_path = sys.argv[0]
    csv_file = sys.argv[1]

    # Initialize two lists to collect integers from the CSV
    number_host_list = []
    differences_list = []


    # Open the CSV file and read it
    try:
        with open(csv_file, 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                line = line.split(',')
                number_hosts = line[0]
                difference = line[1]

                # Append to both lists
                number_host_list.append(number_hosts)
                differences_list.append(difference)

                cont += 1



    except Exception as e:
        print(f"An error occurred: {e}")

    # Print the collected lists
    #print("[!] Number of hosts:\n", number_host_list)
    #print("[!] Differences:\n", differences_list)

    # The average of the list
    sum_differences = 0

    for difference in differences_list:
        sum_differences += int(difference)
        #print(difference)

    # Analysis
    seconds = 5
    average = sum_differences / len(differences_list)
    average = round(average, 2)
    average_per_second = round(average / seconds, 2)

    login_hosts = number_host_list.pop()    # Last's row number
    total_time_seconds = 5 * len(differences_list)  # Each time was 5 seconds of interval
    total_time_minutes = round(total_time_seconds / 60, 2)
    total_time_hours = round(total_time_minutes / 60, 2)

    # Determine the total numbers of hosts to try the logins
    number = 55
    hardcoded_path = f"/mnt/Kali/home/grimaldi/Bash/Telnet/scans/crawling/ips_up_port_23_10.0.0.0_8/ips_up_port_23_10.0.0.0_8.{number}.clean"
    with open(hardcoded_path, 'r') as file:
        total_hosts = sum(1 for line in file)

    expected_time_seconds = round(total_hosts/ average_per_second, 2)
    expected_time_minutes = round(expected_time_seconds / 60, 2)
    expected_time_hours = round(expected_time_minutes / 60, 2)
    expected_time_days = round(expected_time_hours / 24, 2)




    print("------ Report --------")
    print(f"[!] Total Lines of the CSV:\n\t[{cont}]\n")
    print(f"[1] Login Hosts:\n\t[{login_hosts}]\n")
    print(f"[2] Total Time Trying to login:\n\t[{total_time_seconds} sec]\n\t[{total_time_minutes} min]\n\t[{total_time_hours} hrs]\n")
    print(f"[3] {average} hosts every {seconds} seconds\n\t[{average}/{seconds}s]\n")
    print(f"[4] {average_per_second} hosts every second\n\t[{average_per_second}/1s]\n")
    print(f"[5] Total Hosts:\n\t[{total_hosts}]\n")
    print(f"[6] Expected time to try login on all the hosts:\n\t[{expected_time_seconds} sec]\n\t[{expected_time_minutes} min]\n\t[{expected_time_hours} hrs]\n\t[{expected_time_days} days]\n")
