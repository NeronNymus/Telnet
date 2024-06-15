#!/usr/bin/env python3

import socket


def tcp_client():
    target_host = "www.google.com"
    target_port = 80

    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the client
    client.connect((target_host, target_port))

    # Send some data
    request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
    client.send(request.encode())

    # Receive some data
    response = client.recv(4096)

    print(response)

if __name__ == "__main__":
    tcp_client()
