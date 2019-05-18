# To declare db package / module
from .dbops import customers
from .dbops import books
from .dbops import orders
from .dbops import popsample
from .dbops import inventory

# DB Names
DATABASE = "test_bookstore"
BOOKS = "books"
INVENTORY = "inventory" 
CUSTOMERS = "customers"
ORDERS = "orders"
ORDER_LINES = "order_lines"