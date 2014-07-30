#! /usr/bin/env python
# coding=utf-8
__author__ = 'Marco'

from flask import json
from util import convert_to_builtin_type

import ClientSocket2DailingModule as csdm

class Calling:
    session_no = ''
    progress = ''
    status = ''
    result = ''
    reason = ''

    def doCalling(self, called_party, timeout, gateway_ip, gateway_port, account, password):
        #1001;called_party,timeout,gateway_ip,gateway_port,account,password
        msg = "1001;%s,%s,%s,%s,%s,%s" % (called_party, timeout, gateway_ip, gateway_port, account, password)
        rslt = csdm.querydm(msg)
        # 2001;status,result_code
        if rslt:
            rslt_tuple = rslt.split(';')[1].split(',')
            self.status = rslt_tuple[0]
            self.session_no = rslt_tuple[1]
        else:
            self.status = "N/A"
            self.session_no = "0"

    def doQueryCalling(self,session_no,progress,status,result,reason):
        msg = "1002;%s" % session_no
        self.session_no = session_no
        rslt = csdm.querydm(msg)
        # 2002;session_no,progress,status,result,reason
        if rslt:
            rslt_tuple = rslt.split(';')[1].split(',')
            self.progress = rslt_tuple[0]
            self.status = rslt_tuple[1]
            self.result = rslt_tuple[2]
            self.reason = rslt_tuple[3]
        else:
            self.progress = progress
            self.status = status
            self.result = result
            self.reason = reason


def getCalling(called_party,timeout,gateway_ip,gateway_port,account,password):
    c = Calling()
    c.doCalling(called_party,timeout,gateway_ip,gateway_port,account,password)

    s = json.dumps(c, default=convert_to_builtin_type, ensure_ascii=False)
    return s

def getQueryCalling(session_no):
    c = Calling()
    c.doQueryCalling(session_no,'N/A','N/A','INTERNAL ERROR','500')
    s = json.dumps(c, default=convert_to_builtin_type, ensure_ascii=False)
    return s
