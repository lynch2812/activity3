# Objective:

# Create a Python script that manages a library's inventory of books using lambdas, arrays, and simple OOP concepts.

#Instructions:

#1. Create a Book class with attributes for title, author, and availability.

#2. Use an array to store the library's collection of books.

#3 .Implement methods to add books, search for books by title or author, and update book availability using lambdas.


#4. Create instances of the Book class and test the functionality.

# This creates the class and the allows the specific details for the book to be accessed and modified later.

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []
    # adds a book to the library (an instance)
    def add_book(self, book):
        self.books.append(book)
    # finds all the books matching the given title 
    def search_by_title(self, title):
        # Use lambda to search for books by title
        search_title = lambda book: book.title.lower() == title.lower()
        return list(filter(search_title, self.books))
    # finds all the books matching the given author
    def search_by_author(self, author):
        # Use lambda to search for books by author
        search_author = lambda book: book.author.lower() == author.lower()
        return list(filter(search_author, self.books))
    # updates the availability  of a book by its title 
    def update_availability(self, title, available):
        # Use lambda to update book availability
        update_book = lambda book: setattr(book, 'available', available) if book.title.lower() == title.lower() else None
        list(map(update_book, self.books))

# Create instances of the Book class, these are the books available 
book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Structures and Algorithms", "Dave Jones")
book3 = Book("Web Development with Python", "John Smith")

# Create an instance of the Library class
library = Library()

# Add books to the library class above
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Search for books by title
print("Books with title 'Python Programming':")
for book in library.search_by_title("Python Programming"):
    print(f"- {book.title} by {book.author}") 

# Search for books by author- change authors name to search 
print("\nBooks by author 'Dave Jones':")
for book in library.search_by_author("Dave jones"):
    print(f"- {book.title} by {book.author}")

# Update book availability
library.update_availability("Data Structures and Algorithms", False)

# Check updated availability
print("\nAvailability of 'Data Structures and Algorithms':")
for book in library.search_by_title("Data Structures and Algorithms"):
    print(f"- {book.title} is {'available' if book.available else 'not in the library at present'}")

  


