# coding=utf-8
__author__ = 'Marco'

import xml.etree.ElementTree as ET
import os
import sys
import string
from MySingleton import Singleton


class Gdm(Singleton):

    srv_port = 80
    srv_ip = '0.0.0.0'
    default_timeout = 25
    explicit_channum = 3
    dm_baseport = 1300
    uac_ip = '0.0.0.0'
    uas_ip = '118.85.214.1'
    uas_port = 5060
    domain_name = 'sh.ctcims.cn'

    def __init__(self):

        pass

    def readConfigXml(self, filePath, fileName):

        xmlDoc = ET.parse(filePath + "/" + fileName)
        xmlRoot = xmlDoc.getroot()
        cmCfgNode = xmlRoot.find("cm/default")
        for node in cmCfgNode:
            if node.tag == 'srv_port':
                self.srv_port = string.atoi(node.text)
                if self.srv_port <= 0 or self.srv_port >= 65535:
                    self.srv_port = 80
            elif node.tag == 'srv_ip':
                self.srv_ip = node.text
            elif node.tag == 'default_timeout':
                self.default_timeout = string.atoi(node.text)
                if self.default_timeout < 15 or self.default_timeout > 90:
                    self.default_timeout = 25
            elif node.tag == 'explicit_channum':
                self.explicit_channum = string.atoi(node.text)
                if self.explicit_channum <= 0 or self.explicit_channum >= 10:
                    self.explicit_channum = 3
            elif node.tag == 'dm_baseport':
                self.dm_baseport = string.atoi(node.text)
                if self.dm_baseport <= 127 or self.dm_baseport >= 65500:
                    self.dm_baseport = 1300
            elif node.tag == 'uac_ip':
                self.uac_ip = node.text
            elif node.tag == 'uas_ip':
                self.uas_ip = node.text
            elif node.tag == 'uas_port':
                self.uas_port = string.atoi(node.text)
                if self.uas_port <= 127 or self.uas_port >= 65500:
                    self.uas_port = 5060
            elif node.tag == 'domain_name':
                self.domain_name = node.text


if __name__ == "__main__":
    gdm = Gdm()
    cfgPath = os.path.dirname(os.path.dirname(__file__))
    gdm.readConfigXml(cfgPath, "config.xml")
    gdm2 = Gdm()

    if gdm == gdm2:
        print 'equal.'
    print type(gdm.srv_port), gdm.srv_port
    print type(gdm.srv_ip),gdm.srv_ip
    print type(gdm.default_timeout), gdm.default_timeout
    print type(gdm.explicit_channum),gdm.explicit_channum
    print type(gdm.dm_baseport), gdm.dm_baseport
    print type(gdm.uac_ip),gdm.uac_ip
    print type(gdm.uas_ip), gdm.uas_ip
    print type(gdm.uas_port),gdm.uas_port
    print type(gdm.domain_name), gdm.domain_name

    abspath = os.path.dirname(__file__)
    sys.path.append(abspath)
    print "os.path.dirname(__file__) is " + abspath
    print "sys.path[0] is " + sys.path[0]
    if abspath == '':
        cur_path = sys.path[0]
    else:
        cur_path = abspath
    print "choose curpath is " + cur_path
    pass

