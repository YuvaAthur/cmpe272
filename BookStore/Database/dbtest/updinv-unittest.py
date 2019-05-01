import unittest
import mongomock
import json
import updinventory 

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
		ret=updinventory.fulfill_order(self.db,5)
		print("Created Order with ID --",ret)
		#self.assertEqual(ret['NumItems'],2)
		

if __name__ == '__main__':
    unittest.main()

