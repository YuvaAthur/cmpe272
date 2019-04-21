import pymongo
import pprint
import bson

myclient = pymongo.MongoClient("mongodb+srv://cmpe272:cmpe272@cluster0-g5aa2.mongodb.net/test")
mydb = myclient["warriors_bookstore"]
mycol = mydb["war_order_lines"]

mylist = [
{ "order_id" : 1002, "orderLineid" : 1 , "BookID" : 765, "Quantity" : 2 },
{ "order_id" : 1002, "orderLineid" : 2 , "BookID" : 755, "Quantity" : 2 },
{ "order_id" : 1002, "orderLineid" : 3 , "BookID" : 665, "Quantity" : 2 },
{ "order_id" : 1003, "orderLineid" : 1 , "BookID" : 565, "Quantity" : 2  },
{ "order_id" : 1003, "orderLineid" : 2 , "BookID" : 465, "Quantity" : 2  },
{ "order_id" : 1004, "orderLineid" : 1 ,  "BookID" : 365, "Quantity" : 2  },
{ "order_id" : 1005, "orderLineid" : 1 , "BookID" : 165, "Quantity" : 2  },
{ "order_id" : 1005, "orderLineid" : 2 , "BookID" : 265, "Quantity" : 2  },
{ "order_id" : 1005, "orderLineid" : 3 , "BookID" : 65, "Quantity" : 2  },
{ "order_id" : 1005, "orderLineid" : 4 , "BookID" : 55, "Quantity" : 2  },
{ "order_id" : 1005, "orderLineid" : 5 , "BookID" : 76, "Quantity" : 2  },
{ "order_id" : 1006, "orderLineid" : 1 , "BookID" : 6, "Quantity" : 2  },
{ "order_id" : 1006, "orderLineid" : 2 , "BookID" : 5, "Quantity" : 2  },
{ "order_id" : 1006, "orderLineid" : 3 , "BookID" : 7, "Quantity" : 2  },
{ "order_id" : 1006, "orderLineid" : 4 , "BookID" : 8, "Quantity" : 2  },
{ "order_id" : 1007, "orderLineid" : 1 , "BookID" : 111, "Quantity" : 2  },
{ "order_id" : 1007, "orderLineid" : 2 , "BookID" : 113, "Quantity" : 2  },
{ "order_id" : 1008, "orderLineid" : 1 , "BookID" : 4, "Quantity" : 2  },
{ "order_id" : 1008, "orderLineid" : 2 , "BookID" : 2, "Quantity" : 2  },
{ "order_id" : 1008, "orderLineid" : 3 , "BookID" : 66, "Quantity" : 2  },
{ "order_id" : 1008, "orderLineid" : 4 , "BookID" : 76, "Quantity" : 2  },
{ "order_id" : 1008, "orderLineid" : 5 , "BookID" : 77, "Quantity" : 2  },
{ "order_id" : 1008, "orderLineid" : 6 , "BookID" : 88, "Quantity" : 2  },
{ "order_id" : 1008, "orderLineid" : 7 , "BookID" : 99, "Quantity" : 2  },
{ "order_id" : 1009, "orderLineid" : 1 , "BookID" : 23, "Quantity" : 2  },
{ "order_id" : 10010, "orderLineid" : 1 ,  "BookID" : 71, "Quantity" : 2  },
{ "order_id" : 10011, "orderLineid" : 1 , "BookID" : 27, "Quantity" : 2  },
{ "order_id" : 10011, "orderLineid" : 2 , "BookID" : 43, "Quantity" : 2  },
{ "order_id" : 10011, "orderLineid" : 3 , "BookID" : 58, "Quantity" : 2  },
{ "order_id" : 10011, "orderLineid" : 4 , "BookID" : 94, "Quantity" : 2  },
{ "order_id" : 10011, "orderLineid" : 5 , "BookID" : 107, "Quantity" : 2  },
{ "order_id" : 10011, "orderLineid" : 6 , "BookID" : 201, "Quantity" : 2  },
{ "order_id" : 10011, "orderLineid" : 7 , "BookID" : 343, "Quantity" : 2  },
{ "order_id" : 10011, "orderLineid" : 8 , "BookID" : 234, "Quantity" : 2  },
{ "order_id" : 10012, "orderLineid" : 1 , "BookID" : 123, "Quantity" : 2  },
{ "order_id" : 10012, "orderLineid" : 2 , "BookID" : 34, "Quantity" : 2  },
{ "order_id" : 10012, "orderLineid" : 3 , "BookID" : 56, "Quantity" : 2  },
{ "order_id" : 10012, "orderLineid" : 4 , "BookID" : 88, "Quantity" : 2  },
{ "order_id" : 10012, "orderLineid" : 5 , "BookID" : 78, "Quantity" : 2  },
{ "order_id" : 10012, "orderLineid" : 6 , "BookID" : 95, "Quantity" : 2  },
{ "order_id" : 10012, "orderLineid" : 7 , "BookID" : 85, "Quantity" : 2  },
{ "order_id" : 10013, "orderLineid" : 1 , "BookID" : 75, "Quantity" : 2  }
]

x = mycol.insert(mylist)

print(x.inserted_ids)

