#  Python scope follows the LEGB rules, Local, enclosing fuctional locals, global, Built-in

x = 25

def my_func():
    x = 50
    return x


# print(x) # 25
# print(my_func()) # 50
my_func() 
print(x) # 25

# LOCAL level scope
lambda x: x**2

# enclosing function locals
name = 'This is a global name!'

def greet():
    name = 'sammy'

    def hello():
        print(f'Hello {name}')

    hello()

greet()
print(name)