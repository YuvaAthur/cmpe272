import mongomock
import json

from db.dbops.popsample import pop_books, pop_customers, pop_inventory, pop_orders
from svr import db_data

class AppDB():
    def __init__(self):
        self.client= mongomock.MongoClient()
        self.db = self.client["db.DB"]
    
    def popsample(self):
        ret1 = pop_books(self.db,db_data.sample_books)
        ret2 = pop_customers(self.db,db_data.sample_customers)
        ret3 = pop_inventory(self.db, db_data.sample_inventory)
        ret4 = pop_orders(self.db,db_data.sample_orders,db_data.sample_orderlines)

        

