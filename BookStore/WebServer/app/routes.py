from app import app

@app.route('/')                 #decorator mapping root call
@app.route('/index')            #decorator mapping /index call
def index():
    return "Hello, welcome to the Web Server of team  Warriors"