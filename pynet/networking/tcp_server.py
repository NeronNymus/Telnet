#!/usr/bin/env python3

import socket
import threading


def tcp_server():
    bind_ip = "0.0.0.0"
    bind_port = 9999

    # Declare a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((bind_ip, bind_port))

    server.listen(5)

    print("[*] Listening on %s:%d" % (bind_ip, bind_port))

    while True: 
        client, addr = server.accept()

        print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

        # Spin up our client thread to handle incoming data 
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


# This is our client-handling thread
def handle_client(client_socket):

    # Print out what the client sends
    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)

    # Send back a packet
    client_socket.send("ACK!")

    client_socket.close()


if __name__ == "__main__":
    tcp_server()

