# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 21:09:14 2014

@author: wyh
"""

from socket import *
                
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
# 创建 socket通信
tcpCliSock = socket(AF_INET, SOCK_STREAM)
# 创建连接
tcpCliSock.connect(ADDR)
# 客户端通信循环
while True:
    # 接受服务器传的数据
    data = tcpCliSock.recv(BUFSIZ)
  
    print data
                
tcpCliSock.close()