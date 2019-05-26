from svr import app, oidc, okta_client
from flask import Flask, jsonify, abort, make_response, request, render_template, flash,redirect, url_for
from flask import current_app, g
from flask_login import login_user, logout_user, current_user, login_required, login_manager
from flask import session
from werkzeug.urls import url_parse
from svr.forms import LoginForm, RegistrationForm, BookOrderForm, QuantityOrderForm , ConfirmOrderForm

from context import db
from db.dbops import books, customers, orders, inventory
from svr.models import AppDB

# #for testing
from db.data import sample_data

# Schema for GraphQL



# # for rendering user name
user = {'username': 'Miguel'}


# initializes to Mongo DB : For testing use Mongo Mock
initdb = AppDB()    
initdb.popsample()
appdb = initdb.db


# # Minima GraphQL : https://bcb.github.io/python/graphql-flask 
# # Bug fix at : http://docs.graphene-python.org/en/latest/quickstart/#creating-a-basic-schema
# from graphene import ObjectType, String, Schema
# from flask_graphql import GraphQLView
# class Query(ObjectType):
#     hello = String(argument=String(default_value="stranger"))
#     def resolve_hello(self, info, argument):
#         return 'Hello ' + argument

# view_func = GraphQLView.as_view("graphql", schema=Schema(query=Query),graphiql=True)

# app.add_url_rule('/graphql', view_func=view_func)

# # Optional, for adding batch query support (used in Apollo-Client)
# # app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view('graphql', schema=schema, batch=True))


from oauth2client.client import OAuth2Credentials

@app.before_request
def before_request():
    if oidc.user_loggedin:
        # OpenID Token as 
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None

@app.route('/')                 #decorator mapping root call
@app.route('/index', methods=['GET','POST'])            #decorator mapping /index call
def index():
    return render_template('index.html', title='Home', user=user)
        # return "Hello, welcome to the Web Server of team  Warriors"

#for testing purposes
@app.route('/login', methods=['GET', 'POST'])
@oidc.require_login
def login():
    """
    Force the user to login, then redirect them to the get_books.
    """
    # form = LoginForm()
    # if form.validate_on_submit():
    #     print("routes::login login form has data")
    #     flash('Login requested for user {}, remember_me={}'.format(
    #         form.username.data, form.remember_me.data))
    #     return redirect(url_for('get_books'))
    # return render_template('login.html', title='Sign In', form=form)

    info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])
    id_token = OAuth2Credentials.from_json(oidc.credentials_store[info.get('sub')]).token_response['id_token']
    # flash('routes::login : User Token ID {}'.format(id_token))

    # Ref: https://blog.paradoxis.nl/defeating-flasks-session-management-65706ba9d3ce
    if 'logged_in' not in session:
        session['logged_in'] = False


    return redirect(url_for(".index"))

@app.route("/logout")
@oidc.require_login
def logout():
    """
    Log the user out of their account.
    """
    info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])
    id_token = OAuth2Credentials.from_json(oidc.credentials_store[info.get('sub')]).token_response['id_token']
    # logout_request = base_url + logout_url + str(id_token) + logout_redirect_url
    base_url = "http://localhost:5000/"
    logout_url =  url_for(".logout")
    logout_redirect_url =  url_for(".index")
    # logout_request = str(id_token) 
    logout_request = base_url + logout_url + str(id_token) + logout_redirect_url

    # flash('routes::logout : Congratulations, you have logged out!')
    oidc.logout()
    session.clear()
    # info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])
    # id_token = OAuth2Credentials.from_json(oidc.credentials_store[info.get('sub')]).token_response['id_token']
    # flash('routes::logout : User Token ID {}'.format(id_token))

    return redirect(logout_request) #     redirect(url_for(".index"))

