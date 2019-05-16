from svr import app
from flask import Flask, jsonify, abort, make_response, request, render_template, flash,redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required, login_manager
from werkzeug.urls import url_parse
from svr.forms import LoginForm, RegistrationForm, BookOrderForm

from context import db
from db.dbops import books, customers, orders, inventory
from svr.models import AppDB

# #for testing
from db.data import sample_data


# # for rendering user name
user = {'username': 'Miguel'}

# initializes to Mongo DB : For testing use Mongo Mock
initdb = AppDB()    
initdb.popsample()
appdb = initdb.db


@app.route('/')                 #decorator mapping root call
@app.route('/index', methods=['GET','POST'])            #decorator mapping /index call
def index():
    return render_template('index.html', title='Home', user=user)
        # return "Hello, welcome to the Web Server of team  Warriors"

#for testing purposes
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("routes::login login form has data")
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# using example from http://flask.pocoo.org/docs/0.12/patterns/wtforms/
@app.route('/register', methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        # db.session.add(user)
        # db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

## API List

#GET books: returns a JSON list with all the book details, including number of copies available.
@app.route('/api/v1.0/books', methods=['GET','POST'])
def get_books():
    form = BookOrderForm()
    isbn_books = books.get_available_books(appdb)  #sample_data.sample_books  # 
    books_list = list(isbn_books.values())
    # if(0== len(books)):      
    #     flash('No books available - data loaded?')
    # else:
    #     flash('Found {} books with quantity > 0 '.format(len(books))) 
    # return jsonify({'books': books})  # for debugging - raw dump to UI
    if form.validate_on_submit():
        ordered_books = request.form.getlist("ordered_books") # value of checkbox field
        ordered_qty = request.form.getlist("ordered_qty") # value of orders 
        # validate that checked book is the one for which order is being picked!
        place_order = []
        # flash('Number of different Books ordered {} '.format(len(ordered_books)))
        # flash('Number of different Quantities ordered {} '.format(len(ordered_qty)))
        isbn_list = list(isbn_books)
        flash('Number of isbn_books {} books_list {} '.format(len(isbn_list),len(books_list)))
        for isbn in ordered_books:
            # flash('Order for isbn {}'.format(isbn))
            book = isbn_books.get(isbn)
            i = 0
            for k in isbn_list:
                if isbn == k:
                    book['order_quantity'] = int(ordered_qty[i])
                    flash('Quantity ordered isbn {} index {} value{}'.format(isbn,i,ordered_qty[i]))
                    place_order.append(book)
                i += 1
            # if 0< int(ordered_qty[i]):
            #     print ('routes::get_books book ordered ',book.keys())
            #     book['order_quantity'] = int(ordered_qty[i])
            #     place_order.append(book)
            # i+=1
        flash('Number of order lines {} '.format(len(place_order)))
        # for book in place_order:
        #     flash('isbn value {} quantity ordered {}'.format(book.isbn,book.order_quantity))

        # flash('Number of different Books ordered {} '.format(len(ordered_books)))
        # flash('Number of different Quantities ordered {} '.format(len(ordered_qty)))
        # for isbn in ordered_books:
        #         flash('isbn value {} '.format(isbn))
        # for qty in ordered_qty:
        #     if qty is not None :
        #         flash('qty value {}'.format(qty))
        # # print ('routes::get_books Number of different Books ordered ', len(ordered_books))
        return redirect(url_for('index')) # to test URI change
    return render_template('books.html', title='Books Available to purchase', books=books_list,user=user, form=form)




#GET books/isbn: returns a JSON object with the details of the book identified by ISBN, including number of copies available.
@app.route('/api/v1.0/books/<string:isbn>', methods=['GET'])
def get_book(isbn):             #unique - should return ONLY one book
    books = sample_data.sample_books
    book = [book for book in books if book['isbn'] == isbn]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book})

#POST orders: takes as input a JSON object with the order details (customer and books) and returns an order number
# details['booklist'] = ['customerid':1,'booklist':[{'bookid':1,'qty':1},{'bookid':2,'qty':2}]]
# send data in the BODY of the API call - not Query Parameters!
@app.route('/api/v1.0/orders', methods=['POST'])
def add_order(): 

    print("routes::add_order POST -- start --")
    details = request.json 
    print("routes::add_order POST request", details)
    if not details: #or not 'customerid' in request.json:
        abort(400) # Bad Request error
    # return jsonify(details)

    # append order first
    newOrderId = sample_data.sample_orders[-1]['_id'] + 1
    sample_data.sample_orders.append(
         {
        '_id': newOrderId,
        'customerid': details['customerid']
        }
    )
    #append order items 
    booklist = details['booklist']
    # return jsonify(booklist)


    if(0 < len(booklist)): 
        for book in booklist:
            sample_data.sample_orderlines.append(
                {
                    '_id': sample_data.sample_orderlines[-1]['_id'] + 1,
                    'orderid': newOrderId,
                    'bookid' : book["bookid"],
                    'orderqty': book["qty"]
                }
            )
    # return jsonify (sample_data.sample_orderitems),201
    print (sample_data.sample_orderlines)
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


