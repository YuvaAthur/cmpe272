
from .test_db_base import DBTestsBase

from .context import bookstore # needed by pytest & therefore travis

from bookstore.db.dbops.customers import add_cust, list_cust, del_cust

# Ref: https://gist.github.com/twolfson/13f5f5784f67fd49b245
# refactoring 
class DBTests(DBTestsBase):
    def setUp(self):
        self.db = self.client[bookstore.db.DATABASE]
        self.cust_rec1 = { 
            "_id" : 5, 
            "FirstName" : "Apple", 
            "LastName" : "Seed", 
            "address" : {
                "street": "123 Fake Street", 
                "city": "Faketon", 
                "state": "MA", 
                "zip": "12345"
                } , 
            "contact" : {
                "phone" : "111-111-1111" , 
                "email" : "apple@test.com"
                } 
            }
        self.custid = 5

    def step1(self):
        ret = add_cust(self.db,self.cust_rec1)
        self.assertEqual(ret.inserted_id,self.custid)

    def step2(self):
        ret= list_cust(self.db)
        self.assertEqual(ret.find().count(),1)

    def step3(self):
        ret = del_cust(self.db,self.custid)
        self.assertEqual(ret.deleted_count,1)


# class DBTests(unittest.TestCase):
#     def setUp(self):
#         self.client = mongomock.MongoClient()
#         self.db = self.client[bookstore.db.DB]
#         self.cust_rec1 = { 
#             "_id" : 5, 
#             "FirstName" : "Apple", 
#             "LastName" : "Seed", 
#             "address" : {
#                 "street": "123 Fake Street", 
#                 "city": "Faketon", 
#                 "state": "MA", 
#                 "zip": "12345"
#                 } , 
#             "contact" : {
#                 "phone" : "111-111-1111" , 
#                 "email" : "apple@test.com"
#                 } 
#             }
#         self.custid = 5
# # Requirement: Execute in a specific order

#     def step1(self):
#         ret = add_cust(self.db,self.cust_rec1)
#         self.assertEqual(ret.inserted_id,self.custid)

#     def step2(self):
#         ret= list_cust(self.db)
#         self.assertEqual(ret.find().count(),1)

#     def step3(self):
#         ret = del_cust(self.db,self.custid)
#         self.assertEqual(ret.deleted_count,1)

#     def _steps(self):
#         for name in dir(self): # dir() result is implicitly sorted
#             if name.startswith("step"):
#                 yield name, getattr(self, name) 

#     def test_steps(self):
#         for name, step in self._steps():
#             try:
#                 step()
#             except Exception as e:
#                 self.fail("{} failed ({}: {})".format(step, type(e), e))

#     def tearDown(self):
#         pass

# Inidividual tests - have to be strung togethe anyway!

    # def test_cust_add(self):
    #     ret = add_cust(self.db,self.cust_rec1)
    #     self.assertEqual(ret.inserted_id,5)
    #     pass

    # def test_list_cust(self):
    #     self.test_cust_add() #test_cust_add(self)
    #     ret= list_cust(self.db)
    #     self.assertEqual(ret.find().count(),1)

    # def test_del_cust(self):
    #     self.test_list_cust()
    #     ret = del_cust(self.db,self.custid)
    #     self.assertEqual(ret.deleted_count,1)


# Suite approach - not working - needs to be debugged.\
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(DBTests.test_cust_add)
#     suite.addTest(DBTests.test_list_cust)
#     return suite

# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     print( "Running Main")
#     runner.run(suite())


