# CMPE 272 - Enterprise SW Platforms
Progressive Project for CMPE272 
Team Warriors 
Team Members:
* Pradeep 
* Sanjeevi
* Senthil
* Yuva

## WebServer
### Purpose 
WebServer of Books Store

## Database
### Purpose
Python scripts to create collections in MongoDB


### Reference
Reference [MicroBlog](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) - Building a Simple Web Server using Flask

### Built With
* [Flask](https://www.palletsprojects.com/) - The web framework used

### Local Deployment

* Setup venv : good for local multi-library version development/testing 
```
$ python3 -m venv venv
$ . venv/bin/activate
```

* Install pre-requisites
```
(venv) $ pip3 install flask
(venv) $ pip3 install pprint"
(venv) $ pip3 install bson"    
(venv) $ pip3 install mongomock"
(venv) $ pip3 install pymongo"  
(venv) $ pip3 install dnspython"
```

* run flask process in venv on port 80
```
(venv) $ export FLASK_APP=web_server.py
(venv) $ sudo bash
(venv) root $ . venv/bin/activate
(venv) root $ flask run --host=0.0.0.0 --port=80
```

### Set up REST API Server in Flask
* Ref: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask 
* Running Flask in Debug Mode
* Debug mode for Flask App
* `export FLASK_APP=web_server`
* `export FLASK_ENV=development`
* `flask run`


### Unit Testing API end points
* Exploring creating RESTful Services
    * Ref: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
    * Self-contained web_server.py
    * include dummy data for tests
    * use flask_testing for unit tests

* Structure of Web Server project for complex app
    * Ref: http://exploreflask.com/en/latest/organizing.html
        * Ref: Example: https://github.com/nicolewhite/neo4j-flask 
    * Restructuring test code above as follows
        * trial/ : contains code of previous testing experiement
        * following dir structure as recommended in Ref
            * /config.py : for configuration settings
            * /app/__init__.py : Flask application initialization
            * /instance/config.py : Ignoring for now 

### Implementing POST Method
* Ref: https://github.com/rmotr/flask-api-example/blob/master/api/_03_post_method.py
* Debugging POST method
    * Go for JSON Data:
        * ```details = request.json ```
        * In Postman send data in BODY Tab corresponding to JSON structure expected.
````
{
	"customerid" : 1,
	"booklist" : [
		{ "bookid": 1, "qty":1}
		
		]
}
````
* Unit Test approach 
    * Set up headers in SetUp call :
        * ``` self.headers = {'Content-type': 'application/json'} ```
    * Pass a well formed JSON to Flask-Testing Client.
        * ```BASE_ORDER_URL = 'http://127.0.0.1:5000/api/v1.0/orders' ```
        * ```response = self.client.post(BASE_ORDER_URL, headers=self.headers, data=json.dumps(custorder)) ```

    * Test for 
        * HTTP Error
        * Functional Error

### Creating HTML Tempaltes
* Ref: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates 
* Make template
    * ```/app/templates/index.html ```
````
<html>
    <head>
        <title> CME272 Warriors </title>
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
        <h1> Welcome to CMPE 272 (2019) Warrior's Bookstore </h1>
    </body>
</html>
````
* In routes.py
    * ``` from flask import render_template ```
    * Add dummy user ``` user = {'username': 'Miguel'} ```
    * to /index add:
````
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)
````
* Adding Navigation bar
    * Ref: https://code.tutsplus.com/tutorials/templating-with-jinja2-in-flask-essentials--cms-25571
    * 
* Run Flask ```flask run```
### Adding Flask-WTF 
* Ref: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms 
* Flask-WTF : 
    * With WTForms, your form field HTML can be generated for you, but we let you customize it in your templates. This allows you to maintain separation of code and presentation, and keep those messy parameters out of your python code. Because we strive for loose coupling, you should be able to do that in any templating engine you like, as well.
    * the Flask-WTF extension, which is a thin wrapper around the WTForms package that nicely integrates it with Flask.
    * ``` pip install flask-wtf ```
* Add more configuration items in config.py
* Add /app/forms.py
````
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
````
* Add app/templates/base.html
````
<html>
    <head>
      {% if title %}
      <title>{{ title }} - CME272 Warriors</title>
      {% else %}
      <title>CME272 Warriors</title>
      {% endif %}
    </head>
    <body>
        <div>Warriors Bookstore: <a href="/index">Home</a></div>
        <hr>
        {% block content %}{% endblock %}
    </body>
