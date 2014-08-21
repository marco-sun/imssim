#! /usr/bin/env python
# coding=utf-8
__author__ = 'Marco'

import socket
from socket import *

HOST = 'localhost'
PORT = 12346
BUFSIZE = 1024
ADDR = (HOST, PORT)

def test1():
    while True:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        data = raw_input('>')
        if not data:
            break
        tcpCliSock.send('%s\r\n' % data)
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print data.strip()
        tcpCliSock.close()


def test2():
    try:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        data = "This is test2."
        tcpCliSock.send('%s\r\n' % data)
        data = tcpCliSock.recv(BUFSIZE)
        if data:
            print data.strip()
        tcpCliSock.close()
    except Exception, e:
        # (errno, err_msg) = arg
        # print "Connect server failed: %s, errno=%d" % (err_msg, errno)
        print "Connect server failed: %s" % e


def test3():
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = "This is test2."
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZE)
    if data:
        print data.strip()
    tcpCliSock.close()


if __name__ == '__main__':
    test2()
