#! /usr/bin/env python
# coding=utf-8
__author__ = 'Marco'

from SocketServer import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from time import ctime,sleep

HOST = ''
PORT = 12346
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print self
        print '...connected from:', self.client_address

        recv = self.rfile.readline().strip()
        btuple = recv.split(';')
        if btuple[0] == '1001':
            self.wfile.write('%s\r\n' % self.handle1001(btuple[1]))
        elif btuple[0] == '1002':
            self.wfile.write('%s\r\n' % self.handle1002(btuple[1]))
        elif btuple[0] == '1003':
            self.wfile.write('%s\r\n' % self.handle1003(btuple[1]))
        else:
            print 'Unknown cmd: %s' % recv
            #self.wfile.write('[%s] %s\r\n' % (ctime(), recv))

    def handle1001(self, param_line):
        btuple = param_line.split(',')
        print '1001 params:%s' % param_line
        return '2001;0,1'

    def handle1002(self, param_line):
        btuple = param_line.split(',')
        print '1002 params:%s' % param_line
        return '2002;%s,register_tester,progressing,NA,NA' % btuple[0]

    def handle1003(self, param_line):
        btuple = param_line.split(',')
        print '1003 params:%s' % param_line
        return '2003;%s;calling,10000;called,57575777' % btuple[0]

tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
