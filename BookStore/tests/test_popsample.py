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
from bookstore.db.dbops.popsample import add_cust

class DBTests(unittest.TestCase):
	def setUp(self):
		self.db = mongomock.MongoClient()['testdb']
		self.cust_rec1=[{"_id" : 5, "FirstName" : "Melon", "LastName" : "Seed"},
				{"_id" : 6, "FirstName" : "Apple", "LastName" : "Seed"},
				{"_id" : 7, "FirstName" : "Orange", "LastName" : "Seed"},
				{"_id" : 8, "FirstName" : "Grape", "LastName" : "Seed"},
				{"_id" : 9, "FirstName" : "Berry", "LastName" : "Seed"}]
 
	def tearDown(self):
        	pass

	def test_cust_add(self):
		ret=add_cust(self.db,self.cust_rec1)
		print("Populated Customers data with IDs --",ret.inserted_ids)
		self.assertEqual(len(ret.inserted_ids), 5)
		

if __name__ == '__main__':
    unittest.main()

