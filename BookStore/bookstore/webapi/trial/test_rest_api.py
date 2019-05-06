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
order = pymongo.collection.Collection(db,'orders')
customer = pymongo.collection.Collection(db,'customers')

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

@app.route('/create_order', methods=['POST'])
def add_order():

    isbn = request.json['isbn']
    quantity = request.json['quantity']
    customer = request.json['Customer_id']
    order_id = db.orders.find({},{order_id:1, _id: 0}).sort({order_id:-1} ).limit(1)+1

    #if isbn in db.books.find( { 'isbn': "isbn" }, { isbn: 1, _id: 0 } ) and quantity <= db.books.find( { 'isbn': "isbn" }, { quantity: 1, _id: 0 } ) and customer in db.customers.find( { 'Customer_id': "customer
" }, { Customer_id: 1, _id: 0 } )

    db.orders.insert({'order_id' : order_id, 'isbn' : isbn, 'quantity' : quantity, 'Customer_id' : Customer_id, 'Status': "Created" })

    return jsonify({'Order ID' : order_id})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
