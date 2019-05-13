import sys
import pymongo


def list_orders(db):
	orders=db['db.ORDERS']
	return (orders)

def create_order(db,customer_id,book_list):
	orders=db["db.ORDERS"]
	order_lines=db["db.ORDER_LINES"]	
	# begin transaction
	ret=orders.insert_one({"CustomerID" : customer_id})
	order_id=(ret.inserted_id)
	for b in book_list:
		order_lines.insert_one({"OrderID" : order_id, "BookID" : b["id"], "Quantity" : b["qty"]})
	return({"OrderID": order_id, "NumOrderLines" : len(book_list)})	
	# end transacton

# def del_order(db,orderid):
# 	orders=db['db.ORDERS']
# 	order_lines=db["db.ORDER_LINES"]	
# 	# begin transaction
# 	del1 = order_lines.remove({"OrderID" : order_id)})
# 	del2 = orders.delete_one({ "_id": orderid })
# 	return ("RemoveOrderLines": del1.nRemoved, "DeleteOrder": del2.deletedCount)
# 	# end transacton

if __name__ == "__main__":
	argv = sys.argv
	if len(argv) < 2:
		print("Usage: python add_customer.py mongodb_uri")
		exit(-1)

	mongodb_uri = argv[1]

	db = pymongo.MongoClient(mongodb_uri).get_database()

	for order in create_order(db):
	  print("Order Created --",customer['FirstName'])
