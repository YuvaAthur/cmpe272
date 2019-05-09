import pymongo
import pprint
import bson

myclient = pymongo.MongoClient("mongodb+srv://cmpe272:cmpe272@cluster0-g5aa2.mongodb.net/test")
mydb = myclient["bookstore"]
mycol = mydb["orders"]

mylist = [
{ "_id" : 1002, "Customer_id" : 2 , "Shipaddress" : {"FirstName" : "Guava", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1003, "Customer_id" : 3 , "Shipaddress" : {"FirstName" : "Apple", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1004, "Customer_id" : 5 ,  "Shipaddress" : {"FirstName" : "Almond", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1005, "Customer_id" : 4 , "Shipaddress" : {"FirstName" : "Watermelon", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1006, "Customer_id" : 6 , "Shipaddress" : {"FirstName" : "Grape", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1007, "Customer_id" : 9 , "Shipaddress" : {"FirstName" : "Berry", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1008, "Customer_id" : 11 , "Shipaddress" : {"FirstName" : "Pumpkin", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1009, "Customer_id" : 12 , "Shipaddress" : {"FirstName" : "Lotus", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 10010, "Customer_id" : 13 ,  "Shipaddress" : {"FirstName" : "Almond", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 10011, "Customer_id" : 7 , "Shipaddress" : {"FirstName" : "Grapefruit", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 10012, "Customer_id" : 8 , "Shipaddress" : {"FirstName" : "Test", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 10013, "Customer_id" : 8 , "Shipaddress" : {"FirstName" : "Test", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  }
]

x = mycol.insert(mylist)

print(x.inserted_ids)

