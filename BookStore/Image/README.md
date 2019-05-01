# CMPE 272 - Enterprise SW Platforms
Progressive Project for CMPE272 
Team Warriors 
Team Members:
* Pradeep 
* Sanjeevi
* Senthil
* Yuva

## Image
### Purpose
Docker image for AWS deployment

### Creating AWS Instance
* Image Name: Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type - ami-0080e4c5bc078760e
    * Free-eligible
* Details: The Amazon Linux AMI is an EBS-backed, AWS-supported image. The default image includes AWS command line tools, Python, Ruby, Perl, and Java. The repositories include Docker, PHP, MySQL, PostgreSQL, and other packages.
* Size: t2.micro 1vCPU ; 1GB memory
    * Free-eligible
* Connecting to Image
    * Ref: https://unix.stackexchange.com/questions/115838/what-is-the-right-file-permission-for-a-pem-file-to-ssh-and-scp 
        * See ssh-config.txt for more details
        * For Amazon Linux AMI user is `ec2-user` : _don't replace with AWS user name_
    * `sudo yum update` 

### Set up docker container with pre-requisites




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
