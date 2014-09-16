# coding=utf-8
__author__ = 'Marco'

from MySingleton import Singleton

class Tsm(Singleton):

    sessions = {}  ## <workerid,tuple(uid,pwd)>

    def __init__(self):
        import os
        conf_file = open(os.path.dirname(os.path.dirname(__file__))+"/testnum.cfg")
        test_work_id = 10
        for line in conf_file:
            tuple_conf = line.strip('\n').strip('\r').split(",")
            if len(tuple_conf) == 2: ## calling number and password
                self.sessions[str(test_work_id)] = tuple_conf
                test_work_id += 1
        conf_file.close()


if __name__ == "__main__":
    sm = Tsm()
    print sm.sessions

    pass