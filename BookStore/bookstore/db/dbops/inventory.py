import sys
import pymongo
from pprint import pprint



def add_inv(db,inv_rec1):
	collection=db['db.INVENTORY']
	insert_inv=collection.insert_one(inv_rec1)
	return(insert_inv)

def list_inv(db):
	collection=db['db.INVENTORY']
	return (collection)


def del_inv(db,invid):
	collection=db['db.INVENTORY']
	return (collection.delete_one({ "_id": invid }))


# TODO: This function needs to be checked
def fulfill_order(db,order_id):
	inventory=db[INVENTORY]
	orders=db[ORDERS]
	order_lines=db["order_lines"]	
	for item in (order_lines.find({"OrderID" : order_id})):  # find line items with order ID
		for avail in (inventory.find_one({"id" : item.BookID})): # find inventory value for one book
			newvalues = { "$set": { "Quantity": avail.Quantity - 1 } }
			print(avail.Quantity)
	return 						# have to create an aggregated JSON for each book



if __name__ == "__main__":
	argv = sys.argv
	if len(argv) < 2:
		print("Usage: python add_invomer.py mongodb_uri")
		exit(-1)

	mongodb_uri = argv[1]

	db = pymongo.MongoClient(mongodb_uri).get_database()

	for order in create_order(db):
	  print("Order Created --",invomer['FirstName'])
