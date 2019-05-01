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
1. list_books.py : Code to be tested
    * using Inventory Collection, aggregate available books into Books.Qty
    * Function: `get_available_books`
2. books-code.py: Test Script
    * uses mongomock to simulate mongo db
    * SetUp: adds documents into books and inventory collection
    * test_ : calls `get_available_books`
    


