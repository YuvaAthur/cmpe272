import pymongo
import pprint
import bson

myclient = pymongo.MongoClient("mongodb+srv://cmpe272:cmpe272@cluster0-g5aa2.mongodb.net/test")
mydb = myclient["bookstore"]
mycol = mydb["customer"]

mylist = [
{ "_id" : 2, "FirstName" : "Apple", "LastName" : "Seed", "address" : {"street": "123 Fake Street", "city": "Faketon", "state": "MA", "zip": "12345"} , "contact" : {"phone" : 111-111-1111 , "email" : "apple@test.com"} },
{ "_id" : 3, "FirstName" : "Orange", "LastName" : "Seed", "address" : {"street": "45 Fake Street", "city": "Faketon", "state": "CA", "zip": "12345"} , "contact" : {"phone" : 222-111-1111 , "email" : "orange@test.com"}},
{ "_id" : 4, "FirstName" : "Grape", "LastName" : "Seed", "address" : {"street": "678 Fake Street", "city": "Faketon", "state": "FL", "zip": "12345"} , "contact" : {"phone" : 223-111-1111 , "email" : "grape@test.com"}},
{ "_id" : 5, "FirstName" : "Berry", "LastName" : "Seed", "address" : {"street": "900 Fake Street", "city": "Faketon", "state": "NH", "zip": "12345"} , "contact" : {"phone" : 333-111-1111 , "email" : "berry@test.com"}},
{ "_id" : 6, "FirstName" : "Guava", "LastName" : "Seed", "address" : {"street": "200 Fake Street", "city": "Faketon", "state": "CT", "zip": "12345"} , "contact" : {"phone" : 444-111-1111 , "email" : "guava@test.com"}},
{ "_id" : 7, "FirstName" : "Watermelon", "LastName" : "Seed", "address" : {"street": "1234 Fake Street", "city": "Faketon", "state": "NY", "zip": "12345"} , "contact" : {"phone" : 155-111-1111 , "email" : "watermelon@test.com"}},
{ "_id" : 8, "FirstName" : "Pumpkin", "LastName" : "Seed", "address" : {"street": "500 Fake Street", "city": "Faketon", "state": "HI", "zip": "12345"} , "contact" : {"phone" : 545-111-1111 , "email" : "pumpkin@test.com"}},
{ "_id" : 9, "FirstName" : "Almond", "LastName" : "Seed", "address" : {"street": "333 Fake Street", "city": "Faketon", "state": "WA", "zip": "12345"}, "contact" : {"phone" : 777-111-1111 , "email" : "almond@test.com"} },
{ "_id" : 10, "FirstName" : "Rose", "LastName" : "Seed", "address" : {"street": "789 Fake Street", "city": "Faketon", "state": "OR", "zip": "12345"}, "contact" : {"phone" : 789-111-1111 , "email" : "rose@test.com"} },
{ "_id" : 11, "FirstName" : "Lotus", "LastName" : "Seed", "address" : {"street": "2000 Fake Street", "city": "Faketon", "state": "AL", "zip": "12345"}, "contact" : {"phone" : 192-111-1111 , "email" : "lotus@test.com"} },
{ "_id" : 12, "FirstName" : "Grapefruit", "LastName" : "Seed", "address" : {"street": "4001 Fake Street", "city": "Faketon", "state": "TX", "zip": "12345"}, "contact" : {"phone" : 945-111-1111 , "email" : "grapefruit@test.com"} },
{ "_id" : 13, "FirstName" : "Test", "LastName" : "Seed", "address" : {"street": "555 Fake Street", "city": "Faketon", "state": "WY", "zip": "12345"}, "contact" : {"phone" : 808-111-1111 , "email" : "test@test.com"} }
]

x = mycol.insert(mylist)

print(x.inserted_ids)