</html>
````
* Adapt app/templates/index.html
````
{% extends "base.html" %}

{% block content %}
    <h1>Hi, {{ user.username }}!</h1>
<!----   {% for post in posts %}
    <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
    {% endfor %}
-->
{% endblock %}
````
* Add app/templates/login.html
````
{% extends "base.html" %}

{% block content %}
    <h1>Sign In</h1>
    <form action="" method="post" novalidate>
        {{ form.hidden_tag() }}
        <p>
            {{ form.username.label }}<br>
            {{ form.username(size=32) }}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}
        </p>
        <p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
        <p>{{ form.submit() }}</p>
    </form>
{% endblock %}
````
* Adapt /app/routes.py
````
from app.forms import LoginForm

# ...

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
````
* Add reference to base.html
    * ```     <a href="/login">Login</a>```
* Debugging Key Error
    * Ref: http://flask.pocoo.org/docs/0.12/patterns/wtforms/ 
    * Sample code:
```` /app/routes.py
# using example from http://flask.pocoo.org/docs/0.12/patterns/wtforms/
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
````
```` /app/forms.py
class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
````
```` /app/templates/register.html
{% from "_formhelpers.html" import render_field %}
<form method=post>
  <dl>
    {{ render_field(form.username) }}
    {{ render_field(form.email) }}
    {{ render_field(form.password) }}
    {{ render_field(form.confirm) }}
    {{ render_field(form.accept_tos) }}
  </dl>
  <p><input type=submit value=Register>
</form>
````

```` /app/templates/_formhelpers.html
{% macro render_field(field) %}
  <dt>{{ field.label }}
  <dd>{{ field(**kwargs)|safe }}
  {% if field.errors %}
    <ul class=errors>
    {% for error in field.errors %}
      <li>{{ error }}</li>
    {% endfor %}
    </ul>
  {% endif %}
  </dd>
{% endmacro %}

````
* Passing Secret Key
    * Ref: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
    * Sample Ref: https://flask-wtf.readthedocs.io/en/stable/quickstart.html
    * The form.hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks. All you need to do to have the form protected is include this hidden field and have the SECRET_KEY variable defined in the Flask configuration. If you take care of these two things, Flask-WTF does the rest for you.

    * FlaskForm from flask_wtf 
        * Only the flask-wtf extension has the special Form class which can handle CSRF automatically / other stuff.
        * Ref: https://stackoverflow.com/questions/19612186/forms-contactform-object-has-no-attribute-hidden-tag 
        * Add ```{{ form.hidden_tag() }}``` to .html template
        * Add ``` SECRET_KEY = "powerful secretkey"``` in config
        
    * Currently passing key is not working - defaulting to wtf Form approach 

* Fix for secret key
    * config.Config class is not working right
    * direct import of config file with ``` app.config.from_object('config')``` works
    * commented ```# csrf =  forms.CSRFProtect(app)``` in ```__init__.py```

### More Forms and navigations

* Requirements:
    * The front-end should allow customers to pick one or more books from the available ones 
    * and place an order for those books. 
    * Once an order is placed, the backend needs to simulate fulfilling the order (update the number of copies available for the ordered books).

* Book Order Form
    * ```books.html```
        * Check box for each item
            * Ref: https://coderwall.com/p/pkthoa/read-checkbox-in-flask 
        * Add Quantity Integer field 
````
<tr> 
    <td><input type="checkbox" id="id_{{book._id}}" name="ordered_books" value="{{book.isbn}}"> </td>
    <td align="left"><label for="id_{{book._id}}">{{book.title}}</label></td>                    
    <td align="center"><input type = "number" id="id_{{book._id}}" name="ordered_qty"}> </td>
</tr>
````
* Book selection + Quantity inputs
    * Implement ``` if form.validate_on_submit():```
    * Get Data from form:
        * ```ordered_books = request.form.getlist("ordered_books") ```
        * ```ordered_qty = request.form.getlist("ordered_qty") ```
        * ``` ordered_books ``` and ``` ordered_qty ``` are values in ```books.html```
    * flash the number of data points collected
        * Checkbox list returns only checked values
        * Input field with validation returns full list. 
    * TODO: Validate only books checked are ordered 
        * Idea complex to implement. HTML is tedious. 

