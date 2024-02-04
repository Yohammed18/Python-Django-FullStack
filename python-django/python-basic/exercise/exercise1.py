# given the string below you want to print out the following 
s = 'django'
# 'd'
print(s[0])
# 'o'
print(s[-1])
# 'djan'
print(s[0:4])
# 'jan'
print(s[1:4])
# 'go'
print(s[-2::])

# Bonus: Use indexing to reverse the string
reverse_s = s[::-1]


# given this nested list
l = [3,7, [1,3,'hello']]

# reassign 'hello' to be 'goodbye'
l[2][2] = 'goodbye'
print(l)

# Using keys and indexing, grab the 'hello; from the following dictionaries

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}

print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1])

#  use a set to find the unique values of a list below:
mylist = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]

myset = set(mylist)
print(myset)

#  You are given two variables
age = 4
name =  "Sammy"

# use print formating to print the following string
"Hello my dog's name is Sammy and he is 4 years old"
print(f"Hello my dog's name is {name} and he is {age} years old.")

print("Hello my dog's name is {} and he is {} years old.".format(name, age))
