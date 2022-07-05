class Book:
    no_of_books = 0

    def __init__(self, title, author, no_page, price):
        self.title = title
        self.author = author
        self.no_page = no_page
        self.price = price
    
    def __str__(self):
        return f"Details of the book {self.title}"
    
    def __repr__(self):
        return f"Book(\"{self.title}\", \"{self.author}\", {self.no_page}, {self.price}"
    
    @classmethod
    def increment_no_of_books(cls):
        cls.no_of_books+=1
    
    def explain(self):
        print(f"{self.title} is written by {self.author}")
        print(f"It costs {self.price} dollars")
        print(f"It have {self.no_page} pages")

b1 = Book("The Secret", "Rhonda Byrne", 150, 200.50)
b1.explain()
Book.increment_no_of_books()
print(Book.no_of_books)

print()

b2 = Book("The Hunger Games", "Joswin Emmanuel", 203, 1500.00)
b2.explain()
Book.increment_no_of_books()
print(Book.no_of_books)

print()

print(b1.__str__())
print(b1.__repr__())