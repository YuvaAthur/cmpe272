# Yuva's notes

## Guru's words:
* ``` https://github.com/pallets/flask/tree/1.0.2/examples/tutorial ```
*  ```http://flask.pocoo.org/docs/1.0/tutorial/#tutorial```


## Source Directory
* Placed under CMPE272. Might move it later.
    * /Flaskr
    * Copied every file in the file structure using ```Ctrl-C/Ctrl-V``` ! =( !!
* Set up virtual python environment for Flaskr
``` python3 -m venv venv```
```. venv/bin/activate```
```pip install --upgrade pip```
```pip install -U Flask```

```export FLASK_APP=flaskr```
```export FLASK_ENV=development```
```flask run```


* Step1 :  ```http://flask.pocoo.org/docs/1.0/tutorial/factory/``` has to work
    * added ```@app.route('/')``` to get to root URL 
        * Local/Single route - for testing purposes
    * Works

* Step 2:  Fix DB issues with SQLite
    * from command line (after setting FLASK_APP, FLASK_ENV)
        * ``` flask init-db ```
    * Bug was in name of .sql file --> should be ```schema.sql```
    * Basic screen is now visible

* Step 3: Blueprints & Views
    * Views are registered into Blueprint
    * Blueprint is registered with app when available from App Factory

* Step 4: User Management
    * ```/register``` checks for existence of user in DB
        * If yes --> redirect to ```/login```
        * If no --> get new user name, save password as hash
    * ```/login``` success
        * ```session['user_id'] = user['id']```
            * ```session``` preserves state across requests
            * ```g``` needs to be updated with  user record using ```session['user_id']```
    * ```login_required```
        * decorator that can be used to intercept (like Aspect Oriented Programming) user calls
        * forces login even if route is hacked
    * Queries with parameters
        * The database library will take care of escaping the values to prevent SQL injection attack.
    
* Step 5: Unit Tests
    * ``` pip install pytest coverage```



## Deploy to Production
* Ref: http://flask.pocoo.org/docs/1.0/tutorial/deploy/ 
    * ``` pip install wheel```
    * ``` python setup.py bdist_wheel ```
        * Will generate file in ``` dist/flaskr-1.0.0-py3-none-any.whl ``` 
    * Installation
        * Copy to new machine
        * Set up venv
        * ``` pip install flaskr-1.0.0-py3-none-any.whl```
        * ``` export FLASK_APP=flaskr```
        * ``` flask init-db ```
    * Instance folder is created in a different location
        * ``` venv/var/flaskr-instance ``` <-- This is why SECRET is placed in this folder>
    * Configure secret
        * ``` python -c 'import os; print(os.urandom(16))' ```
        * In ``` venv/var/flaskr-instance/config.py```
            * ``` SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/' ```
    * Use Production Server
        * ``` Werkzeug ``` is for development/debug purposes
        * ``` pip install waitress ```
        * ``` waitress-serve --call 'flaskr:create_app' ```

## Deploy on AWS Elastic Beanstalk
* Ref: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html 




## Miscellaneous info
* Fix:  ```sqlite3.OperationalError: no such table: post``` in ```blog.py```
    * Ref: https://stackoverflow.com/questions/28126140/python-sqlite3-operationalerror-no-such-table
````
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "PupilPremiumTable.db")
with sqlite3.connect(db_path) as db:
````



