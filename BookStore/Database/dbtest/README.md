# CMPE 272 - Enterprise SW Platforms
Progressive Project for CMPE272 
Team Warriors 
Team Members:
* Pradeep 
* Sanjeevi
* Senthil
* Yuva

## Database 
### Purpose 
Assignment 3: Setting up CI/CD to test data manipulation code


### Reference
TravisCI linked to GitHub: https://travis-ci.org/YuvaAthur/cmpe272 



### Deployment
* Activate CMPE272 Repository in TravisCI
* Follow instructions on https://docs.travis-ci.com/user/tutorial/ 

### Setting up Travis
* Update travis.yml with necessary steps to test code


### Testing requirements:
1. populate the sample data (eg. by importing it from some CSV files).
2. generate a list all the available books with the number of copies available for each.
3. add a new customer.
4. create a new order for this new customer with at least a couple of books.
5. update the inventory to reflect the order being fulfilled.

### Code & Test Scripts
1. populate the sample data (eg. by importing it from some CSV files).
    * `popsample.py` : `insert_many` into **customer** collection in `add_cust` method
    * `popsample-unittest.py` : creates multiple records and tests `add_cust`
2. generate a list all the available books with the number of copies available for each.
    * 


