import sys 
import pymongo 

def add_cust(db,cust_rec1): 
    #print("add_customer::add_cust - Begin")
    #print (collection)
    insert_cust=db.customer.insert_one(cust_rec1) 
    print (insert_cust.inserted_id)
    #print("add_custoer::add_cust - End")
    return(insert_cust) 
    
if __name__ == "__main__": 
    argv = sys.argv 
    if len(argv) < 2: 
        print("Usage: python add_customer.py mongodb_uri") 
        exit(-1) 
    mongodb_uri = argv[1] 
    db = pymongo.MongoClient(mongodb_uri).get_database() 
    for customer in add_cust(db): 
        print("Customer Added --",customer['FirstName'])