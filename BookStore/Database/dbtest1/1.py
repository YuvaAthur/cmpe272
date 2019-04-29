import pymongo

myclient = pymongo.MongoClient("mongodb+srv://cmpe272:cmpe272@cluster0-g5aa2.mongodb.net/test")
mydb = myclient["warriors_bookstore"]
mycol = mydb["war_customers"]

x=mycol.find()

for y in x:
  	print(y)

