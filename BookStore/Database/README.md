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
Scripts to create consistent collections in MongoDB


### Reference



### Deployment
* Install pre-requisites

```
$ pip3 install pymongo
$ pip3 install dnspython
```

* Insert Data into MongoDB Collections
Note: Have to have authorizations to do this operation on "mongodb+srv://cmpe272:cmpe272@cluster0-g5aa2.mongodb.net/test"
```
$ python3 cmpe272_books.py
$ python3 cmpe272_customers.py
$ python3 cmpe272_inventory.py
$ python3 cmpe272_order_lines.py
$ python3 cmpe272_orders.py
```
