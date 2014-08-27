#! /usr/bin/env python
# coding=utf-8
__author__ = 'Marco'

from flask import json
from util import convert_to_builtin_type
import os

import ClientSocket2DailingModule as csdm

class Calling:

    def __init__(self):
        self.session_no = '0'
        self.progress = 'NA'
        self.status = 'NA'
        self.result = 'NA'
        self.reason = '0'

    def doCalling(self, called_party, timeout, gateway_ip, gateway_port, account, password):
        #1001;called_party,timeout,gateway_ip,gateway_port,account,password
        msg = "1001;%s,%s,%s,%s,+8621%s,%s" % (called_party, timeout, gateway_ip, gateway_port, account, password)
        rslt = csdm.querydm(msg)
        # 2001;status,result_code
        if rslt:
            rslt_tuple = rslt.split(';')[1].split(',')
            self.status = rslt_tuple[0]
            if self.status == '1':
                self.session_no = rslt_tuple[1]
            else:
                self.reason = rslt_tuple[1]
        else:
            self.status = "0"
            self.reason = "500"

    def doQueryCalling(self,session_no):
        msg = "1002;%s" % session_no
        self.session_no = session_no
        rslt = csdm.querydm(msg)
        # 2002;session_no,progress,status,result,reason
        if rslt:
            rslt_tuple = rslt.split(';')[1].split(',')
            self.progress = rslt_tuple[1]
            self.status = rslt_tuple[2]
            self.result = rslt_tuple[3]
            self.reason = rslt_tuple[4]
        else:
            self.status = "0"
            self.reason = "500"


# 必选参数 called_party, 其他参数若空则从配置文件中获取
def getCalling(called_party, timeout, gateway_ip, gateway_port, account, password):

    c = Calling()
    # step1 参数检查
    if called_party == '':
        c.status = '0'
        c.reason = 'Param called_party must be set.'
        s = json.dumps(c, default=convert_to_builtin_type, ensure_ascii=False)
        return s

    # step2 默认参数补齐
    def_timeout = '120'
    def_gateway_ip = '127.0.0.1'
    def_gateway_port = '5060'
    def_account = 'default@localhost'
    def_password = 'default_password'
    conf_file = open(os.path.dirname(os.path.dirname(__file__))+"/config.ini")
    for line in conf_file:
        tuple_conf = line.strip('\n').strip('\r').split("=")
        if len(tuple_conf) == 2:
            if tuple_conf[0] == "timeout":
                def_timeout = tuple_conf[1]
            elif tuple_conf[0] == "gateway_ip":
                def_gateway_ip = tuple_conf[1]
            elif tuple_conf[0] == "gateway_port":
                def_gateway_port = tuple_conf[1]
            elif tuple_conf[0] == "account":
                def_account = tuple_conf[1]
            elif tuple_conf[0] == "password":
                def_password = tuple_conf[1]
    conf_file.close()
    if timeout == '':
        timeout = def_timeout
    if gateway_ip == '':
        gateway_ip = def_gateway_ip
    if gateway_port == '':
        gateway_port = def_gateway_port
    if account == '':
        account = def_account
    if password == '':
        password = def_password

    # step3 执行
    c.doCalling(called_party, timeout, gateway_ip, gateway_port, account, password)

    # step4 将calling对象作为结果对象以json格式返回
    s = json.dumps(c, default=convert_to_builtin_type, ensure_ascii=False)
    return s

def getQueryCalling(session_no):
    c = Calling()
    # step1 参数检查
    if session_no == '':
        c.status = '0'
        c.reason = 'Param session_no must be set.'
        s = json.dumps(c, default=convert_to_builtin_type, ensure_ascii=False)
        return s

    c.doQueryCalling(session_no)
    s = json.dumps(c, default=convert_to_builtin_type, ensure_ascii=False)
    return s
