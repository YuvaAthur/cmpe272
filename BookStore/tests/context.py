import os
import sys

# Testing db ops
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bookstore

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bookstore/db')))
# import add_customer

# Testing app routes
from bookstore import webapi
# for config.py path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bookstore/webapi')))

# for routes.py / routescode.py path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bookstore/webapi/app')))
