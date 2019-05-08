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

 


