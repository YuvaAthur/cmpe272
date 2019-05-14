import sys
import pymongo

def pop_books(db,books):
	collection=db['db.BOOKS'] 
	ret=collection.insert_many(books)
	return(ret)

def pop_customers(db,cust):
	collection=db['db.CUSTOMERS'] 
	ret=collection.insert_many(cust)
	return(ret)

def pop_inventory(db,inv):
	collection=db['db.INVENTORY'] 
	ret=collection.insert_many(inv)
	return(ret)

def pop_orders(db,orders,orderlines):
	ordercol=db['db.ORDERS'] 
	lines=db['db.ORDER_LINES']
	ret1=ordercol.insert_many(orders)
	print("popsample::pop_orders len(orderlines) = ", len(orderlines))
	ret2=lines.insert_many(orderlines)
	return ({"num_orders": ret1.inserted_ids, "num_order_lines" : ret2.inserted_ids})	

if __name__ == "__main__":
	argv = sys.argv
	if len(argv) < 2:
		print("Usage: python add_customer.py mongodb_uri")
		exit(-1)

	mongodb_uri = argv[1]

	db = pymongo.MongoClient(mongodb_uri).get_database()

	for customer in add_cust(db):
	  print("Customer Added --",customer['FirstName'])
