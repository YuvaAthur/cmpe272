from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import pymongo
from bson.json_util import dumps
import json


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'warriors'
app.config['MONGO_URI'] = 'mongodb+srv://warriors:warriors@warriors-vc2w4.mongodb.net/test'

mongo = pymongo.MongoClient('mongodb+srv://warriors:warriors@warriors-vc2w4.mongodb.net/test', maxPoolSize=50, connect=False)

db = pymongo.database.Database(mongo,'warriors')
book = pymongo.collection.Collection(db,'books')
orders = pymongo.collection.Collection(db,'orders')
customers = pymongo.collection.Collection(db,'customers')

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Welcome to Warriors CMPE272 Bookstore'

@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify({'result' : json.loads(dumps(book.find().limit(5).sort("time", -1)))})

@app.route('/book/<isbn>', methods=['GET'])
def get_one_book(isbn):

    q = book.find_one({'isbn' : isbn})

    if q:
        output = {'isbn' : q['isbn'], 'No. of copies available' : q['quantity']}
    else:
        output = 'No results found'

    return jsonify({'result' : output})

@app.route('/orders', methods=['GET'])
def get_all_orders():
    return jsonify({'result' : json.loads(dumps(order.find().limit(5).sort("time", -1)))})

@app.route('/create_order', methods=['POST'])
def add_order():

    isbn = request.json['isbn']
    quantity = request.json['quantity']
    customer = request.json['Customer_id']
    order_id = orders.find({},{order_id:1, _id: 0}).sort({order_id:-1} ).limit(1)+1

if isbn not in book.find( { 'isbn': "isbn" }, { isbn: 1, _id: 0 } ):
        print("ISBN used is not valid")
elif  quantity > book.find( { 'isbn': "isbn" }, { quantity: 1, _id: 0 } ):
       print("Quantity is more than available copies. Update your quantity to be less than or equal to available copies")
elif customer in customers.find({'Customer_id':"customer"},{Customer_id: 1, _id:0}):
      print("Balance is below 0, add funds now or you will be charged a penalty.")
else:
    orders.insert({'order_id' : order_id, 'isbn' : isbn, 'quantity' : quantity, 'Customer_id' : Customer_id, 'Status': "Created" })
    print(order_id)
#return jsonify({'Order ID' : order_id})

@app.route('/order_fulfill/<order_id>', methods=['PUT'])
def fulfill_order(order_id):

    q = orders.find({'order_id': order_id,'Status' : "Created"}, {"Status":1, _id: 0 } )
    isbn = orders.find({'order_id': order_id,'Status' : "Created"}, {"isbn":1, _id: 0 } )
    current_qty = book.find({'isbn': isbn}, {"quantity":1, _id: 0 } )
    order_qty = orders.find({'order_id': order_id,'Status' : "Created"}, {"quantity":1, _id: 0 } )
    final_qty = current_qty['quantity'] - order_qty['quantity']

    if q:
        orders.updateOne({'order_id':order_id},{'Status':"Fulfilled"})
        book.updateone({'isbn': isbn'},{'quantity': final_qty})
    else:
        output = 'Order is either fulfilled or not found'

    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
