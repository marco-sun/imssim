# coding=utf-8
__author__ = 'Marco'

import threading

class Singleton(object):

    objs  = {}
    objs_locker =  threading.Lock()

    def __new__(cls, *args, **kv):
        if cls in cls.objs:
            return cls.objs[cls]['obj']

        cls.objs_locker.acquire()
        try:
            if cls in cls.objs: ## double check locking
                return cls.objs[cls]['obj']
            obj = object.__new__(cls)
            cls.objs[cls] = {'obj': obj, 'init': False}
            setattr(cls, '__init__', cls.decorate_init(obj.__init__))
            return obj
        finally:
            cls.objs_locker.release()
            print 'locker released.'

    @classmethod
    def decorate_init(cls, fn):
        def init_wrap(*args):
            if not cls.objs[cls]['init']:
                print 'first run init.'
                print args
                nargs = list(args)
                nargs.pop(0)
                fn(*nargs)
                cls.objs[cls]['init'] = True
            return

        return init_wrap

class SessionManager(Singleton):

    sessions = {}

    def __init__(self, k):
        print '%s inited.' % k
        for x in range(1,10):
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
    sm = SessionManager('test1')
    print sm.sessions
    sm2 = SessionManager('test2')
    print sm2.sessions
    if sm == sm2:
        print 'equal.'
    print sm.checkCalling('0')
    print sm.checkCalling('68001234')
    sm2.nailCalling('5','68001234')
    print sm.checkCalling('68001234')
    pass
