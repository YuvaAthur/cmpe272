from svr import app
from flask import Flask, jsonify, abort, make_response, request, render_template, flash,redirect
from flask_login import login_user, logout_user, current_user, login_required, login_manager
from werkzeug.urls import url_parse
from svr.forms import LoginForm, RegistrationForm

# from db.dbops import books, customers, orders, inventory
# from svr.models import AppDB

# #for testing
from . import db_data


# # for rendering user name
user = {'username': 'Miguel'}
# initdb = AppDB()    # initializes to Mongo DB : For testing use Mongo Mock
# appdb = initdb.db


@app.route('/')                 #decorator mapping root call
@app.route('/index')            #decorator mapping /index call
def index():
    return render_template('index.html', title='Home', user=user)
        # return "Hello, welcome to the Web Server of team  Warriors"

#for testing purposes
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        print("routes::login login form has data")
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
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
@app.route('/api/v1.0/books', methods=['GET'])
def get_books():
    books = db_data.sample_books  # books.get_available_books()   #
    return jsonify({'books': books})

#GET books/isbn: returns a JSON object with the details of the book identified by ISBN, including number of copies available.
@app.route('/api/v1.0/books/<string:isbn>', methods=['GET'])
def get_book(isbn):             #unique - should return ONLY one book
    books = db_data.sample_books
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
    newOrderId = db_data.sample_orders[-1]['id'] + 1
    db_data.sample_orders.append(
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
            db_data.sample_orderitems.append(
                {
                    'id': db_data.sample_orderitems[-1]['id'] + 1,
                    'orderid': newOrderId,
                    'bookid' : book["bookid"],
                    'orderqty': book["qty"]
                }
            )
    # return jsonify (db_data.sample_orderitems),201
    print (db_data.sample_orderitems)
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


