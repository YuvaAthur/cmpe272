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
from bookstore.db.dbops.new_order import create_order

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

	def tearDown(self):
        	pass

	def test_create_order(self):
		customer_id=5
		book_list={'id':1,'qty':2},{'id':2,'qty':3}
		ret=create_order(self.db,customer_id,book_list)
		print("Created Order with ID --",ret)
		self.assertEqual(ret['NumItems'],2)
		

if __name__ == '__main__':
    unittest.main()

