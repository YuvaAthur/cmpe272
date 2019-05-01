# CMPE 272 - Enterprise SW Platforms
Progressive Project for CMPE272 
Team Warriors 
Team Members:
* Pradeep 
* Sanjeevi
* Senthil
* Yuva

## Database 
### Purpose 
Test scripts given by instructor for study purposes.


### Reference
https://sjsu.instructure.com/courses/1317745/assignments/4963332 


### Deployment
* Install pre-requisites

```
$ pip3 install pymongo
$ pip3 install dnspython
$ pip3 install unittest
$ pip3 install mongomock
$ pip3 install json

```
### Test Scripts 
1. `list_books.py` : Code to be tested
    * using Inventory Collection, aggregate available **books** collection into Books.Qty
    * Function: `get_available_books`
2. `books-code.py`: Test Script 
    * uses mongomock to simulate mongo db
    * SetUp: adds documents into **books** and **inventory** collection
    * test_ : calls `get_available_books`
3. `list_customer.py` : Code to be tested
    * Lists customers in **customer** collection
    * Function: `get_available_customer`
4. `customers-code.py`: Test Script 
    * uses mongomock to simulate mongo db
    * SetUp: adds documents into **customer** collection
    * test_ : calls `get_available_customer` 
5. `add_customer.py`: Exploring insert option
    * Given a customer record, insert into **customer** collection
6. `unit_test_insert_customer.py`: Test Script
    * Add a new customer record with specific ID and check after insert.

### Exploring Mongo Atlas operations
1. `explore_async_atlas.py`: Exploring async methods to connect to Mongo Atlas
    * uses `motor` and `tornado` libraries
2. `explore_join_atlas.py` : Exploring join constructs in MongoDB
    * create a pipeline that defines the programmatic logic
    * execute this on server side


    


