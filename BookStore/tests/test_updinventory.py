import unittest
import mongomock
import json


# path resolution for sibling directories test and bookstore
# https://stackoverflow.com/questions/39134718/how-to-add-a-package-to-sys-path-for-testing
# `tests` directory has to be declared a module/package
#	# so add __init__.py to that folder
#	#  .context is for relative import --> did not work
#	# https://stackoverflow.com/questions/45446418/modulenotfounderror-no-module-named-main-xxxx-main-is-not-a-packag
#from context import bookstore # this works from command line
from .context import bookstore # needed by pytest & therefore travis
from bookstore.db.dbops.updinventory import fulfill_order

class DBTests(unittest.TestCase):
	def setUp(self):
		self.db = mongomock.MongoClient()['testdb']
		self.db.customer.insert_one({"_id" : 5, "FirstName" : "Melon", "LastName" : "Seed"})
		self.db.customer.insert_one({"_id" : 6, "FirstName" : "Grape", "LastName" : "Seed"})
		self.db.books.insert_one({'_id': '1', 'title': 'A test book'})
		self.db.books.insert_one({'_id': '2', 'title': 'Another test book'})
		self.db.books.insert_one({'_id': '3', 'title': 'A rare book'})
		self.db.inventory.insert_one({'_id': '1', 'id': '1', 'qty': 5})
		self.db.inventory.insert_one({'_id': '2', 'id': '2', 'qty': 7})
		self.db.orders.insert_one({'_id': '5', 'customer_id': '1'})
		self.db.order_lines.insert_one({'_id': '1','OrderID': '5','BookId': '1','Qty': '2'})
		self.db.order_lines.insert_one({'_id': '2','OrderID': '5','BookId': '2','Qty': '3'})

	def tearDown(self):
        	pass

	def test_fulfill_order(self):
		ret=fulfill_order(self.db,5)
		#print("Created Order with ID --",ret)
		self.assertEqual(ret,2)
		
# not required if running from pytest		
# if __name__ == "__main__":
# 	unittest.main()

