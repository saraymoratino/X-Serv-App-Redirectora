#!/usr/bin/python

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

try:
	while True:
		print 'Waiting for connections'
		(recvSocket, address) = mySocket.accept()
		print 'HTTP request received:'
		request = recvSocket.recv(2048)
		print 'Answering back...'
		num = random.randint (0,9999999)
		url = "http://localhost:1234"
		print recvSocket.send("HTTP/1.1 302 Found \r\n\r\n" "<html><body>" +
		'<meta http-equiv="refresh" content="0;url= url" />' +
		"</body><html>"+ "\r\n")    
		recvSocket.close()

except KeyboardInterrupt:
	print "Closing binded socket"
	mySocket.close()
            
            
          
		
            
