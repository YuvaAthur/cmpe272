import unittest
import mongomock
import json
import add_customer

class DBTests(unittest.TestCase):
	def setUp(self):
		self.db = mongomock.MongoClient()['testdb']
		self.cust_rec1={"_id" : 5, "FirstName" : "Melon", "LastName" : "Seed"}
 
	def tearDown(self):
        	pass

	def test_cust_add(self):
		ret=add_customer.add_cust(self.db,self.cust_rec1)
		print("Added Customer with ID --",ret.inserted_id)
		self.assertEqual(ret.inserted_id, 5)
		

if __name__ == '__main__':
    unittest.main()

