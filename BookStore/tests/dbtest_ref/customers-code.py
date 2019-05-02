import unittest
import mongomock
import json
import list_customer

class DBTests(unittest.TestCase):
    def setUp(self):
        self.db = mongomock.MongoClient()['testdb']
        self.db.customer.insert_one({ "_id" : 2, "FirstName" : "Apple", "LastName" : "Seed", "address" : {"street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"} , "contact" : {"phone" : 111-111-1111 , "email" : "apple@test.com"} })
        self.db.customer.insert_one({ "_id" : 3, "FirstName" : "Orange", "LastName" : "Seed", "address" : {"street": "45 Fake Street", "city": "Faketon", "state": "CA", "zip": "12345"} , "contact" : {"phone" : 222-111-1111 , "email" : "orange@test.com"}})
 
    def tearDown(self):
        pass

    def test_get_available_customer(self):
        customer = list_customer.get_available_customer(self.db)
        print(customer)

if __name__ == '__main__':
    unittest.main()

