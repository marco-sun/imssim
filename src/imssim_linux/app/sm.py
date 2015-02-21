# coding=utf-8
__author__ = 'Marco'

from MySingleton import Singleton


class Sm(Singleton):

    usessions = {}
    tsessions = {}

    def __init__(self, explicit_channum=3):

        work_id = 1
        # prepare test channels
        import os
        conf_file = open(os.path.dirname(os.path.dirname(__file__))+"/testnum.cfg")
        for line in conf_file:
            tuple_conf = line.strip('\n').strip('\r').split(",")
            if len(tuple_conf) == 2: ## calling number and password
                self.tsessions[str(work_id)] = tuple_conf
                work_id += 1
        conf_file.close()
        # prepare user channels
        for x in range(0, explicit_channum):
            self.usessions[str(work_id)] = ''
            work_id += 1

    def checkCalling(self, calling):

        candi = '0'
        self.objs_locker.acquire()
        for (k, v) in self.usessions.items():
            if v == calling:
                candi = k
                break
        self.objs_locker.release()
        return candi

    def nailCalling(self, workid, calling):

        self.objs_locker.acquire()
        self.usessions[workid] = calling
        self.objs_locker.release()



if __name__ == "__main__":
    sm = Sm(4)
    print sm.usessions
    sm2 = Sm()
    print sm2.usessions
    if sm == sm2:
        print 'equal.'
    print sm.checkCalling('0')
    print sm.checkCalling('68001234')
    sm2.nailCalling('5','68001234')
    print sm.checkCalling('68001234')
    pass
