from app import app
from app.usm import Usm
from app.tsm import Tsm
import startup_agent as sa
import time

usm = Usm()
tsm = Tsm()
print 'Default test accounts are: ',
print tsm.sessions

print 'Each default account has one independent channel.',
print 'And 3 more channels for explicit accounts.'
sa.init_agents_ex(3, len(tsm.sessions))

#app = Flask(__name__)
app.run(port=80, debug = True, use_reloader=False)
