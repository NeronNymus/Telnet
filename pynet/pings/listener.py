#!/usr/bin/env python3

import os
import logging
from scapy.all import *
from datetime import datetime
import random

counter = 1
spoofed_ip = f"10.170.51.5"

# Set up logging to a file
logging.basicConfig(filename='ping_logs.txt', level=logging.INFO,
                    format='%(message)s')

def packet_callback(packet):
    global counter
    global spoofed_ip
    if ICMP in packet and packet[ICMP].type == 8:  # ICMP Echo Request
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current timestamp
        print(f"[{counter}] [{timestamp}] Ping request send from {src_ip} to {dst_ip} (Spoofed from {spoofed_ip})")
        logging.info(f"[{counter}] [{timestamp}] Ping request send from {src_ip} to {dst_ip} (Spoofed from {spoofed_ip})")
        counter += 1

def start_sniffing(interface):
    global spoofed_ip
    print(f"[*] Starting listener on IP address {interface}...")
    print(f"[*] Spoofing IP: {spoofed_ip}")
    print("[!] Listening for incoming ICMP Echo Requests.")
    sniff(filter="icmp and icmp[0] == 8", prn=packet_callback, store=0, iface=interface)

# Call start_sniffing() when this module is executed directly
if __name__ == "__main__":

    # Clear the terminal
    os.system('clear')
    
    try:
        interface = "eth0"  
        start_sniffing(interface)
    except Exception as e:
        print(f"Error occurred: {e}")

