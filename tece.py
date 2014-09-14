# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 22:49:51 2014

@author: wyh
"""

from socket import *
from time import ctime
import sys

bufsize = 1024

host = sys.argv[1]
port = int(sys.argv[2])
addr = (host,port)

client_sock = socket(AF_INET,SOCK_STREAM)
client_sock.connect(addr)
