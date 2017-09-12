#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *
from time import ctime

HOST = ''#bind（）方法的标识，表示可以使用任何可用的地址
PORT = 21567#随机的端口号
BUFSIZ = 1024#缓冲区的大小设置为1KB
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)#分配TCP服务器套接字
tcpSerSock.bind(ADDR)#将地址（主机号，端口号对）绑定在套接字上
tcpSerSock.listen(5)#设置并启动TCP监听器

while True:
    print 'Waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()#被动接受TCP客户端连接，一直等待直到连接到达（阻塞）
    print'...connected from:', addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:#if not data：表示if data == 0
            break
        tcpCliSock.send('[%s] %s' %(ctime(), data))

    tcpCliSock.close()
tcpSerSock.close()
