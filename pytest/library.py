class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages} pages) "

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to Library")

    def __len__(self):
        return len(self.books)
    
    def __str__(self):
        return f"Library with {len(self.books)} Books"

    def __contains__(self, item):
        if isinstance(item, str):
            return any(book.title == item for book in self.books)
        elif isinstance(item, Book):
            return item in self.books
    
b1 = Book("Dune","Herbert", 432)
b2 = Book("Diwani","Inyass", 2390)
b3 = Book("1984","orwell", 232)
print(b1)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print(repr(b2))
print(len(lib))
print(str(lib))
print("Diwani" in lib)

for book in lib.books:
    print(book)