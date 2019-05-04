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

### Unit Testing 
* Use `pytest' 
    * Navigates to Test Directory
    * Executes test_xxxx.py files
    * Following code is *not* required in the test_ files
        * `# not required if running from pytest`	 
        * `# if __name__ == "__main__":`
        * `#    unittest.main()`
    * This removes need to update travis yaml file.
        * `script: pytest`
* Directory structure to keep code and test separate
    * /bookstore: Application code
        * Can have nested substructures
        * Add `__init__.py` to each directory - this informes Python that the directory corresponds to a module
    * /tests: Contains test code
        * Add `context.py` to set up right search path
            * Unit tests search for current durectory subtree for code
            * When app and tests are sibling directories, path has to be specified.
            * Following code adds parent directory in python loader search path
                * `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))`
                * `import bookstore`
        * Import code to test
            * `from .context import bookstore # needed by pytest & therefore travis`
            * `from bookstore.db.dbops.add_customer import add_cust`
* Testing DB Operations
    * Use `unittest` 
    * Set up dummy data, perform test, report test result, teardown
* Testing Flask API Server 
    * Use `flask_testing`
    * Assert on response object
* Test files
    * `pytest` reports on all `test_ ` methods in the `test_ .py` files
    * Travis reports on tests on every check-in
        * There seems to be an issue with responsiveness of Travis community edition.
        * Alternatively, we can trigger manually. 
        



