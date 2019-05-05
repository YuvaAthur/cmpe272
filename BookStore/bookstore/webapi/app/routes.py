from app import app
from flask import jsonify, abort, make_response, request

#for testing
from app import routescode


@app.route('/')                 #decorator mapping root call
@app.route('/index')            #decorator mapping /index call
def index():
        return "Hello, welcome to the Web Server of team  Warriors"


@app.route('/api/v1.0/books', methods=['GET'])
def get_books():
    return jsonify({'books': app.books})

@app.route('/api/v1.0/books/<string:isbn>', methods=['GET'])
def get_book(isbn):             #unique - should return ONLY one book
    books = app.books
    book = [book for book in books if book['isbn'] == isbn]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book})
