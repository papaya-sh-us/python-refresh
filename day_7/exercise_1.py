class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def summary(self):
        return "'" + self.title + "' by " + self.author + " in " + str(self.year)


book1 = Book("Human Compatible", "Stuart Russell", 2019)
book2 = Book("The Alignment Problem", "Brian Christian", 2020)

print(book1.summary())
print(book2.summary())