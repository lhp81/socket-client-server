"""
An attempt to write a client that can send user input to my server.

In writing this I looked at:
http://www.devshed.com/c/a/Python/Sockets-in-Python-Into-the-World-of-
    Python-Network-Programming/2/
http://ilab.cs.byu.edu/python/socket/echoserver.html
http://ilab.cs.byu.edu/python/socket/echoclient.html
http://cewing.github.io/training.codefellows/assignments/day06/
    socket_exercise.html
"""

import socket

def run_client():
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)
    client_socket.connect(('127.0.0.1', 50000))
    send_message()

    while True:
        conn, addr = server_socket.accept()
        message_part = connection.recv(4096)
        if len(message_part) < 4096:    #if you got the whole msg...
            socket.close()
            return message_part



def send_message():
    message = raw_input("What message would you like to send? > ")
    client_socket.sendall(message)
    client_socket.shutdown(socket.SHUT_WR)

if __name__ == '__main__':
    run_client()