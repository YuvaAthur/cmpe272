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
(venv) $ export FLASK_APP=WebServer.py
(venv) $ sudo bash
(venv) root $ . venv/bin/activate
(venv) root $ flask run --host=0.0.0.0 --port=80
```

### Set up REST API Server in Flask
* Ref: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask 
* Running Flask in Debug Mode
* Debug mode for Flask App
* `export FLASK_APP=WebServer`
* `export FLASK_ENV=development`
* `flask run`

