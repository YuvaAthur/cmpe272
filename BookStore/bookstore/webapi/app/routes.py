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
# details['booklist'] = ['customerid':1,'booklist':{{'bookid':1,'qty':1},{'bookid':1,'qty':1}}]
@app.route('/api/v1.0/orders', methods=['GET','POST'])
def add_order(): 
    if not request.json : #or not 'customerid' in request.json:
        abort(400) # Bad Request error

    details = request.json
    if not all([details.get('title'), details.get('customerid')]):
        error = json.dumps({'error': 'Missing field/s (title, customerid)'})
        return json_response(error, 400)


    # append order first
    newOrderId = app.orders[-1]['id'] + 1
    app.orders.append(
         {
        'id': newOrderId,
        'customerid': request.json['customerid']
        }
    )
    #append order items 
    booklist = details['booklist']
    orderitems = []
    if(0 < len(booklist)): 
        for book in booklist:
            orderItems.append(
                {
                    'id': app.orderitems[-1]['id'] + 1,
                    'orderid': newOrderId,
                    'bookid': book.id,
                    'orderqty': book.qty
                }
            )
    return jsonify({'orderid': newOrderId}), 201

# def order_create():
#     if request.content_type != JSON_MIME_TYPE:
#         error = json.dumps({'error': 'Invalid Content Type'})
#         return json_response(error, 400)
#     data = request.json
#     if not all([data.get('title'), data.get('customerid')]):
#         error = json.dumps({'error': 'Missing field/s (title, customerid)'})
#         return json_response(error, 400)

    


#PUT orders/number: "fulfills the order" - i.e. adjusts the inventory to account for the books shipped for this order.