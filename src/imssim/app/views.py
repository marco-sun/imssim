# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import render_template,request,json
from app import app

from Calling import getCalling,getQueryCalling
from CallingParam import getCallingParam

##@app.route('/')
##def index():
##    return render_template("a.html")

@app.route('/calling',methods=['GET'])
def calling():
    reqtype = request.args.get('cmd_type', '')
    if reqtype == 'querycalling':
        # 查询测试进度
        session_no = request.args.get('session_no', '')
        ret = getQueryCalling(session_no)
    elif reqtype == 'calling':
        # 发起测试
        called_party = request.args.get('called_party', '')
        timeout = request.args.get('timeout', '')
        gateway_ip = request.args.get('gateway_ip', '')
        gateway_port = request.args.get('gateway_port', '')
        account = request.args.get('account', '')
        password = request.args.get('password', '')
        ret = getCalling(called_party,timeout,gateway_ip,gateway_port,account,password)
    return ret

@app.route('/params',methods=['GET'])
def params():
    reqtype = request.args.get('cmd_type', '')
    if reqtype == 'params':
        # 请求详细参数
        session_no = request.args.get('session_no', '')
        ret = getCallingParam(session_no)
    return ret

@app.route('/processes',methods=['GET'])
def processes():
    reqtype = request.args.get('type', '')
    ret = 'under construction'
    return ret
