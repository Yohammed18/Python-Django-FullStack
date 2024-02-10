# Lists

mylist = ['a','b','c', 'd']
my_list = [1,2,3,4,5]

print(my_list)
print(len(my_list))

# print elements in a list
print(mylist[3])
print(mylist[::3])

# append any element to the end of the list
mylist.append('I have been appended')
print(mylist)

# extend will add multiple items
mylist.extend(["x", "y", 'z'])

print(mylist)


pop_item = mylist.pop()

print(mylist)
print(f'Popped element: {pop_item}')

my_list.reverse()
print(my_list)

# you can sort element as well
unsorted_list = [12,5,3,0,-2,-123, 3,6,2]
unsorted_list.sort()
print(f'{unsorted_list}')

# nested list maxtrix
nested_list = [1, 2, ['x', '4'], 3]
print(nested_list[2][1])

matrix = [[1,2,3], [4,5,6],[7,8,9]]
print(matrix[0][0])

# List comprehansion
first_col = [row[0] for row in matrix]
print(first_col)