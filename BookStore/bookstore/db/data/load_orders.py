import pymongo
import pprint
import bson

myclient = pymongo.MongoClient("mongodb+srv://cmpe272:cmpe272@cluster0-g5aa2.mongodb.net/test")
mydb = myclient["bookstore"]
mycol = mydb["orders"]

mylist = [
{ "_id" : 1002, "customer_id" : 2 , "ship_address" : {"FirstName" : "Guava", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1003, "customer_id" : 3 , "ship_address" : {"FirstName" : "Apple", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1004, "customer_id" : 5 ,  "ship_address" : {"FirstName" : "Almond", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1005, "customer_id" : 4 , "ship_address" : {"FirstName" : "Watermelon", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1006, "customer_id" : 6 , "ship_address" : {"FirstName" : "Grape", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1007, "customer_id" : 9 , "ship_address" : {"FirstName" : "Berry", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1008, "customer_id" : 11 , "ship_address" : {"FirstName" : "Pumpkin", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 1009, "customer_id" : 12 , "ship_address" : {"FirstName" : "Lotus", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 10010, "customer_id" : 13 , "ship_address" : {"FirstName" : "Almond", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 10011, "customer_id" : 7 , "ship_address" : {"FirstName" : "Grapefruit", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 10012, "customer_id" : 8 , "ship_address" : {"FirstName" : "Test", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  },
{ "_id" : 10013, "customer_id" : 8 , "ship_address" : {"FirstName" : "Test", "LastName" : "Seed", "street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"}  }
]

x = mycol.insert(mylist)

print(x.inserted_ids)

