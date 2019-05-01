import sys
import pymongo
import pprint

def fulfill_order(db,order_id):
	collection=db["inventory"]
	collection2=db["orders"]
	collection3=db["order_lines"]	
	for item in (collection3.find({"OrderID" : "5"})):
		for avail in (collection.find_one({"id" : item.BookId})
			pprint.pprint(avail.qty)

	#ret=collection.insert_one({"CustomerID" : customer_id})
	#order_id=(ret.inserted_id)
	#for b in book_list:
	#	collection2.insert_one({"OrderID" : order_id, "BookID" : b["id"], "Quantity" : b["qty"]})
	#return({"OrderID": order_id, "NumItems" : len(book_list)})	



if __name__ == "__main__":
	argv = sys.argv
	if len(argv) < 2:
		print("Usage: python add_customer.py mongodb_uri")
		exit(-1)

	mongodb_uri = argv[1]

	db = pymongo.MongoClient(mongodb_uri).get_database()

	for order in create_order(db):
	  print("Order Created --",customer['FirstName'])
