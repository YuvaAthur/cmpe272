import sys
import pymongo
from pprint import pprint



def add_inv(db,inv_rec1):
	collection=db['DATABASE.INVENTORY']
	insert_inv=collection.insert_one(inv_rec1)
	return(insert_inv)

def list_inv(db):
	collection=db['DATABASE.INVENTORY']
	return (collection)


def del_inv(db,invid):
	collection=db['DATABASE.INVENTORY']
	return (collection.delete_one({ "_id": invid }))





if __name__ == "__main__":
	argv = sys.argv
	if len(argv) < 2:
		print("Usage: python add_invomer.py mongodb_uri")
		exit(-1)

	mongodb_uri = argv[1]

	db = pymongo.MongoClient(mongodb_uri).get_database()

	for order in create_order(db):
	  print("Order Created --",invomer['FirstName'])
