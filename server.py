from socket import *
import sys
import os
import thread

ip = ''
port = sys.argv[1]
ip = str(ip)
port = int(port)
bf = 77777
message = "Please enter you query"
base = os.getcwd()
client_list = []
print "*****Server: Welcome to the CS 382 Search Engine*****"
s = socket(AF_INET, SOCK_DGRAM)
s.bind((ip, port))
print 'The server is ready to receive'
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def main():
	def multThread(c):
		while True:
			s.sendto('Connected to Server', c)
			data,c = s.recvfrom(bf)
			print data
			s.sendto(data, c)

	while True:
		data, conn = s.recvfrom(bf)
		client_list.append(conn)
		c = client_list[-1]
		print data
		thread.start_new_thread(multThread,(c,))

if __name__ == "__main__":
	main()