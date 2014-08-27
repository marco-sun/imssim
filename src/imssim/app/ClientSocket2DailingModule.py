#! /usr/bin/env python
# coding=utf-8
__author__ = 'Marco'

import os
from socket import *

HOST = 'localhost'
PORT = 12346
conf_file = open(os.path.dirname(os.path.dirname(__file__))+"/config.ini")
for line in conf_file:
    tuple_conf = line.strip('\n').strip('\r').split("=")
    if len(tuple_conf) == 2:
        if tuple_conf[0] == "term_host":
            HOST = tuple_conf[1]
        elif tuple_conf[0] == "term_port":
            PORT = tuple_conf[1]
conf_file.close()
print 'LOAD TERM INFO: %s,%s' % (HOST, PORT)
BUFSIZE = 10240
ADDR = (HOST, PORT)


def querydm(msg):
    """向拨测底层发送消息并等待结果（阻塞模式）
    """
    print 'Sending msg [%s]' % msg
    data = ''
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
    ret = data.strip()
    print 'RECV msg <%s>' % ret
    return ret


def test():
    recv = querydm("")
    if recv:
        print "recv: [%s]" % recv

if __name__ == '__main__':
    test()