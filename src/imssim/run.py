from app import app
from app.usm import Usm
from app.tsm import Tsm
import startup_agent as sa
import time

usm = Usm()
tsm = Tsm()
print 'Default test accounts are: ',
print tsm.sessions

import os
import sys
import string
srv_port = 80
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
print abspath
print sys.path[0]
if abspath == '':
    #os.chdir(sys.path[0])
    cur_path = sys.path[0]
else:
    #os.chdir(abspath)
    cur_path = abspath

conf_file = open(cur_path +
                 "/config.ini")
for line in conf_file:
    tuple_conf = line.strip('\n').strip('\r').split("=")
    if len(tuple_conf) == 2:
        if tuple_conf[0] == "port":
            srv_port = string.atoi(tuple_conf[1])
conf_file.close()

print 'Each default account has one independent channel.',
print 'And 3 more channels for explicit accounts.'
sa.init_agents_ex(3, len(tsm.sessions))

#app = Flask(__name__)
app.run(port=srv_port, debug=True, use_reloader=False)
