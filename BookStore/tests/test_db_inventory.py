from .test_db_base import DBTestsBase

from .context import bookstore # needed by pytest & therefore travis

from bookstore.db.dbops.inventory  import add_inv, list_inv, del_inv

# Ref: https://gist.github.com/twolfson/13f5f5784f67fd49b245
# refactoring 
class DBTests(DBTestsBase):
    def setUp(self):
        self.db = self.client[bookstore.db.DB]

# Ref: https://gist.github.com/twolfson/13f5f5784f67fd49b245
# refactoring 
class DBTests(DBTestsBase):
    def setUp(self):
        self.db = self.client[bookstore.db.DB]
        self.inv_rec1 = { 
            "_id" : 5,
            "book_id" : 2, 
            "quantity" : 10
            }
        self.invid = 5

    def step1(self):
        print ("inventory::add_inv")
        ret = add_inv(self.db,self.inv_rec1)
        self.assertEqual(ret.inserted_id,self.invid)

    def step2(self):
        print ("inventory::list_inv")
        ret= list_inv(self.db)
        self.assertEqual(ret.find().count(),1)

    def step3(self):
        print ("inventory::del_inv")
        ret = del_inv(self.db,self.invid)
        self.assertEqual(ret.deleted_count,1)

