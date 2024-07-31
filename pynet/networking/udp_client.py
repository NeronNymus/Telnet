#!/usr/bin/env python3

import socket
import time

def udp_client():
    target_host = "127.0.0.1"
    target_port = 80

    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send some data
    client.sendto("AAABBBCCC".encode(), (target_host, target_port))

    # Receive some data
    data, addr = client.recvfrom(4096)

    print(data)


if __name__ == "__main__":
    while True:
        udp_client()
        time.sleep(1)
