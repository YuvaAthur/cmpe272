from flask import Flask, jsonify, abort, make_response, request

'''
# Debug mode for Flask App
`export FLASK_APP=WebServer`
`export FLASK_ENV=development`
`flask run`
'''
# Active change in this file is immediately visible!
# Flask restarts!

NOT_FOUND = 'Not found'
BAD_REQUEST = 'Bad request'

# def create_app(config_filename):
#    app = Flask(__name__)
#    app.config.from_pyfile(config_filename)
#    return app

app = Flask(__name__)

# Exploring creating RESTful Services
# Ref: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
app.tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.route('/')                 #decorator mapping root call
@app.route('/index')            #decorator mapping /index call
def index():
    return "Debug: Hello, welcome to the Web Server of team  Warriors"



@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': app.tasks})

@app.route('/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    tasks = app.tasks
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task})

if __name__ == '__main__':
    app = create_app()
    app.run()       # debug=True causes exception