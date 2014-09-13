# coding=utf-8
__author__ = 'Marco'

from MySingleton import Singleton

class Usm(Singleton):

    sessions = {}

    def __init__(self):
        for x in range(10,20):
            self.sessions[str(x)] = '0'

    def checkCalling(self, calling):

        candi = '0'
        self.objs_locker.acquire()
        for (k, v) in self.sessions.items():
            if v == calling:
                candi = k
                break
        self.objs_locker.release()
        return candi

    def nailCalling(self, workid, calling):

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

