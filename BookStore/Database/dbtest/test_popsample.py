import unittest
import mongomock
import json
import popsample 

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
		ret=popsample.add_cust(self.db,self.cust_rec1)
		print("Populated Customers data with IDs --",ret.inserted_ids)
		self.assertEqual(len(ret.inserted_ids), 5)
		

if __name__ == '__main__':
    unittest.main()

