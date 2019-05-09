import sys
import pymongo


def list_orders(db):
	collection=db['db.ORDERS']
	return (collection)

def del_order(db,orderid):
	collection=db['db.ORDERS']
	
	return (collection.delete_one({ "_id": orderid }))


def create_order(db,customer_id,book_list):
	collection=db["orders"]
	collection2=db["order_lines"]	
	ret=collection.insert_one({"CustomerID" : customer_id})
	order_id=(ret.inserted_id)
	for b in book_list:
		collection2.insert_one({"OrderID" : order_id, "BookID" : b["id"], "Quantity" : b["qty"]})
	return({"OrderID": order_id, "NumItems" : len(book_list)})	

if __name__ == "__main__":
	argv = sys.argv
	if len(argv) < 2:
		print("Usage: python add_customer.py mongodb_uri")
		exit(-1)

	mongodb_uri = argv[1]

	db = pymongo.MongoClient(mongodb_uri).get_database()

	for order in create_order(db):
	  print("Order Created --",customer['FirstName'])