* Change in UI Flow
    * (1) Select book.  (2) Place order, (3) Review Order, (4) Create/Confirm order. 
    * (1) Select book
        * Use checkbox to determine which books are selected
    * (2) Place order

## Admin flow : Fulfill order
* Fulfill Order: 
    * Admin should log in. 
    * List of Pending Orders available. 
    * Optional
        * Select Orders to fulfill. 
    * Confirm list. 
    * Make changes in DB.

## TODO : Continue and implement Fulfill order flow

## Using GraphQL to query MongoDB Schema
* Start with GraphQL code
```pip install flask-graphql```
""" routes.py
from flask_graphql import GraphQLView

app.add_url_rule(
    '/graphql', 
    view_func=GraphQLView.as_view(
        'graphql', 
        schema=schema, 
        graphiql=True
    )
)
""" 
* Needs Schema: Get from graphene mongo
```pip install graphene-mongo```
* Ref: https://bcb.github.io/python/graphql-flask 
* http://docs.graphene-python.org/en/latest/quickstart/#creating-a-basic-schema
    * Simple example works
    * Postman test
        * POST
            * ```http://127.0.0.1:5000/graphql```
            * raw body = ```query={hello}```
        * Response
            """
            {
               "data": {
                    "hello": "Hello stranger"
                }
            }
            """
* Get MongoDB Schema
    * Ref: https://jeffersonheard.github.io/python/graphql/2018/12/08/graphene-python.html 


## Working with Session Cookies : SSO Logout problem
* Issues:
    * Log-out of user is not logging user out.
    * Known Issue: https://github.com/puiterwijk/flask-oidc/issues/5#issuecomment-86187023 
    * Ref: https://flask-oidc.readthedocs.io/en/latest/ 
* Changes attempted 
    * On Okta server side: Reduced token validity time. 
        * Due to refresh on server side, this does not seem to work
    * On client side : Use Incognito Chrome mode 
        * Close browser to release cookies. 
* Interesting explorations:
    * Ref: https://blog.paradoxis.nl/defeating-flasks-session-management-65706ba9d3ce
    * Shows how Flask Session is managed
    * Offers ways to check for Flask vulnerabilities due to simple Secrets 




* Check point:
```` Debug code in routes.oy get_books call. 
# #        ordered_qty = request.form.getlist("ordered_qty") # value of orders 
#         # validate that checked book is the one for which order is being picked!
#         place_order = []
#             # flash('Number of different Quantities ordered {} '.format(len(ordered_qty)))
#         isbn_list = list(isbn_books)
#         flash('Number of isbn_books {} books_list {} '.format(len(isbn_list),len(books_list)))
#         for isbn in ordered_books:
#             # flash('Order for isbn {}'.format(isbn))
#             book = isbn_books.get(isbn)
#             i = 0
#             for k in isbn_list:
#                 if isbn == k:
#                     book['order_quantity'] = int(ordered_qty[i])
#                     flash('Quantity ordered isbn {} index {} value{}'.format(isbn,i,ordered_qty[i]))
#                     place_order.append(book)
#                 i += 1
#                     # if 0< int(ordered_qty[i]):
#                     #     print ('routes::get_books book ordered ',book.keys())
#                     #     book['order_quantity'] = int(ordered_qty[i])
#                     #     place_order.append(book)
#                     # i+=1
#         flash('Number of order lines {} '.format(len(place_order)))
#             # for book in place_order:
#             #     flash('isbn value {} quantity ordered {}'.format(book.isbn,book.order_quantity))

#             # flash('Number of different Books ordered {} '.format(len(ordered_books)))
#             # flash('Number of different Quantities ordered {} '.format(len(ordered_qty)))
#             # for isbn in ordered_books:
#             #         flash('isbn value {} '.format(isbn))
#             # for qty in ordered_qty:
#             #     if qty is not None :
#             #         flash('qty value {}'.format(qty))
#             # # print ('routes::get_books Number of different Books ordered ', len(ordered_books))
''''

# Adding 






### Authentication
* Ref: https://realpython.com/token-based-authentication-with-flask/ 



### Other explorations
* Ref: http://www.blog.pythonlibrary.org/2017/12/14/flask-101-adding-editing-and-displaying-data/ 
* ``` flask_table``` 
    * Needs strict table structure
    * Not useful for JSON rendering


 


