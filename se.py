# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 21:03:52 2014

@author: wyh
"""

#!/usr/bin/env python
                     
from socket import *
from time import ctime
                     
HOST   = ''
PORT   = 21567
BUFSIZ = 1024
ADDR   = (HOST, PORT)
                     
# 创建socket
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# 绑定地址
tcpSerSock.bind(ADDR)
# 监听链接
tcpSerSock.listen(5)
                     
# 服务器无限循环等待
while True:
    print 'waiting for connection...'
    # 接受客户端请求，并生成一个专门处理客户端的对象
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr
    # 通信循环
    while True:
        # 接受处理客户端发送的数据
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))
                     
    tcpCliSock.close()
tcpSerSock.close()