#!/usr/bin/env python3

import sys
import signal
import socket

# Global variable to track client sockets
client_sockets = []

# Signal handler function to catch Ctrl+C
def signal_handler(sig, frame):
    print("\n\n[!] Exiting gracefully...")

    # Close all open client sockets
    for client_socket in client_sockets:
        client_socket.close()

    sys.exit(0)

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)


def tcp_client(target_host, target_port, local_host, local_port):

    # Create a socket object
    #                               ipv4            TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to a specific local port (optional)
    client.bind((local_host, 0)) # Random port selected

    # Connect to the client
    client.connect((target_host, target_port))
    print(f"[!] Connection established [{target_host}:{target_port}]")

    # Add it to the list of client_sockets
    client_sockets.append(client_sockets)

    instructions = ""
    while True:

        # Press ctrl+D is needed first to begin a correct iteration
        instructions = str(sys.stdin.read())

        if instructions == "exit":
            break

        instructions += "\n"

        instructions = instructions.encode()
        client.sendall(instructions)

        print("\n[!] Data sended to proxy.")


if __name__ == "__main__":

    # Simple command-line parsing here
    if len(sys.argv[1:]) != 2:
        print("Usage: ./proxy_client.py [target_host] [target_port]")
        print("Example:\n./proxy_client.py 127.0.0.1 2323")
        sys.exit(0)

    target_host = sys.argv[1]
    target_port = int(sys.argv[2])
    local_host = target_host
    local_port = 1234

    tcp_client(target_host, target_port, local_host, local_port)





