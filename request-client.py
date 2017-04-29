import socket
import os
import sys

i = ''
p = sys.argv[1]
ip = str(i)
port = int(p)
bf = 77777
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pt = "=>> "
action = 'ok'
message = 'Press "q" to quit else any to continue: '
s.sendto('Hello',(ip,port))
data, server = s.recvfrom(bf)
print data

while action!='q':
	print message
	action = raw_input(pt)
	s.sendto(action,(ip,port))
	action, server = s.recvfrom(bf)
	print action

s.close()