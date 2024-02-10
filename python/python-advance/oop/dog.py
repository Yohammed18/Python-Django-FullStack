class Dog():

    # Class object attributes
    species = "mammal"

    # in Python, the __init__ method is equivalent to a constructor in a class. 
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # method/functions provides an action for the class. They can either be void or return value



my_dog = Dog(breed='Lab', name='Charlie')
huskie_dog = Dog(breed='Huskie', name='Wolf')
print(f'My dog {my_dog.name} is a {my_dog.breed}')
print(f'My dog {huskie_dog.name} is a {huskie_dog.breed}')
print(my_dog.species)