
from flask import Flask

app = Flask(__name__)  #configures Flask to load associated files

from app import routes #app is Flask instance in this package

# programmatic does not seem to work
# have to  $ . venv/bin/activate  | $ sudo bash to get access to port 80.
# better way is to use CLI :
#       $ flask run --host=0.0.0.0 --port=80
## Note: Not sure if this is the right place at all!
#if __name__ == '__main__':
#      app.run(host='0.0.0.0', port=80)