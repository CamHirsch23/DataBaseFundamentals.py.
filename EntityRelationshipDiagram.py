# Define the entities and relationships for the "BookHaven" database

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        # One-to-Many relationship: One author can write multiple books
        self.books = []

class Book:
    def __init__(self, id, title, author_id, isbn, publication_date, price, available=True):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.price = price
        self.available = available
        # Many-to-Many relationship with Transactions through Books_Transactions
        self.transactions = []

class Customer:
    def __init__(self, id, name, address, email):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        # One-to-Many relationship: One customer can place multiple transactions
        self.transactions = []

class Transaction:
    def __init__(self, id, customer_id, transaction_date, total_price):
        self.id = id
        self.customer_id = customer_id
        self.transaction_date = transaction_date
        self.total_price = total_price
        # Many-to-Many relationship with Books through Books_Transactions
        self.books = []

class BooksTransactions:
    def __init__(self, book_id, transaction_id, quantity):
        self.book_id = book_id
        self.transaction_id = transaction_id
        self.quantity = quantity
        # This is a linking class for the Many-to-Many relationship between Books and Transactions

# Example of creating instances and linking them
author = Author(id=1, name='J.K. Rowling')
book = Book(id=1, title='Harry Potter and the Sorcerer\'s Stone', author_id=author.id, isbn='978-0439708180', publication_date='1997-06-26', price=19.95)
author.books.append(book)

customer = Customer(id=1, name='John Doe', address='123 Elm Street', email='john.doe@example.com')
transaction = Transaction(id=1, customer_id=customer.id, transaction_date='2024-07-24', total_price=19.95)
customer.transactions.append(transaction)

books_transaction = BooksTransactions(book_id=book.id, transaction_id=transaction.id, quantity=1)
book.transactions.append(books_transaction)
transaction.books.append(books_transaction)

# Note: This code is for illustrative purposes and does not interact with an actual database.
