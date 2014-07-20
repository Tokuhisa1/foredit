# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 22:22:22 2014

@author: wyh
"""

#!/usr/bin/python

from socket import *
from time import ctime
import sys

bufsize = 1024

host = sys.argv[1]
port = int(sys.argv[2])
addr = (host,port)

client_sock = socket(AF_INET,SOCK_STREAM)
client_sock.connect(addr)

while True:
	data = raw_input(">")
	if not data:
		break
	else:
		client_sock.send(data)
		data = client_sock.recv(bufsize)
		print '%s\n%s' %(ctime(),data)

client_sock.close()