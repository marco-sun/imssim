from app import app
from app.usm import Usm
from app.tsm import Tsm

usm = Usm()
tsm = Tsm()
print 'Test Config is: ',
print tsm.sessions

#app = Flask(__name__)
app.run(port=80,debug = True)
