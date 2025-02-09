class Book:
    def __init__(self, title, author, nu_pages):
        self.title=title
        self.author=author
        self.nu_pages=nu_pages

    def __str__(self):
        return f"{self.title} By {self.author} includes {self.nu_pages}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.nu_pages < other.nu_pages
    
    def __gt__(self, other):
        return self.nu_pages > other.nu_pages
    
    def __add__(self, other):
        return f"{self.nu_pages+other.nu_pages}pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, keyword):
        if keyword== "title":
            return self.title
        elif keyword == "author":
            return self.author
        elif keyword== "num_pages":
            return self.nu_pages
        else:
            return f" key {keyword} not found"


book1=Book("The Overthinking", "J R R thale", 236)
book4=Book("The Overthinking", "J R R thale", 236)
book2=Book("The alone", "J R R jackson", 126)
book3=Book("The act to be done", "Jhen", 152)

print(book1)
print(book1 == book4)
print(book2<book1)
print(book1>book2)
print(book1+book2)
print("ttt" in book1)
print(book1['num_ges'])
