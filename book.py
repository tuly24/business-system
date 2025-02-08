class Book:
    def __init__(self, title, author, genre, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

books_inventory = []

def add_book(title, author, genre, price):
    new_book = Book(title, author, genre, price)
    books_inventory.append(new_book)
    print(f"Book '{title}' added successfully!")

def list_books():
    if not books_inventory:
        print("No books available in the inventory.")
    for book in books_inventory:
        print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Price: {book.price}")
