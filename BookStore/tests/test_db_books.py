import unittest
import mongomock
import json


from .context import bookstore # needed by pytest & therefore travis

from bookstore.db.dbops.books import  add_book, list_book, del_book

from .test_db_base import DBTestsBase

class DBTests(DBTestsBase):
    def setUp(self):
        self.db = self.client[bookstore.db.DB]
        self.book_rec1 = { 
            "_id" : 4, 
            "title" : "Flex 3 in Action", 
            "isbn" : "1933988746", 
            "pageCount" : 576, 
            "publishedDate" : { 
                "date" : "2009-02-02T00:00:00.000-0800" 
                }, 
            "thumbnailUrl" : "https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/ahmed.jpg", 
            "longDescription" : "New web applications require engaging user-friendly interfaces   and the cooler, the better. With Flex 3, web developers at any skill level can create high-quality, effective, and interactive Rich Internet Applications (RIAs) quickly and easily. Flex removes the complexity barrier from RIA development by offering sophisticated tools and a straightforward programming language so you can focus on what you want to do instead of how to do it. And now that the major components of Flex are free and open-source, the cost barrier is gone, as well!    Flex 3 in Action is an easy-to-follow, hands-on Flex tutorial. Chock-full of examples, this book goes beyond feature coverage and helps you put Flex to work in real day-to-day tasks. You'll quickly master the Flex API and learn to apply the techniques that make your Flex applications stand out from the crowd.    Interesting themes, styles, and skins  It's in there.  Working with databases  You got it.  Interactive forms and validation  You bet.  Charting techniques to help you visualize data  Bam!  The expert authors of Flex 3 in Action have one goal   to help you get down to business with Flex 3. Fast.    Many Flex books are overwhelming to new users   focusing on the complexities of the language and the super-specialized subjects in the Flex eco-system; Flex 3 in Action filters out the noise and dives into the core topics you need every day. Using numerous easy-to-understand examples, Flex 3 in Action gives you a strong foundation that you can build on as the complexity of your projects increases.", 
            "status" : "PUBLISH", 
            "authors" : [ 
                "Tariq Ahmed with Jon Hirschi", 
                "Faisal Abid" 
                ], 
            "categories" : [ "Internet" ] 
            }
        self.bookid = 4

# Requirement: Execute in a specific order

    def step1(self):
        ret = add_book(self.db,self.book_rec1)
        self.assertEqual(ret.inserted_id,self.bookid)

    def step2(self):
        ret= list_book(self.db)
        self.assertEqual(ret.find().count(),1)

    def step3(self):
        ret = del_book(self.db,self.bookid)
        self.assertEqual(ret.deleted_count,1)


# Suite approach - not working - needs to be debugged.\
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(DBTests.test_book_add)
#     suite.addTest(DBTests.test_list_book)
#     return suite

# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     print( "Running Main")
#     runner.run(suite())


