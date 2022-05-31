# import socket programming library
import socket

# import thread module
from threading import Thread

#inport date module
from datetime import datetime

def main():
    # reverse a port on your computer
	# can be anything
	port = 10048
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print("socket binded to port", port)

	# put the socket into listening mode
	s.listen(5)
	print("socket is listening")


	# establish connection with client
	c, addr = s.accept()

	print('Connected to :', addr[0], ':', addr[1])


if __name__ == '__main__':
	Main()
