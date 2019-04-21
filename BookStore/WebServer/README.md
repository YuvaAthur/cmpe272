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

### Deployment
* Setup venv
```
$ python3 -m venv venv
$ . venv/bin/activate
```

* run flask process in venv


```
(venv) $ export FLASK_APP=WebServer.py
(venv) $ sudo bash
(venv) root $ . venv/bin/activate
(venv) root $ flask run --host=0.0.0.0 --port=80
```
