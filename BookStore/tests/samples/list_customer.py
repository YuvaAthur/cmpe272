import sys
import pymongo


def get_available_customer(db):
    cursor=db.customer.find()
    for customer in cursor:
    	print(customer)

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: python list_customer.py mongodb_uri")
        exit(-1)

    mongodb_uri = argv[1]
    
    db = pymongo.MongoClient(mongodb_uri).get_database()
    for customer in get_available_customer(db):
        print(customer-FirstName ['FirstName'], LastName ['LastName'], Address ['address'])


