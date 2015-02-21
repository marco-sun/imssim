from app import app
from app.usm import Usm
from app.tsm import Tsm
import time



import xml.etree.ElementTree as ET
import os
import sys
import string


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


def parseConfig(filePath, fileName):
    cfg_port = 80
    cfg_ip = "0.0.0.0"
    cfg_channum = 3
    xmlDoc = ET.parse(filePath + "/" + fileName)
    xmlRoot = xmlDoc.getroot()
    cmCfgNode = xmlRoot.find("cm/default")
    for node in cmCfgNode:
        if node.tag == 'srv_port':
            cfg_port = string.atoi(node.text)
            if cfg_port <= 0 or cfg_port >= 65535:
                cfg_port = 80
        elif node.tag == 'srv_ip':
            cfg_ip = node.text
        elif node.tag == 'explicit_channum':
            cfg_channum = string.atoi(node.text)
            if cfg_channum <= 0 or cfg_channum >= 10:
                cfg_channum = 3
    return cfg_ip, cfg_port, cfg_channum

srv_ip, srv_port, explicit_channum = parseConfig(getCurPath(), "config.xml")
usm = Usm(explicit_channum)
tsm = Tsm()
print 'Default test accounts are: ',
print tsm.sessions

print 'Each default account has one independent channel.',
print 'And 3 more channels for explicit accounts.'

#app = Flask(__name__)
app.run(host=srv_ip, port=srv_port, debug=True, use_reloader=False)
