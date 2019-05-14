from .test_db_base import DBTestsBase

from .context import bookstore # needed by pytest & therefore travis

# from bookstore.db.dbops.orders import create_order, fulfill_order, del_order
# from bookstore.db.dbops.customers import add_cust
# from bookstore.db.dbops.books import  add_book, get_available_books
# from bookstore.db.dbops.inventory  import add_inv

from bookstore.db.dbops.popsample import pop_books, pop_customers, pop_inventory, pop_orders
from bookstore.webapi.app import db_data

class DBTests(DBTestsBase):
    def setUp(self):
        self.db = self.client[bookstore.db.DB]
        self.books = db_data.sample_books
        self.customers = db_data.sample_customers
        self.inventory = db_data.sample_inventory
        self.orders = db_data.sample_orders
        self.orderlines = db_data.sample_orderlines

    def step1(self):
        print (" --- Step 1: popsample::pop_books")
        ret=pop_books(self.db,self.books)
        self.assertEqual(len(ret.inserted_ids),19)  

    def step2(self):
        print (" --- Step 2: popsample::pop_customers")
        ret=pop_customers(self.db,self.customers)
        self.assertEqual(len(ret.inserted_ids),4)      

    def step3(self):
        print (" --- Step 3: popsample::pop_inventory")
        ret=pop_inventory(self.db,self.inventory)
        self.assertEqual(len(ret.inserted_ids),19)      

    def step4(self):
        print (" --- Step 3: popsample::pop_orders")
        print ("num orders ", len(self.orders))
        print ("num order lines", len(self.orderlines))
        ret=pop_orders(self.db,self.orders,self.orderlines)
        self.assertEqual(len(ret['num_orders']),5)      
        self.assertEqual(len(ret['num_order_lines']),15)      