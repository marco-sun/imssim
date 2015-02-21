# coding=utf-8
__author__ = 'Marco'

from app import app
from app.sm import Sm
from app.gdm import Gdm
import os
import sys


def getCurPath():
    abspath = os.path.dirname(__file__)
    sys.path.append(abspath)
    print "os.path.dirname(__file__) is " + abspath
    print "sys.path[0] is " + sys.path[0]
    if abspath == '':
        #os.chdir(sys.path[0])
        cur_path = sys.path[0]
    else:
        #os.chdir(abspath)
        cur_path = abspath
    print "choose curpath is " + cur_path
    return cur_path

gdm = Gdm()
gdm.readConfigXml(getCurPath(), "config.xml")
sm = Sm(gdm.explicit_channum)
print 'Default test accounts are: ',
print sm.tsessions

print 'Each default account has one independent channel.',
print 'And 3 more channels for explicit accounts.'

#app = Flask(__name__)
app.run(host=gdm.srv_ip, port=gdm.srv_port, debug=True, use_reloader=False)
