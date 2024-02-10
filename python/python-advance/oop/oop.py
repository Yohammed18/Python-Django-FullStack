# everything in python is an object
# we can create object by first creating a blue print called "class"

class Sample():
    pass

x = Sample()
# print(type(x))


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

        # this is the equivilent of toString() in java
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('A book is destroyed')

b = Book('Python', 'Mohammed', 50)
print(b)
print(len(b))
del b


