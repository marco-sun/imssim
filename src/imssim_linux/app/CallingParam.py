#! /usr/bin/env python
# coding=utf-8

from flask import json
from util import convert_to_builtin_type

import ClientSocket2DailingModule as csdm

class CallingParam:
    param_name = ''
    param_value = ''

    def doCallingParam(self,param_name,param_value):
        self.param_name = param_name
        self.param_value = param_value


def getCallingParam(session_no):
    inner_sid = session_no[2:]
    worker_id = session_no[:2]
    msg = "1003;%s" % inner_sid
    rslt = csdm.querydm(msg, worker_id)
    if rslt:
        # 2003;session_no;param1,val1;param2,val2;param3,val3;…
        rslt_tuple = rslt.split(';')[2:]
        cps = []
        for user_para in rslt_tuple:
            para_info = user_para.split(',')
            cp = CallingParam()
            cp.doCallingParam(para_info[0],para_info[1])
            cps.append(cp)
        l = {'session_no': session_no, 'params': cps}
    else:
        l = {'session_no': session_no}
    #cpa = CallingParam()
    #cpa.doCallingParam('CallingNum','999')
    #cpb = CallingParam()
    #cpb.doCallingParam('CallingNum','555')
    #l = {'session_no':session_no,'params':[cpa,cpb]}
    s = json.dumps(l, default=convert_to_builtin_type, ensure_ascii=False)
    return s
