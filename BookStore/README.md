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
* Declare packages by placing empty __init__.py in that directory
* Setting path in test files
    * Create context.py to place repo path as first in the path search
    * Import with appropriate paths
    * `from .context import bookstore # needed by pytest & therefore travis`
    * `from bookstore.db.dbops.add_customer import add_cust`
* run `pytest` to validate path navigation (useful for debugging)

### Debugging Travis CI
* Ref: https://stackoverflow.com/questions/21053657/how-to-run-travis-ci-locally
* Pull docker ci-ruby image: 
* `sudo docker pull travisci/ci-ruby:packer-1494868441`
* `docker run -it travisci/ci-ruby:packer-1494868441 /bin/bash`
* `su - travis`
* Clone git repository to root
* Ref: https://stackoverflow.com/questions/9443927/git-clone-into-home-directory/9444352
* `cd ~`
* `git init`
* `git remote add origin https://github.com/YuvaAthur/cmpe272.git`
* `git pull origin master`
* `sudo pip install -r requirements.txt`
* `pytest`
* Result: 
    * ALWAYS Travis yaml in the root
    *   pytest discovers test cases in the directory structure
    *   so if pytest runs from repository root, Travis should work right!
    * Correct version numbers in requirements.txt since pip install fails otherwise

* Central Travis CI build + test now works!! Yay!!

 


