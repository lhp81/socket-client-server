import unittest
import socket
from server import start_server
from client import run_client


class ServerClientTest(unittest.TestCase):
    """
    Testing my server's ability to receive a message.
    """

    def test_recieve_short_message(self):
        test_message = 'pwn on you n00b'
        self.assertEqual(test_message, run_client('pwn on you n00b'))


    def test_receive_long_message(self):
        pass

if __name__ == '__main__':
    unittest.main()
