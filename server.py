"""
An attempt to write a server that can receive messages.

In writing this I looked at:
http://www.devshed.com/c/a/Python/Sockets-in-Python-Into-the-World-of-
    Python-Network-Programming/2/
http://ilab.cs.byu.edu/python/socket/echoserver.html
http://ilab.cs.byu.edu/python/socket/echoclient.html
http://cewing.github.io/training.codefellows/assignments/day06/
    socket_exercise.html
"""

import socket

def start_server():
    server_socket = socket.socket(  # create a server...
        socket.AF_INET,             # type of address
        socket.SOCK_STREAM,         # asdf
        socket.IPPROTO_TCP)         # make it a tcp connection
    address = ('127.0.0.1', 50000)
    server_socket.bind(address)     #give the server ip/port frm above
    server_socket.listen(5)         #'backlog' of 5
    conn, addr = server_socket.accept()

    listen = True
    while listen:
        message = conn.recv(4096)
        print message
        conn.sendall(message)          #and send it out.
        listen = False

    conn.shutdown(socket.SHUT_WR)
    conn.close()
    server_socket.close()


if __name__ == '__main__':
    start_server()