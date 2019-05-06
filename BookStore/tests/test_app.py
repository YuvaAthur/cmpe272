# Ref: https://pybit.es/simple-flask-api.html
# https://github.com/pybites/blog_code/blob/master/flaskapi/test_app.py 

from copy import deepcopy
#import unittest
import json
from pprint import pprint

# Ref: https://stackoverflow.com/questions/34913348/flask-object-has-no-attribute-post-error-for-login-unit-test
# Ref: https://pythonhosted.org/Flask-Testing/
from flask_testing import TestCase 
from flask import Flask

from .context import bookstore # needed by pytest & therefore travis

## 
from .context import webapi # added more system paths
from app import app

BASE_BOOK_URL = 'http://127.0.0.1:5000/api/v1.0/books'
BAD_BOOK_URL = '{}/5'.format(BASE_BOOK_URL)
GOOD_BOOK_URL = '{}/3'.format(BASE_BOOK_URL)

custorder = { 
    'custorder' : {
        'customerid':1,
        'booklist':[
            {'bookid':1,'qty':1},
            {'bookid':2,'qty':2}
        ]
    }
}
BASE_ORDER_URL = 'http://127.0.0.1:5000/api/v1.0/orders'



# Ref: https://realpython.com/python-web-applications-with-flask-part-iii/ 
class TestFlaskApi(TestCase):
    # If you don’t define create_app a NotImplementedError will be raised.
    def create_app(self):
        app.config.from_object(self)
        app.config['TESTING'] = True
        #print(app.config['DEBUG'])      #execution reaches here
        return app

    def setUp(self):
        self.backup_items = deepcopy(app.books)  
        self.app = app.test_client()
        self.app.testing = True

    #@app.route('/api/v1.0/books', methods=['GET'])
    def test_get_books(self):
        response = self.client.get(BASE_BOOK_URL)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(len(data['books']), 3)

    #@app.route('/api/v1.0/books/<int:BOOK_id>', methods=['GET'])
    def test_get_one_BOOK(self):
        response = self.client.get("%s%s" % (BASE_BOOK_URL, '/978-1977051875'))
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['book']), 1)
    
    #@app.route('/api/v1.0/orders', methods=['POST'])
    def test_post_order_noval(self):
        response = self.client.post("%s" % (BASE_ORDER_URL))
        self.assertEqual(response.status_code, 400) # Bad request return


    #@app.route('/api/v1.0/orders', methods=['POST'])
    # def test_post_order(self):
    #     # print (BASE_ORDER_URL, custorder)
    #     response = self.client.post("%s%s" % (BASE_ORDER_URL, custorder))
    #     self.assertEqual(response.status_code, 201)
    #     data = json.loads(response.get_data())
    #     self.assertEqual(len(data['orderid']), 1)

    def tearDown(self):
        # reset app.items to initial state
        app.books = self.backup_items
        pass

