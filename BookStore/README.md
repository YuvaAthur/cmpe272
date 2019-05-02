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

## Image
### Purpose
Cloud Instance Environment Management

### Reference
Reference [MicroBlog](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) - Building a Simple Web Server using Flask

### Built With
* [Flask](https://www.palletsprojects.com/) - The web framework used

### CI/CD with Travis CI
* Ref: https://stackify.com/top-continuous-integration-tools/ 
* Connect to Travi CI 
* Link to GitHub
* Connect to Git repository from Travis CI
    * E.g. https://travis-ci.org/YuvaAthur/cmpe272
* Activation: Checkin .travis.yml file into Git repository
* Constructs in .travis.yml
    * Structure Ref: https://github.com/discogs/pymongo-job-queue/blob/master/.travis.yml
    * Requirements.txt Ref: https://github.com/sjsu-cmpe-272-spring-2019/mongodb_utils 
        * use `pip list` to get the versions of libraries and use them
    * Script pytest Ref: https://github.com/kevchn/travis-ci-pytest 
        * Directory structure is important for pytest

### Project structure 
* Ref: https://www.learnpython.org/en/Modules_and_Packages 
    * Ref: best practice structure for .travis.yml
        * https://blog.ionelmc.ro/2014/05/25/python-packaging/#ci-templates-travis-yml
        * https://docs.python-guide.org/writing/structure/
 
* bookstore : package

