from app import app

# This is *NOT* consistent with DB Schema

app.books = [
    {
        'id': 1,
        'title': u'The New And Improved Flask Mega-Tutorial',
        'author': u'Miguel Grinberg',
        'isbn': '978-1977051875',
        'qty': '50'
    },
    {
        'id': 2,
        'title': u'Learning Flask Framework',
        'author': u'Miguel Grinberg',
        'isbn': '978-1783983360',
        'qty': '105'
    },
    {
        'id': 3,
        'title': u'Mastering Flask Web Development: Build enterprise-grade, scalable Python web applications, 2nd Edition',
        'author': u'Daniel Gaspar',
        'isbn': '978-1788995405',
        'qty': '75'
    }
]


app.customer = [
    {
        'id':1,
        'fname':'First',
        'lname':'Customer'
    }
]

app.orders = [
    {
        'id': 1,
        'customerid': 1
    }
]

app.orderitems = [
    {
        'id': 1,
        'orderid': 1,
        'bookid': 1,
        'orderqty' : 1
    },
    {
        'id': 2,
        'orderid': 1,
        'book': 2,
        'orderqty' : 2
    }
]

## Pradeep Data Model

app.porders = [
    {
        'id': 1,
        'customerid': 1,
        'status':'Fulfiled',
        'isbn': '978-1977051875',
        'quantity': 1
    },
    {
        'id': 2,
        'customerid': 1,
        'status':'Created',
        'isbn': '978-1977051875',
        'quantity': 1
    }

]

app.pbooks = [
    {
        'id': 1,
        'title': u'The New And Improved Flask Mega-Tutorial',
        'author': u'Miguel Grinberg',
        'isbn': '978-1977051875',
        'quantity': '50'
    },
    {
        'id': 2,
        'title': u'Learning Flask Framework',
        'author': u'Miguel Grinberg',
        'isbn': '978-1783983360',
        'quantity': '105'
    },
    {
        'id': 3,
        'title': u'Mastering Flask Web Development: Build enterprise-grade, scalable Python web applications, 2nd Edition',
        'author': u'Daniel Gaspar',
        'isbn': '978-1788995405',
        'quantity': '75'
    }
]

