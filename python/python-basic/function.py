# Functions in Python use the def keyword. 

def helloWorld(name='Smith'):
    print(f'Hello {name}!')


helloWorld('Mohamemd')
helloWorld()

# example showing how you can document a function
def my_func(param1='default'):
    """
    THIS IS THE DOC STRING
    """
    print("Parameter {}".format(param1))

my_func()

# return function
def multiplication(x=3, y=12):
    return x * y

print(multiplication())


# lambda function or expression  a small anonymous function defined using the lambda keyword. Lambda functions are also known as anonymous functions because they don't have a name like a regular function defined with the def keyword.

my_list = [1,2,3,4,5,6,7,8,9]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, my_list)

print(list(evens))

# anonymous function
# lambda num: num%2 == 0

odds = filter(lambda num: num%2==1, my_list)
print(list(odds))

# when or how will you a split method
tweet = "Go basketball! #Sports."
result = tweet.split('#')[1]
print(result)
