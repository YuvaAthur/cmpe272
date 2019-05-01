import sys
import pymongo


def get_available_books(db):
    available_books = []
    for record in db.inventory.find({}):
        book_id = record['id']
        qty = record['qty']
        if qty <= 0:
            continue
        book = db.books.find_one({'_id': book_id})
        book['qty'] = qty
        available_books.append(book)
    return available_books

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: python list_books.py mongodb_uri")
        exit(-1)

    mongodb_uri = argv[1]
    
    db = pymongo.MongoClient(mongodb_uri).get_database()
    for book in get_available_books(db):
        print(book['title'], book['qty'])