# Not needed: Okta takes care of Sign up
# using example from http://flask.pocoo.org/docs/0.12/patterns/wtforms/
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     # if current_user.is_authenticated:
#     #     return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         # db.session.add(user)
#         # db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)

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
        checked_books = request.form.getlist("ordered_books") # value of checkbox field
        # flash('Number of different Books checked {} '.format(len(checked_books)))
        app.ordered_books=[]
        for isbn in checked_books:
            book = get_book(isbn)
            app.ordered_books.append(book)      
        return redirect(url_for('get_order')) # to test URI change
    return render_template('books.html', title='Books Available to purchase', books=books_list,user=user, form=form)


#GET POST: Choose number of books to orde
@app.route('/api/v1.0/order', methods=['GET','POST'])
def get_order():
    form = QuantityOrderForm()
    books_list = app.ordered_books  
    if form.validate_on_submit():
        ordered_qty = request.form.getlist("ordered_qty")
        i = 0
        for qty in ordered_qty:
            books_list[i]['quantity'] = int(qty)
            # flash ('routes::get_order book ordered {} quantity {}'.format(books_list[i]['title'],books_list[i]['quantity']))
            i += 1
        i = 0
        length = len(books_list)
        while i < length:
            if (0 == books_list[i]['quantity']):
                books_list.remove(books_list[i])
                length -= 1
                continue
            i += 1
        # flash ('routes::get_order book final order {}'.format(len(books_list)))        
        # return render_template('index.html', title='Home', user=user)
        return redirect(url_for('confirm_order'))
    return render_template('order.html', title='Choose quantity for selected books', books=books_list,user=user, form=form)

#GET POST: Confirm books ordered
@app.route('/api/v1.0/confirm', methods=['GET','POST'])
def confirm_order():
    form = ConfirmOrderForm()
    books_list = app.ordered_books
    ordered_qty = [] 
    if form.validate_on_submit():
        for book in books_list:
            flash ('Ordered: {} Quantity: {}'.format(book['title'],book['quantity']))
        # return render_template('index.html', title='Home', user=user) # for debugging flow
        return redirect(url_for('get_books'))
    return render_template('confirm.html', title='Confirm quantity for selected books', books_list=books_list,user=user, form=form)



#''''
#Search functions -------
#''''
#GET books/isbn: returns a JSON object with the details of the book identified by ISBN, including number of copies available.
@app.route('/api/v1.0/books/<string:isbn>', methods=['GET'])
def get_book(isbn):             #unique - should return ONLY one book
    books_list = books.get_available_books(appdb) # returns a dictionary
    book = books_list[isbn] 
    print ("routes::get_book(isbn) : found book", book)
    # book = [book for book in books_list if books_list['isbn'] == isbn]
    if 0 == len(book):
        abort(404)
    return book

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



# #Code written against MongoDB --> has to be adapted for JSON Collections!
# #TODO: Needs to be fixed for JSON
# #PUT orders/number: "fulfills the order" - i.e. adjusts the inventory to account for the books shipped for this order.
# @app.route('/api/v1.0/order_fulfill/<int:order_id>', methods=['PUT'])
# def fulfill_order(order_id):
#     orders = app.porders
#     books = app.pbooks
#     order_index = order_id - 1

# #    status = orders.getJSONObject(order_id).getJSONObject('status')
# #json.getJSONArray("content").getJSONObject(0).getString("article")
# #    status = orders[order_index].getString('status')
#     status = orders[order_index].get('status')
#     isbn = orders[order_index].get('isbn')
#     quantity_ordered = orders[order_index].get('quantity')
#     for book in books:
#         if(isbn == book.get('isbn')):
#             quantity_available = book.get('quantity')
#             bookid = book.get('id')

#     # quantity_available = books.getJSONObject(isbn).getJSONObject('quantity')
#     if ("Created" == status):
#         orders[order_index].update({'status':"Fulfilled"})
#         # TODO: Have to update document
#         # books[bookid].update({'quantity':(quantity_available-quantity_ordered)})


#     return jsonify({'orderid': order_id, 'fulfilled': quantity_ordered}), 201


