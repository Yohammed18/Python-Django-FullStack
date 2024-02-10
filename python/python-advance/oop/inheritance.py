# Inheritance is a way to create a new class that is a modified version of an existing class. The new class, called the subclass or derived class, inherits attributes and behaviors from the existing class, known as the base class or parent class. This allows you to reuse code and create a hierarchy of classes.

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print('EATING')


class Cat(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("DOG CREATED")

    def whoAmI(self):
        print("DOG")

    def eat(self):
        print('Dog Eating')


cat = Cat()
cat.whoAmI()
cat.eat()