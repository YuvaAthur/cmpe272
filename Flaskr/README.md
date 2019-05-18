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

* Step 2:  TODO : Fix DB issues with SQLite
    


* Fix:  ```sqlite3.OperationalError: no such table: post``` in ```blog.py```
    * Ref: https://stackoverflow.com/questions/28126140/python-sqlite3-operationalerror-no-such-table
````
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "PupilPremiumTable.db")
with sqlite3.connect(db_path) as db:
````



