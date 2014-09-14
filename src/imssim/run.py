from app import app
from app.usm import Usm
from app.tsm import Tsm
import startup_agent as sa
import time

usm = Usm()
tsm = Tsm()
print 'Test Config is: ',
print tsm.sessions

sa.init_agents(3, len(tsm.sessions))

#app = Flask(__name__)
app.run(port=80,debug = True)
