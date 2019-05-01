import pymongo
import pprint
import bson

myclient = pymongo.MongoClient("mongodb+srv://cmpe272:cmpe272@cluster0-g5aa2.mongodb.net/test")
mydb = myclient["warriors_bookstore"]
mycol = mydb["war_books"]

pipeline = [{
	"$lookup": {
		"from": "war_inventory",
		"localField": "_id",
		"foreignField": "book_id",
		"as": "war_inventory_docs"
		}
},{
	"$match": {
		"war_inventory_docs": {
			"$ne": []
		}
	}
},{
		"$addFields": {
			"war_inventory_docs": {
			"$arrayElemAt": ["$war_inventory_docs",0]
			}
	}
},{
	"$replaceRoot": {
		"newRoot": {
		"$mergeObjects": ["$war_inventory_docs", "$$ROOT"]
			}
	}
}
]

cursor=mycol.aggregate(pipeline)

for doc in cursor:
	print (doc['title'],doc['Quantity'])



