# coding=utf-8
__author__ = 'Marco'

from MySingleton import Singleton

class Usm(Singleton):
    """
    接口2的会话管理类，内部管理一个map，从workid映射到主叫号码
    """
    sessions = {}

    def __init__(self):
        """
        从配置文件config.ini中获取显式呼叫的容许并发数，默认为3，
        因此，默认的workid为20，21，22，初始主叫号码为0
        """
        import os, string
        explicit_channum = 3
        conf_file = open(os.path.dirname(os.path.dirname(__file__))+"/config.ini")
        for line in conf_file:
            tuple_conf = line.strip('\n').strip('\r').split("=")
            if len(tuple_conf) == 2:
                if tuple_conf[0] == "explicit_channum":
                    explicit_channum = string.atoi(tuple_conf[1])
                    break
        conf_file.close()
        for x in range(20, 20 + explicit_channum):
            self.sessions[str(x)] = '0'

    def checkCalling(self, calling):
        """
        根据主叫号码反查workid，找不到返回0
        """
        candi = '0'
        self.objs_locker.acquire()
        for (k, v) in self.sessions.items():
            if v == calling:
                candi = k
                break
        self.objs_locker.release()
        return candi

    def nailCalling(self, workid, calling):
        """
        将workid和主叫号码关联
        """
        self.objs_locker.acquire()
        self.sessions[workid] = calling
        self.objs_locker.release()



if __name__ == "__main__":
    sm = Usm()
    print sm.sessions
    sm2 = Usm()
    print sm2.sessions
    if sm == sm2:
        print 'equal.'
    print sm.checkCalling('0')
    print sm.checkCalling('68001234')
    sm2.nailCalling('5','68001234')
    print sm.checkCalling('68001234')
    pass

