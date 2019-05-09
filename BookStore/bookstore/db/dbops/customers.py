import sys
import pymongo



def add_cust(db,cust_rec1):
	collection=db['db.CUSTOMERS']
	insert_cust=collection.insert_one(cust_rec1)
	return(insert_cust)

def list_cust(db):
	collection=db['db.CUSTOMERS']
	return (collection)


def del_cust(db,custid):
	collection=db['db.CUSTOMERS']
	return (collection.delete_one({ "_id": custid }))


# if __name__ == "__main__":
# 	argv = sys.argv
# 	if len(argv) < 2:
# 		print("Usage: python add_customer.py db record")
# 		exit(-1)

# 	mongodb_uri = argv[1]

# 	db = pymongo.MongoClient(mongodb_uri).get_database()

# 	for customer in add_cust(db):
# 	  print("Customer Added --",customer['FirstName'])
