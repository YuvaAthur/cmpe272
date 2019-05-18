import sys
import pymongo
import json


def list_orders(db):
	orders=db['DATABASE.ORDERS'] 
	return (orders)

def create_order(db,customer_id,book_list):
	orders=db["DATABASE.ORDERS"]
	newOrderId = 1 if (0 == orders.count_documents({})) else orders.count_documents({})  + 1
	print ("create_order::order id = ", newOrderId)
	order_lines=db["DATABASE.ORDER_LINES"]	
	# begin transaction
	ret=orders.insert_one({'_id':newOrderId, 'customer_id' : customer_id})
	print("create_order::order insert_one ret = ",ret.inserted_id)
	for b in book_list:
		newLineId = 1 if (0 == order_lines.count_documents({})) else order_lines.count_documents({}) + 1
		print ("create_order::new line id = ", newLineId)
		ret = order_lines.insert_one({'_id': int(newLineId), 'order_id' : newOrderId, 'book_isbn' : b['book_isbn'], "quantity" : b['quantity']})
		print("create_order::line insert_one ret = ",ret.inserted_id, " order_id = ", newOrderId, "book_isbn = ", b['book_isbn'], " quantity = ", b['quantity'])
	return ({"order_id": newOrderId, "num_order_lines" : len(book_list)})	
	# end transacton


def fulfill_order(db,order_id):
	inventory=db["DATABASE.INVENTORY"]
	books=db["DATABASE.BOOKS"]
	orders=db["DATABASE.ORDERS"]
	order_lines=db["DATABASE.ORDER_LINES"]	
	fulfilled_books = []
	for item in (order_lines.find({"order_id" : order_id})):  # find line items with order ID
		print("orders::fulfill_order item book_id = ", item['book_id'], " ; quantity = ", item['quantity'])
		for avail in (inventory.find({"book_id" : item['book_id']})): # find inventory value for one book
			print("orders::fulfill_order avail book_id = ", avail['book_id'], " ; quantity = ", avail['quantity'])
			new_quantity = avail['quantity'] - item['quantity'] 
			ret=inventory.update_one({
				'_id':avail['_id']
			},{
				'$set': { 
					'quantity': new_quantity
				}
			})
			print("orders::fulfill_order old value = ", avail['quantity'], " ; new value = ", new_quantity, " updated records = ",ret.modified_count)
			book = books.find_one({'_id': avail['book_id']})
			book['fulfilled_quantity']=item['quantity'] 
			fulfilled_books.append(book)
	return fulfilled_books # have to create an aggregated JSON for each book


# TODO: This function needs to be checked
def del_order(db,order_id):
	orders=db['DATABASE.ORDERS']
	order_lines=db["DATABASE.ORDER_LINES"]	
	# begin transaction
	del1 = order_lines.delete_many({'order_id' : order_id})
	print ("orders::del_order deleted ",del1.deleted_count," order_lines with order_id = ", order_id, "")
	del2 = orders.delete_one({ '_id': order_id })
	print ("orders::del_order deleted ",del2.deleted_count," orders with order_id = ", order_id, "")
	return ({'num_deleted_order': del2.deleted_count, 'num_removed_order_lines': del1.deleted_count}) 
	# end transacton


if __name__ == "__main__":
	argv = sys.argv
	if len(argv) < 2:
		print("Usage: python add_customer.py mongodb_uri")
		exit(-1)

	mongodb_uri = argv[1]

	db = pymongo.MongoClient(mongodb_uri).get_database()

	for order in create_order(db):
	  print("Order Created --",customer['FirstName'])
