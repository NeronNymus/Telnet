#!/usr/bin/env python3

import socket

def udp_server():
    target_host = "127.0.0.1"
    target_port = 80

    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the address and port
    server.bind((target_host, target_port))

    print("UDP server up and listening")

    while True:
        # Receive some data
        data, addr = server.recvfrom(4096)
        print(f"Received message: {data.decode()} from {addr}")

        # Send a response
        server.sendto("Hello UDP Client".encode(), addr)

if __name__ == "__main__":
    udp_server()

