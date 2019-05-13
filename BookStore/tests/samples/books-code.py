import unittest
import mongomock
import json
import list_books

class DBTests(unittest.TestCase):
    def setUp(self):
        self.db = mongomock.MongoClient()['testdb']
        self.db.books.insert_one({'_id': '1', 'title': 'A test book'})
        self.db.books.insert_one({'_id': '2', 'title': 'Another test book'})
        self.db.books.insert_one({'_id': '3', 'title': 'A rare book'})
        self.db.inventory.insert_one({'_id': '1', 'id': '1', 'qty': 5})
        self.db.inventory.insert_one({'_id': '2', 'id': '2', 'qty': 0})
 
    def tearDown(self):
        pass

    def test_get_available_books(self):
        books = list_books.get_available_books(self.db)
        self.assertEqual(len(books), 1)
        print(books)

if __name__ == '__main__':
    unittest.main()

