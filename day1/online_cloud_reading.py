"""
Online Cloud book reading application similar to amazon kindle (for short stories).

A few thing to looking for:
- Users have a library of books that they can add to or remove from.
- Users can set a book from their library as active
- The reading application remembers where a user left off in a given book
- The reading application only displays a page of text at a time in the active book.
"""

"""
My own thought process:
Before of it, 
We have a cloud read application. that means:


Before anything, let's break the requirements into responsibilities:

So, We will have following components:
1. AppCloud (Our App) (Overall Wrapper)
2. Users 
    - id
    - username
3. Library:
    - id 
    - book_id
    - user_id 
    - last read page
    
4. Books ## Collection of books
    - id 
    - title
    - total page

"""

from dataclasses import dataclass, field
from typing import Dict
from uuid import uuid4


# Implementation
# Note: This is like a admin side. Client doesnt add book. The real owner does.


# ---------------------------- BOOK -------------------------------------
@dataclass
class Book:
    title: str
    total_page: int
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class Books:
    books: Dict[str, Book] = field(default_factory=dict)

    def add(self, book: Book):
        self.books[book.id] = book

    def update(self, id, book: Book):
        if not self.books.get(id):
            raise Exception("Book not found")
        self.books[id] = book

    def delete(self, id):
        if not self.books.get(id):
            raise Exception("Book not found")
        del self.books[id]

    def get_one(self, id: str):
        if not self.books.get(id):
            raise Exception("Books not found")
        return self.books[id]


# ---------------------------- User -------------------------------------
# User Class
@dataclass
class User:
    username: str
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class Users:
    users: Dict[str, User] = field(default_factory=dict)

    def add(self, user: User):
        self.users[user.id] = User

    def update(self, id, user: User):
        if not self.users.get(id):
            raise Exception("User not found")
        self.users[id] = user

    def delete(self, id):
        if not self.users.get(id):
            raise Exception("User not found")
        del self.users[id]


# --------------------- Library -----------------------


@dataclass
class LibraryEntry:
    book_id: str
    user_id: str
    is_active: bool = False
    id: str = field(default_factory=lambda: str(uuid4()))
    last_read_page: int = 0


@dataclass
class UserLibrary:
    books: dict[Books]
    entries: list[LibraryEntry] = field(default_factory=list)

    def add(self, data: LibraryEntry):
        # Before it, we have to know, either the book exists or not.
        if not self.books.get(data.book_id):
            raise Exception("Books not found")

        self.entries.append(data)
        return data

    def update(self, id: str, data: LibraryEntry):
        does_exists, index = self.does_entry_exists(id=id)

        if not does_exists:
            raise Exception("Id not found")

        self.entries[index] = data

    def delete(self, id: str):
        does_exists, index = self.does_entry_exists(id=id)

        if not does_exists:
            raise Exception("Id not found")
        del self.entries[index]

    def does_entry_exists(self, id: str):
        does_exists = False
        index = None

        for idx, book in enumerate(self.entries):
            if book.id == id:
                index = idx
                does_exists = True
                break

        return does_exists, index

    def read_book(self, lib_id: str , book_id: str, page_number: str, user_id: str):
        book: Book = self.books.get(book_id)
        if not book:
            raise Exception("Books not found")

        if page_number > book.total_page:
            raise Exception("Page number exceeded")

        updated_book = LibraryEntry(
            book_id=book.id,
            id=lib_id,
            last_read_page=page_number,
            user_id=user_id,
            is_active=True,
        )

        self.update(id=lib_id,data=updated_book)
        return True

    def get_my_active_book(self, user_id: str ):
        active_book = None
        for book in self.entries:
            if book.is_active == True and  book.user_id == user_id:
                active_book = book
                break
            
        return active_book

    def remove_book_from_active(self, user_id: str ):
        active_book = None
        for book in self.entries:
            if book.is_active == True and book.user_id == user_id:
                active_book = book
                break
        
        if not active_book:
            raise Exception("No Active book till now")
        
        active_book.is_active = False
        self.update(active_book.id, data=active_book)
        

# ------------------------------ Appplication Cloud ----------------------------------------
@dataclass
class ApplicationCloud:
    books = Books()
    my_library = UserLibrary(books=books.books)


# ---------------------------------------------------- Running the progra -------------------------------------

cloud = ApplicationCloud()

# Listing all the books


# Adding new book
new_book = Book(title="Welcome to Copilot", total_page=50)
cloud.books.add(new_book)


new_book2 = Book(title="Welcome to AI ERA", total_page=500, id=40)
cloud.books.add(new_book2)

books = cloud.books.books

print(books, "WOW")


# Create my Profile
my_profile = User(username="Sujan")

# Add new book to the library
library_entry = LibraryEntry(
    book_id=new_book.id,
    user_id=my_profile.id,
    last_read_page=0,
)
cloud.my_library.add(data=library_entry)


# Let's read the book
active_book = cloud.my_library.read_book(lib_id=library_entry.id, book_id=new_book.id,page_number=2, user_id=my_profile.id  )
print(active_book)



# List my active book 
active_book_details = cloud.my_library.get_my_active_book(my_profile.id)
print(active_book_details)