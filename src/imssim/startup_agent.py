# coding=utf-8
__author__ = 'Marco'

import time
import win32api, win32con
import win32pdh
import atexit
import traceback
import sys


# ***********************************************************************
# ***********************************************************************
def GetAllProcesses():
    object = "Process"
    items, instances = win32pdh.EnumObjectItems(None,None,object, win32pdh.PERF_DETAIL_WIZARD)
    return instances
# ***********************************************************************


# ***********************************************************************
# ***********************************************************************
def GetAllTargetProcesses(pname):
    ret = []
    object = "Process"
    items, instances = win32pdh.EnumObjectItems(None,None,object, win32pdh.PERF_DETAIL_WIZARD)
    temp = list(instances)
    while pname in temp:
        temp.remove(pname)
        ret.append(pname)
    return ret
# ***********************************************************************


# ***********************************************************************
# ***********************************************************************
def GetProcessID( name ):
    object = "Process"
    items, instances = win32pdh.EnumObjectItems(None,None,object, win32pdh.PERF_DETAIL_WIZARD)
    val = None
    if name in instances :
        hq = win32pdh.OpenQuery()
        hcs = []
        item = "ID Process"
        path = win32pdh.MakeCounterPath( (None,object,name, None, 0, item) )
        hcs.append(win32pdh.AddCounter(hq, path))
        win32pdh.CollectQueryData(hq)
        time.sleep(0.01)
        win32pdh.CollectQueryData(hq)
        for hc in hcs:
            type, val = win32pdh.GetFormattedCounterValue(hc, win32pdh.PDH_FMT_LONG)
            win32pdh.RemoveCounter(hc)
            win32pdh.CloseQuery(hq)
            return val
# ***********************************************************************


'''
#THIS IS SLOW !!
def Kill_Process ( process ) :
    #get process id's for the given process name
    pids = win32pdhutil.FindPerformanceAttributesByName ( process )
    for p in pids:
        handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, p) #get process handle
    win32api.TerminateProcess(handle,0) #kill by handle
    win32api.CloseHandle(handle) #close api
'''

# ***********************************************************************
# ***********************************************************************
def Kill_Process_pid(pid) :
    handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, pid) #get process handle
    win32api.TerminateProcess(handle,0) #kill by handle
    win32api.CloseHandle(handle) #close api
    # ***********************************************************************


# ***********************************************************************
# ***********************************************************************
def Kill_Process ( name ) :
    pid = GetProcessID (name)
    print pid
    if pid:
        print "exist"
        Kill_Process_pid(pid)
        return True
    else:
        print "not this proccess"
        return False
# ***********************************************************************

def close_agents():
    process = 'winsockserver'# process name
    a = GetAllTargetProcesses(process)
    print a
    for useless in a:
        time.sleep(0.5)
        Kill_Process(process)

@atexit.register
def atexit_fun():
    close_agents()
    print 'i am exit, stack track:'
    exc_type, exc_value, exc_tb = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_tb)


def init_agents_ex(us_count, ts_count):
    process = 'winsockserver'# process name
    a = GetAllTargetProcesses(process)
    print a
    for useless in a:
        time.sleep(0.5)
        Kill_Process(process)

    import os, string
    host_ip = '192.168.202.189'
    domain_name = 'sh.ctcims.cn'
    base_port = 1300
    conf_file = open(os.path.dirname(__file__)+"/config.ini")
    for line in conf_file:
        tuple_conf = line.strip('\n').strip('\r').split("=")
        if len(tuple_conf) == 2:
            if tuple_conf[0] == "uac_host":
                host_ip = tuple_conf[1]
            elif tuple_conf[0] == "term_port":
                base_port = string.atoi(tuple_conf[1])
            elif tuple_conf[0] == "domain_name":
                domain_name = tuple_conf[1]
    conf_file.close()

    for x in range(ts_count):
        print 'default%d: %s %s %d' % (x, host_ip, domain_name, base_port + (10+x)*100)
        win32api.ShellExecute(0, 'Open', '%s/agents/winsockserver.exe' % os.path.dirname(__file__),
                              '%s %s %d' % (host_ip, domain_name, base_port + (10+x)*100),
                              '%s/agents' % os.path.dirname(__file__), 1)
        time.sleep(1.1)
    for x in range(us_count):
        print 'explicit%d; %s %s %d' % (x, host_ip, domain_name, base_port + (20+x)*100)
        win32api.ShellExecute(0, 'Open', '%s/agents/winsockserver.exe' % os.path.dirname(__file__),
                              '%s %s %d' % (host_ip, domain_name, base_port + (20+x)*100),
                              '%s/agents' % os.path.dirname(__file__), 1)
        time.sleep(1.1)


def init_agents(us_count, ts_count):
    process = 'winsockserver'# process name
    a = GetAllTargetProcesses(process)
    print a
    for useless in a:
        time.sleep(0.5)
        Kill_Process(process)

    import os, string
    host_ip = '192.168.202.189'
    domain_name = 'sh.ctcims.cn'
    base_port = 1300
    conf_file = open(os.path.dirname(__file__)+"/config.ini")
    for line in conf_file:
        tuple_conf = line.strip('\n').strip('\r').split("=")
        if len(tuple_conf) == 2:
            if tuple_conf[0] == "uac_host":
                host_ip = tuple_conf[1]
            elif tuple_conf[0] == "term_port":
                base_port = string.atoi(tuple_conf[1])
            elif tuple_conf[0] == "domain_name":
                domain_name = tuple_conf[1]
    conf_file.close()


    for x in range(us_count):
        print '%s %d' % (host_ip, base_port + (10+x)*100)
        win32api.ShellExecute(0, 'Open', '%s/us_agents/a%d/winsockserver.exe' % (os.path.dirname(__file__), x),
                              '%s %d' % (host_ip, base_port + (10+x)*100), '%s/us_agents/a%d' % (os.path.dirname(__file__), x), 1)
    for x in range(ts_count):
        print '%s %d' % (host_ip, base_port + (20+x)*100)
        win32api.ShellExecute(0, 'Open', '%s/ts_agents/a%d/winsockserver.exe' % (os.path.dirname(__file__), x),
                              '%s %d' % (host_ip, base_port + (20+x)*100), '%s/ts_agents/a%d' % (os.path.dirname(__file__), x), 1)

# ***********************************************************************
# ***********************************************************************
if __name__ == "__main__":
    #a = GetAllProcesses()
    process = 'notepad'# process name
    a = GetAllTargetProcesses(process)
    print a
    for useless in a:
        time.sleep(0.5)
        Kill_Process ( process )

    import os
    win32api.ShellExecute(0, 'Open', 'notepad.exe', 'param.txt',
                          '%s/agents/a01' % os.path.dirname(__file__), 1)
    win32api.ShellExecute(0, 'Open', 'notepad.exe', 'param.txt',
                          '%s/agents/a02' % os.path.dirname(__file__), 1)
    win32api.ShellExecute(0, 'Open', 'notepad.exe', 'param.txt',
                          '%s/agents/a03' % os.path.dirname(__file__), 1)




