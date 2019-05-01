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

* Test Scripts 

* * list_books.py : 
* * * using Inventory Collection, aggregate available books into Books.Qty
* * books-code.py: 
* * * uses mongomock to simulate mongo db
* * * adds documents into books and inventory collection
* * * tests available book count from list_books



