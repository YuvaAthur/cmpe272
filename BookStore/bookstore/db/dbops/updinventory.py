import sys
import pymongo
from pprint import pprint

# TODO: This function needs to be checked
def fulfill_order(db,order_id):
	collection=db["inventory"]
	collection2=db["orders"]
	collection3=db["order_lines"]	
	for item in (collection3.find({"OrderID" : order_id})):  # find line items with order ID
		for avail in (collection.find_one({"id" : item.BookID})): # find inventory value for one book
			#pprint(avail.qty)
			return avail.Qty								# have to create an aggregated JSON for each book



if __name__ == "__main__":
	argv = sys.argv
	if len(argv) < 2:
		print("Usage: python add_customer.py mongodb_uri")
		exit(-1)

	mongodb_uri = argv[1]

	db = pymongo.MongoClient(mongodb_uri).get_database()

	for order in create_order(db):
	  print("Order Created --",customer['FirstName'])
