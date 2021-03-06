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
Manage Cloud Instance Environment

### Creating AWS Ubuntu Instance
* Maximize on Free-eligible tier
* Image name: Ubuntu Server 18.04 LTS (HVM), SSD Volume Type 
* Size: t2.micro 1vCPU ; 1GB memory
* Storage : 30 GB 
* Connecting to Image
    * Ref: https://unix.stackexchange.com/questions/115838/what-is-the-right-file-permission-for-a-pem-file-to-ssh-and-scp 
        * See ssh-config.txt for more details
    * Ubuntu user is `ubuntu` : _don't replace with AWS user name_
    * `sudo apt-get update`
    * Ensure right security group that allows ssh access 
        * In case security group is right and port 22 error occurs, wait or reboot instance
* Set up environment for python3 / virtual env / Flask
    * Ref: https://vishnut.me/blog/ec2-flask-apache-setup.html 
    * `pip3 install virtualenv`
    * `mkdir flaskproject`
    * `cd flaskproject/`
    * `sudo apt install virtualenv`
    * `virtualenv venv`
        * `virtualenv --python=python3 venv` incase there is python conflict
    * `. venv/bin/activate`
* Test Flask
    * `vi app.py`
        * ```
        from flask import Flask
        app = Flask(__name__)

        @app.route('/')
        def hello_world():
            return 'Hello, World!'

        if __name__ == "__main__":
            app.run()
        ```
    * `export FLASK_APP=app.py`
    * `flask run --host=0.0.0.0 --port=80`
        * Ensure that port 80 connections are open on AWS side
        * port 80 is special - requires 2 additional steps
            * `sudo bash`
            * `. venv/bin/activate`
* Connect to <instance-public-ip>:80 for 'Hello World'
    * E.g. http://54.221.13.133:80 



=================================================================================


# Yuva's journey! : Useful information for others to explore 

### Creating AWS AMI Instance
* Image Name: Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type - ami-0080e4c5bc078760e
    * Free-eligible
* Details: The Amazon Linux AMI is an EBS-backed, AWS-supported image. The default image includes AWS command line tools, Python, Ruby, Perl, and Java. The repositories include Docker, PHP, MySQL, PostgreSQL, and other packages.
* Size: t2.micro 1vCPU ; 1GB memory : Free-eligible
* Storage : go for max allowed for Free-eligible
* Connecting to Image
    * Ref: https://unix.stackexchange.com/questions/115838/what-is-the-right-file-permission-for-a-pem-file-to-ssh-and-scp 
        * See ssh-config.txt for more details
        * For Amazon Linux AMI user is `ec2-user` : _don't replace with AWS user name_
    * `sudo yum update` 
* Trouble shooting if ssh is not connecting
    * Check security group settings to let ssh connections
    * Ref: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html 

### Set up docker container with pre-requisites 
* Working with Docker
    * Probably **not** required. Seems too round about!
* AWS Launch Templates are for implementing best practices
* AWS Batch is used for setting up compute environments for batch jobs - upto ECS Instance creation.
* Need to use Docker images to set up right environment
* Set up docker service in EC2 Instance SSH Terminal:
    ```
    sudo yum update -y
    sudo yum install -y docker
    sudo service docker start
    ```
* Pull relevant image from DockerHub
    * docker pull saptarshikar/pymongo

### Setup Python environment
* This can  become start-up script later.
    * For AWS put it into User Data of Instance
        * Ref: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html
    * In GCP add it as Startup Script
* Setup python :
```
$ sudo pip install --upgrade pip
* Ref: https://stackoverflow.com/questions/27669927/how-do-i-install-python-3-on-an-aws-ec2-instance 
$ sudo yum list | grep python3
$ sudo yum install python36-virtualenv.noarch
```
.noarch means applicable for all architectures

* Setup venv : good for local multi-library version development/testing 
```
$ python3 -m venv venv
$ . venv/bin/activate
```

* Install pre-requisites
    * Can be set as User Data of Instance as start-up script
```
(venv) $ pip3 install --upgrade pip
(venv) $ pip3 install flask
(venv) $ pip3 install pymongo  
(venv) $ pip3 install dnspython
(venv) $ pip3 install mongomock
(venv) $ pip3 install bson    
(venv) $ pip3 install pprint
```

* Test Flask
    * Ref: https://www.codementor.io/dushyantbgs/deploying-a-flask-application-to-aws-gnva38cf0 
```
$ mkdir testFlask
$ cd testFlask
$ cat > app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

^c (to exit)
$ cat app.py
$ export FLASK_APP=app.py
$ flask run --host=0.0.0.0 --port=80
```
Note: Flask defaults to 5000 which is typically blocked by EC2
    Option 1: Add incoming rule for port 5000
    Option 2: Launch on a different port
* app.run(debug=True, port=3000)

* Connect from remote place


* run flask process in venv on port 80


```
(venv) $ export FLASK_APP=WebServer.py
(venv) $ sudo bash
(venv) root $ . venv/bin/activate
(venv) root $ flask run --host=0.0.0.0 --port=80
```
