#  Control Flow Comparison operators

# no triple sign

# python does not use braket so indentation is EXTREMELY important
if 1 < 2:
    print('Hello World')

if 3 != 3:
    print("It's not 3")
elif 2 == 1:
    print('You got it')
else:
    print('You printing the last')

# loops in python
    # List 
seq = [1,2,3,4,5]
for seq_num in seq:
    print(seq_num)


# disctionary
d = { 'Sam': 1, 'Frank':2, 'Dan':3}

# prints out the value first
for k in d:
    print(k)
    print(d[k])


# print out tuples
    # tuples insid of a list
my_pairs = [(1,2), (3,4), (5,6)]

for item in my_pairs:
    print(item)

for (item1, item2) in my_pairs:
    print(item1)
    print(item2)

# while loop
i = 1

while i <= 5:
    print(f'i is: {i}')
    i+=1


# range function the second parameter is not included,
# n Python, the range() function is used to generate a sequence of numbers. It is commonly used in for loops to iterate over a sequence of numbers. The basic syntax of the range() function is as follows:  
# range(stop)
# range(start, stop)
# range(start, stop, step)

let_list = list(range(0,33,3))
print(let_list)

for item in range(10):
    print(item)


#  List comprehensions in Python provide a concise way to create lists. They are a syntactic construct that allows you to create a new list by specifying its elements in a single line. The basic syntax of a list comprehension looks like this:
    # new_list = [expression for item in iterable if condition]
squares = [x**2 for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]
