class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_books(self):
        print(f"title: {self.title}")
        print(f"author: {self.author}")
        print(f"pages: {self.pages}")


book1 = Book("Harry Potter", "J.K. Rowling", 300)
book1.display_books()  # Output: Title: Harry Potter, Author: J.K. Rowling, Pages: 300