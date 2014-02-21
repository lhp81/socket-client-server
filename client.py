"""
An attempt to write a client that can send user input to my server.

"""

import socket

def run_client():
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)
    client_socket.connect(('127.0.0.1', 50000))
    message = raw_input("What message would you like to send? > ")
    client_socket.sendall(message)
    msg_back = client_socket.recv(4096)
    print msg_back
    client_socket.shutdown(socket.SHUT_WR)


if __name__ == '__main__':
    run_client()