my_dict = {'item1': 1, 'item2':2,  'item3':3,  'item4':5}
# print dictionary
print(my_dict)
print(f'You call the dictionary by passing the key: {my_dict["item1"]}\n')

# dictionaries are flexible 
flex_dictionary = {'Michael':23, 'Kobe':24, 'Shaq': 34, 'Key':{'123':[1,2,"grab me"]}}

print(flex_dictionary['Key']['123'][2])

# change dictionary
my_lunch = {'pizza':9.99, 'pasta': 10.99}

print(f'Before third key addition. {my_lunch}')

# addingt a key-value pair
my_lunch['burger'] = 5.99
# changing the value for key 'pizza'
my_lunch['pizza'] = 15.99

print(f'Before third key addition. {my_lunch}')
