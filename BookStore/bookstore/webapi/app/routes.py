from app import app
from flask import jsonify, abort, make_response, request


#for testing
from app import routescode


@app.route('/')                 #decorator mapping root call
@app.route('/index')            #decorator mapping /index call
def index():
        return "Hello, welcome to the Web Server of team  Warriors"


#GET books: returns a JSON list with all the book details, including number of copies available.
@app.route('/api/v1.0/books', methods=['GET'])
def get_books():
    return jsonify({'books': app.books})

#GET books/isbn: returns a JSON object with the details of the book identified by ISBN, including number of copies available.
@app.route('/api/v1.0/books/<string:isbn>', methods=['GET'])
def get_book(isbn):             #unique - should return ONLY one book
    books = app.books
    book = [book for book in books if book['isbn'] == isbn]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book})

#POST orders: takes as input a JSON object with the order details (customer and books) and returns an order number
# details['booklist'] = ['customerid':1,'booklist':[{'bookid':1,'qty':1},{'bookid':2,'qty':2}]]
@app.route('/api/v1.0/orders', methods=['POST'])
def add_order(): 
    # data = request.get_json()
    # print (data)
    # return jsonify(data)
    # return jsonify(request.values)

    details = request.values
    if not request.values or not 'customerid' in request.values:
        abort(400) # Bad Request error
    # return jsonify(details)


    # append order first
    newOrderId = app.orders[-1]['id'] + 1
    app.orders.append(
         {
        'id': newOrderId,
        'customerid': details['customerid']
        }
    )
    #append order items 
    booklist = details['booklist']
    # return jsonify(booklist)


    if(0 < len(booklist)): 
        for book in booklist:
            app.orderitems.append(
                {
                    'id': app.orderitems[-1]['id'] + 1,
                    'orderid': newOrderId,
                    'bookid' : book,
                    'orderqty': book
                }
            )
    # return jsonify (app.orderitems),201
    return jsonify({'orderid': newOrderId}), 201



#Code written against MongoDB --> has to be adapted for JSON Collections!
#TODO: Needs to be fixed for JSON
#PUT orders/number: "fulfills the order" - i.e. adjusts the inventory to account for the books shipped for this order.
@app.route('/api/v1.0/order_fulfill/<int:order_id>', methods=['PUT'])
def fulfill_order(order_id):
    orders = app.porders
    books = app.pbooks
    order_index = order_id - 1

#    status = orders.getJSONObject(order_id).getJSONObject('status')
#json.getJSONArray("content").getJSONObject(0).getString("article")
#    status = orders[order_index].getString('status')
    status = orders[order_index].get('status')
    isbn = orders[order_index].get('isbn')
    quantity_ordered = orders[order_index].get('quantity')
    for book in books:
        if(isbn == book.get('isbn')):
            quantity_available = book.get('quantity')
            bookid = book.get('id')

    # quantity_available = books.getJSONObject(isbn).getJSONObject('quantity')
    if ("Created" == status):
        orders[order_index].update({'status':"Fulfilled"})
        # TODO: Have to update document
        # books[bookid].update({'quantity':(quantity_available-quantity_ordered)})


    return jsonify({'orderid': order_id, 'fulfilled': quantity_ordered}), 201


