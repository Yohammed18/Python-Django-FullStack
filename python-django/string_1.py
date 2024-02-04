# python using snake cases instead of camel case
first_name = 'Michael'
last_name = 'Jordan'

print(f'My name is {first_name} and my last name is {last_name}!')

# single quote with double quote

print("I'm not a dog")
print('I\'m not a dog')

# grab an element from a string
my_string = 'abcdefg'

# grabs element up to the 4th index
print(my_string[:3])

# only grab cde
print(my_string[2:5])

# step side 
print(my_string[::2])

x = my_string.upper()
print(x)

# split
print( 'You Don\'t Know My Name.'.split(' '))

# String interpolation 
print("Insert another string here: {}".format("INSERT ME!"))

print("I am Software Engineer learning {x}. I will be using {y} to be web application!".format(x="Python", y="Django"))