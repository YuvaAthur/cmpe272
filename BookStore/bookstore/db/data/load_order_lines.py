import pymongo
import pprint
import bson

myclient = pymongo.MongoClient("mongodb+srv://cmpe272:cmpe272@cluster0-g5aa2.mongodb.net/test")
mydb = myclient["bookstore"]
mycol = mydb["order_lines"]

mylist = [
{ "order_id" : 1002, "_id" : 1 , "book_id" : 765, "quantity" : 2 },
{ "order_id" : 1002, "_id" : 2 , "book_id" : 755, "quantity" : 2 },
{ "order_id" : 1002, "_id" : 3 , "book_id" : 665, "quantity" : 2 },
{ "order_id" : 1003, "_id" : 1 , "book_id" : 565, "quantity" : 2  },
{ "order_id" : 1003, "_id" : 2 , "book_id" : 465, "quantity" : 2  },
{ "order_id" : 1004, "_id" : 1 ,  "book_id" : 365, "quantity" : 2  },
{ "order_id" : 1005, "_id" : 1 , "book_id" : 165, "quantity" : 2  },
{ "order_id" : 1005, "_id" : 2 , "book_id" : 265, "quantity" : 2  },
{ "order_id" : 1005, "_id" : 3 , "book_id" : 65, "quantity" : 2  },
{ "order_id" : 1005, "_id" : 4 , "book_id" : 55, "quantity" : 2  },
{ "order_id" : 1005, "_id" : 5 , "book_id" : 76, "quantity" : 2  },
{ "order_id" : 1006, "_id" : 1 , "book_id" : 6, "quantity" : 2  },
{ "order_id" : 1006, "_id" : 2 , "book_id" : 5, "quantity" : 2  },
{ "order_id" : 1006, "_id" : 3 , "book_id" : 7, "quantity" : 2  },
{ "order_id" : 1006, "_id" : 4 , "book_id" : 8, "quantity" : 2  },
{ "order_id" : 1007, "_id" : 1 , "book_id" : 111, "quantity" : 2  },
{ "order_id" : 1007, "_id" : 2 , "book_id" : 113, "quantity" : 2  },
{ "order_id" : 1008, "_id" : 1 , "book_id" : 4, "quantity" : 2  },
{ "order_id" : 1008, "_id" : 2 , "book_id" : 2, "quantity" : 2  },
{ "order_id" : 1008, "_id" : 3 , "book_id" : 66, "quantity" : 2  },
{ "order_id" : 1008, "_id" : 4 , "book_id" : 76, "quantity" : 2  },
{ "order_id" : 1008, "_id" : 5 , "book_id" : 77, "quantity" : 2  },
{ "order_id" : 1008, "_id" : 6 , "book_id" : 88, "quantity" : 2  },
{ "order_id" : 1008, "_id" : 7 , "book_id" : 99, "quantity" : 2  },
{ "order_id" : 1009, "_id" : 1 , "book_id" : 23, "quantity" : 2  },
{ "order_id" : 10010, "_id" : 1 ,  "book_id" : 71, "quantity" : 2  },
{ "order_id" : 10011, "_id" : 1 , "book_id" : 27, "quantity" : 2  },
{ "order_id" : 10011, "_id" : 2 , "book_id" : 43, "quantity" : 2  },
{ "order_id" : 10011, "_id" : 3 , "book_id" : 58, "quantity" : 2  },
{ "order_id" : 10011, "_id" : 4 , "book_id" : 94, "quantity" : 2  },
{ "order_id" : 10011, "_id" : 5 , "book_id" : 107, "quantity" : 2  },
{ "order_id" : 10011, "_id" : 6 , "book_id" : 201, "quantity" : 2  },
{ "order_id" : 10011, "_id" : 7 , "book_id" : 343, "quantity" : 2  },
{ "order_id" : 10011, "_id" : 8 , "book_id" : 234, "quantity" : 2  },
{ "order_id" : 10012, "_id" : 1 , "book_id" : 123, "quantity" : 2  },
{ "order_id" : 10012, "_id" : 2 , "book_id" : 34, "quantity" : 2  },
{ "order_id" : 10012, "_id" : 3 , "book_id" : 56, "quantity" : 2  },
{ "order_id" : 10012, "_id" : 4 , "book_id" : 88, "quantity" : 2  },
{ "order_id" : 10012, "_id" : 5 , "book_id" : 78, "quantity" : 2  },
{ "order_id" : 10012, "_id" : 6 , "book_id" : 95, "quantity" : 2  },
{ "order_id" : 10012, "_id" : 7 , "book_id" : 85, "quantity" : 2  },
{ "order_id" : 10013, "_id" : 1 , "book_id" : 75, "quantity" : 2  }
]

x = mycol.insert(mylist)

print(x.inserted_ids)

