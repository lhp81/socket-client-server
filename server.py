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

    while True:
        response = 'you said: '
        conn, addr = server_socket.accept()
        message_part = connection.recv(4096)
        if len(message_part) < 4096:    #if you got the whole msg...
            socket.close()
        response += message_part        #add msg to my response tag
        connection.sendall(response)    #and send it out.

    conn.shutdown(socket.SHUT_WR)
    conn.close()
    server_socket.close()


if __name__ == '__main__':
    start_server()