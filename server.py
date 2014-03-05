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
        socket.SOCK_STREAM,         # type of socket
        socket.IPPROTO_TCP)         # make it a tcp connection
    address = ('127.0.0.1', 50000)  # the ip and port
    server_socket.bind(address)     # give the server ip/port frm above
    server_socket.listen(5)         # 'backlog' of 5
    conn, addr = server_socket.accept()  # accept connections.

    listen = True                   # start a listening loop.
    while listen:
        message = ''
        message += conn.recv(4096)
        if len(message) < 4096:     # this is so it can accept messages that
            listen = False                      # are longer than the buffer.

    print message                   # so it shows us the message and then sends
    conn.sendall(message)           # the same message back to the client.



if __name__ == '__main__':
    start_server()
