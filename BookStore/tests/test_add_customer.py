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

from bookstore.db.dbops.add_customer import add_cust


class DBTests(unittest.TestCase):
	def setUp(self):
		self.db = mongomock.MongoClient()['testdb']
		self.cust_rec1={"_id" : 5, "FirstName" : "Melon", "LastName" : "Seed"}
 
	def tearDown(self):
        	pass

	def test_cust_add(self):
#works		ret= bookstore.db.dbops.add_customer.add_cust(self.db,self.cust_rec1)
		#ret= add_cust(self.db,self.cust_rec1)
		ret= add_cust(self.db,self.cust_rec1)
		print("Added Customer with ID --",ret.inserted_id)
		self.assertEqual(ret.inserted_id, 5)
		
if __name__ == "__main__":
	unittest.main()



