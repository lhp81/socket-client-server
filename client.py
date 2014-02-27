"""
An attempt to write a client that can send user input to my server.
"""

import socket
import sys


def run_client(message):
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)
    client_socket.connect(('127.0.0.1', 50000))
    client_socket.sendall(message)
    msg_back = client_socket.recv(4096)
    print 'Response received: %s' % msg_back
    client_socket.shutdown(socket.SHUT_WR)


if __name__ == '__main__':
    message = sys.argv[1]
    print 'Sending message: %s' % message
    run_client()
