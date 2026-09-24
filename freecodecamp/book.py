"""
  Normally, Python data types like strings and numbers already know how to add things, do concatenation, compare for equality, be used in loops, and others.

  But when we create our own class, Python won't know how to handle things automatically.

  This is where special methods come in — they let us customize Python's built-in behavior.

  Let's say we want to get the number of pages in book objects created with the class below, or compare them and get a readable string of the objects. 
  Here's what happens without special methods:
      len(book1) fails because Python doesn't know how to get the length of your book object without __len__()

      str(book1) prints something like <__main__.Book object at 0x102ed2900> because that's the default representation when we don't use __str__()

      book1 == book2 results in False because Python just checks if both objects are the same in memory, not by content.

Here's how we can define your own __len__(), __str__(), and __eq__() special methods to make working with objects created from the Book class easier:
"""

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

    def __eq__(self, other):
        return self.pages == other.pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1)) # 420
print(len(book2)) # 420
print(str(book1)) # 'Built Wealth Like a Boss' has 420 pages
print(str(book2)) # 'Be Your Own Start' has 420 pages
print(book1 == book2) # True
