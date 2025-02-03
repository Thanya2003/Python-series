class library:
    def __init__(self, name):
        self.name=name
        self.Books=[]
    
    def add_book(self, book):
        self.Books.append(book)

    def list_book(self):
        return[f"{book.title} by {book.author} " for book in self.Books]

class Book:
    def __init__(self, title, author):
        self.title= title
        self.author=author

lib=library("New City center Library")

book1=Book("Harry Potter", "J K Rotter")
book2=Book("Harry genner", "J K genifer")
book3=Book("It's fine", "W K Rao")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
print(lib.name)
for boo in lib.list_book():
    print(boo)

