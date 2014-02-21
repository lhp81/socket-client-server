There are two files: server.py and client.py.

The two files are meant to complement each other. The server listens to the client, prints the message received from it, and sends a response.
After the _server_ **sends** out a response, which is the same text as the message sent, it shuts down.
After the _client_ **receives** the response, it shuts down.

In addition to the Python documents, the following sources were consulted in the creation of these scripts:

http://www.devshed.com/c/a/Python/Sockets-in-Python-Into-the-World-of-Python-Network-Programming/2/

http://ilab.cs.byu.edu/python/socket/echoserver.html

http://ilab.cs.byu.edu/python/socket/echoclient.html

http://cewing.github.io/training.codefellows/assignments/day06/socket_exercise.html