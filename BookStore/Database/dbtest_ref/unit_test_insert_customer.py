import unittest 
import mongomock 
import pymongo
import json 
import add_customer 


class DBTests(unittest.TestCase): 
    def setUp(self): 
        self.db = mongomock.MongoClient()['testdb'] 
        #self.col = pymongo.collection.Collection(self.db,"Customer")
        #print(len(self.col.count()))
        self.cust_rect0={"_id" : 1, "FirstName" : "Apple", "LastName" : "Seed"}
        ret = self.db.customer.insert_one(self.cust_rec0).inserted_id
        print("Added Record",ret.in
        #self.cust_rec1={ "_id" : 5, "FirstName" : "Melon", "LastName" : "Seed"}
        # #print(self.db.list_collection_names)
        # self.assertEqual(len(customer), 1) 
                
    
    def tearDown(self): 
        pass 
        
    def test_cust_add(self): 
        ret=add_customer.add_cust(self.db,self.cust_rec1) 
        #collection=self.db["customer"]
        #print (collection)
        #print(self.db.list_collection_names)
        self.assertEqual(ret.inserted_id, 5) 
        # print(customer) 

if __name__ == '__main__': 
    unittest.main()
