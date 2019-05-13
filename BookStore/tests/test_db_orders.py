import unittest
import mongomock
import json


from .context import bookstore # needed by pytest & therefore travis

from bookstore.db.dbops.orders import create_order

class DBTests(unittest.TestCase):
    def setUp(self):
        self.client = mongomock.MongoClient()
        self.db = self.client[bookstore.db.DB]

