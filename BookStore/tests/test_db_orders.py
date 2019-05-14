from .test_db_base import DBTestsBase

from .context import bookstore # needed by pytest & therefore travis

from bookstore.db.dbops.orders import create_order, fulfill_order, del_order
from bookstore.db.dbops.customers import add_cust
from bookstore.db.dbops.books import  add_book, get_available_books
from bookstore.db.dbops.inventory  import add_inv


from tests import db_data 


class DBTests(DBTestsBase):
    def setUp(self):
        self.db = self.client[bookstore.db.DB]
        self.cust_rec1 = db_data.cust_rec1
        self.cust_rec2 = db_data.cust_rec2
        self.book_rec1 = db_data.book_rec1
        self.book_rec2 = db_data.book_rec2
        self.book_rec3 = db_data.book_rec3
        self.inv_rec1 = db_data.inv_rec1
        self.inv_rec2 = db_data.inv_rec2
        self.inv_rec3 = db_data.inv_rec3



    def step0(self):
        print ("orders::add cust, book, inv")
        ret = add_cust(self.db, self.cust_rec1)
        ret = add_cust(self.db, self.cust_rec2)
        ret = add_book(self.db,self.book_rec1)
        ret = add_book(self.db,self.book_rec2)
        ret = add_book(self.db,self.book_rec3)
        ret = add_inv(self.db,self.inv_rec1)
        ret = add_inv(self.db,self.inv_rec2)      
        ret = add_inv(self.db,self.inv_rec3)    
        print ("orders::get_available_books")
        ret = get_available_books(self.db)
        self.assertEqual(len(ret),2)  
        for book in ret:
            print ("orders::get_available_books: book_id = ", book['_id']," quantity = ", book['quantity'] )



    def step1(self):
        print ("orders::create_order")
        customer_id=5
        book_list={'book_id':4,'quantity':2},{'book_id':19,'quantity':3}
        ret=create_order(self.db,customer_id,book_list)
        #{"order_id": newOrderId, "num_order_lines" : len(book_list)}
        self.assertEqual(ret['num_order_lines'],2)
        print ("orders::create_order order id ", ret['order_id'])
        self.order_id = ret['order_id']


    def step2(self):
        print ("orders::fulfill_order order id is ",self.order_id)
        ret=fulfill_order(self.db,self.order_id)
        self.assertEqual(len(ret),2)

    def step3(self):
        print ("orders::del_order order id is ",self.order_id)
        ret=del_order(self.db,self.order_id)
        #{'num_deleted_order': del2.deletedCount, 'num_removed_order_lines': del1.nRemoved}
        self.assertEqual(ret['num_deleted_order'],1)
        self.assertEqual(ret['num_removed_order_lines'],2)

	
