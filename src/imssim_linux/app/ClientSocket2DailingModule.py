#! /usr/bin/env python
# coding=utf-8
__author__ = 'Marco'

from gdm import Gdm
from socket import *

BUFSIZE = 10240


def querydm(msg, workerid):
    """向拨测底层发送消息并等待结果（阻塞模式）
    """
    gdm = Gdm()
    addr = (gdm.uac_ip, gdm.dm_baseport+int(workerid))
    print 'To worker%s(%s,%d) Sending msg [%s]' % (workerid, gdm.uac_ip, gdm.dm_baseport+int(workerid), msg)
    data = ''
    try:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(addr)
        tcpCliSock.send('%s\n' % msg)
        data = tcpCliSock.recv(BUFSIZE)
        if data:
            print data.strip()
        tcpCliSock.close()
    except Exception, e:
        print "Connect server failed: %s" % e
    ret = data.strip()
    print 'RECV msg <%s>' % ret
    return ret


def test():
    recv = querydm("",'1')
    if recv:
        print "recv: [%s]" % recv

if __name__ == '__main__':
    test()