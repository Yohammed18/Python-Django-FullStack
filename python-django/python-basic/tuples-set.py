#  tuples are immutable while set are unique unorderd collections of elements

# Booleans

True or False


# Tuples - can't change the value once stored, Opposite of a list
my_tuple = (1, '2', 32, 10, True, 19.01)
print(my_tuple)
print(my_tuple[0])

my_list = list(my_tuple)
my_list[4] = False

print(f'Tuples: {my_tuple}, {type(my_tuple)}')
print(f'Lists: {my_list}, {type(my_list)}')


# Sets -  unordered collection of unique elements. 

x = set()
x  = { 2,5, 0, 11, -23}

print(type(x))
x.add(1)
x.add(2)
x.add(2)
x.add(2)
x.add(2)
print(x)