import unittest
import mongomock
import json

# consolidating all dbops tests into one file

from .context import bookstore # needed by pytest & therefore travis

from bookstore.db.dbops.add_customer import add_cust
from bookstore.db.dbops.list_books import get_available_books
from bookstore.db.dbops.new_order import create_order
from bookstore.db.dbops.popsample import pop_sample
from bookstore.db.dbops.updinventory import fulfill_order


class DBTests(unittest.TestCase):
	def setUp(self):
		self.db = mongomock.MongoClient()['testdb']
		# test_cust_add
		self.cust_rec1={"_id" : 2, "FirstName" : "Melon", "LastName" : "Seed"}
        # test_get_available_books
		self.db.books.insert_one({'_id': '1', 'title': 'A test book'})
		self.db.books.insert_one({'_id': '2', 'title': 'Another test book'})
		self.db.books.insert_one({'_id': '3', 'title': 'A rare book'})
		self.db.inventory.insert_one({'_id': '1', 'id': '1', 'qty': 5})
		self.db.inventory.insert_one({'_id': '2', 'id': '2', 'qty': 0})
		# test_create_order
		self.db.customer.insert_one({"_id" : 5, "FirstName" : "Melon", "LastName" : "Seed"})
		self.db.customer.insert_one({"_id" : 6, "FirstName" : "Grape", "LastName" : "Seed"})
		self.db.books.insert_one({'_id': '5', 'title': 'A test book'})
		self.db.books.insert_one({'_id': '6', 'title': 'Another test book'})
		self.db.books.insert_one({'_id': '7', 'title': 'A rare book'})
		self.db.inventory.insert_one({'_id': '5', 'id': '1', 'qty': 5})
		self.db.inventory.insert_one({'_id': '6', 'id': '2', 'qty': 7})
		# test_pop_sample
		self.cust_rec1=[{"_id" : 10, "FirstName" : "Melon", "LastName" : "Seed"},
				{"_id" : 11, "FirstName" : "Apple", "LastName" : "Seed"},
				{"_id" : 12, "FirstName" : "Orange", "LastName" : "Seed"},
				{"_id" : 13, "FirstName" : "Grape", "LastName" : "Seed"},
				{"_id" : 14, "FirstName" : "Berry", "LastName" : "Seed"}]
		# test_fulfill_order
		self.db.customer.insert_one({"_id" : 15, "FirstName" : "Melon", "LastName" : "Seed"})
		self.db.customer.insert_one({"_id" : 16, "FirstName" : "Grape", "LastName" : "Seed"})
		self.db.books.insert_one({'_id': '15', 'title': 'A test book'})
		self.db.books.insert_one({'_id': '16', 'title': 'Another test book'})
		self.db.books.insert_one({'_id': '17', 'title': 'A rare book'})
		self.db.inventory.insert_one({'_id': '15', 'id': '1', 'qty': 5})
		self.db.inventory.insert_one({'_id': '16', 'id': '2', 'qty': 7})
		self.db.orders.insert_one({'_id': '5', 'customer_id': '1'})
		self.db.order_lines.insert_one({'_id': '1','OrderID': '5','BookId': '15','Qty': '2'})
		self.db.order_lines.insert_one({'_id': '2','OrderID': '5','BookId': '16','Qty': '3'})


	def tearDown(self):
        	pass

	def test_cust_add(self):
		ret= add_cust(self.db,self.cust_rec1)
		print("Added Customer with ID --",ret.inserted_id)
		self.assertEqual(ret.inserted_id, 2)
		
	def test_get_available_books(self):
		books = get_available_books(self.db)
		self.assertEqual(len(books), 5) # it should be 9, right?
		#print(books)

	def test_create_order(self):
		customer_id=5
		book_list={'id':1,'qty':2},{'id':2,'qty':3}
		ret=create_order(self.db,customer_id,book_list)
		#print("Created Order with ID --",ret)
		self.assertEqual(ret['NumItems'],2)

	def test_cust_add(self):
		ret=pop_sample(self.db,self.cust_rec1)
		print("Populated Customers data with IDs --",ret.inserted_ids)
		self.assertEqual(len(ret.inserted_ids), 5)

	# fulfill_order method is not ready
	# def test_fulfill_order(self):
	# 	ret=fulfill_order(self.db,5)
	# 	#print("Order Items --",ret)
	# 	self.assertEqual(ret,2)