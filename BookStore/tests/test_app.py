# Ref: https://pybit.es/simple-flask-api.html
# https://github.com/pybites/blog_code/blob/master/flaskapi/test_app.py 

from copy import deepcopy
#import unittest
import json

# Ref: https://stackoverflow.com/questions/34913348/flask-object-has-no-attribute-post-error-for-login-unit-test
# Ref: https://pythonhosted.org/Flask-Testing/
from flask_testing import TestCase 
from flask import Flask

from .context import bookstore # needed by pytest & therefore travis
from bookstore.webapi.web_server import app

BASE_TASK_URL = 'http://127.0.0.1:5000/api/v1.0/tasks'
BAD_TASK_URL = '{}/5'.format(BASE_TASK_URL)
GOOD_TASK_URL = '{}/3'.format(BASE_TASK_URL)

# Ref: https://realpython.com/python-web-applications-with-flask-part-iii/ 
class TestFlaskApi(TestCase):
    # If you don’t define create_app a NotImplementedError will be raised.
    def create_app(self):
        app.config.from_object(self)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.backup_items = deepcopy(app.tasks)  # no references!
        self.app = app.test_client()
        self.app.testing = True

    #@app.route('/api/v1.0/tasks', methods=['GET'])
    def test_get_tasks(self):
        response = self.client.get(BASE_TASK_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['tasks']), 2)

    #@app.route('/api/v1.0/tasks/<int:task_id>', methods=['GET'])
    def test_get_one_task(self):
        response = self.client.get("%s%s" % (BASE_TASK_URL, '/2'))
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['task']), 1)

    def tearDown(self):
        # reset app.items to initial state
        app.tasks = self.backup_items

