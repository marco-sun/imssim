#! /usr/bin/env python
# coding=utf-8
__author__ = 'Marco'

from socket import *

HOST = 'localhost'
PORT = 12346
BUFSIZE = 10240
ADDR = (HOST, PORT)


def querydm(msg):
    """向拨测底层发送消息并等待结果（阻塞模式）
    """
    data = None
    try:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        tcpCliSock.send('%s\r\n' % msg)
        data = tcpCliSock.recv(BUFSIZE)
        if data:
            print data.strip()
        tcpCliSock.close()
    except Exception, e:
        # (errno, err_msg) = arg
        # print "Connect server failed: %s, errno=%d" % (err_msg, errno)
        print "Connect server failed: %s" % e
    return data.strip()


def test():
    recv = querydm("")
    if recv:
        print "recv: [%s]" % recv

if __name__ == '__main__':
    test()