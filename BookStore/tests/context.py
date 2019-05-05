import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bookstore
from bookstore import webapi

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bookstore/webapi')))
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bookstore/db')))
# import add_customer
