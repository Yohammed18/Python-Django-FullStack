# given a list of intergers, return true if the sequence of number 1,2,3 appears in the list somwhere

# case [1,1,2,3,1] = True
# case [1,1,2,4,1] = False
# case [1,1,2,1,2,3] = True

def arraycheck(nums):
    """
    Given a list of intergers, return true if the sequence of number 1,2,3 appears in the list somwhere
    """
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False
            
testcase1 = [1,1,2,3,1]
print(arraycheck(testcase1))
testcase2 = [1,1,2,4,1]
print(arraycheck(testcase2))
testcase3 = [1,1,2,1,2,3]
print(arraycheck(testcase3))


# Given a string return a new string made of every other character starting with the first 
# StringBits('Hello') -> 'Hlo'
# StringBits('Hi') -> 'H'
# StringBits('Heeololeo') -> 'Hello'

def stringBits(mystring):
    """Given a string return a new string made of every other character starting with the first """
    result = ''

    for i in range(len(mystring)):
        if i%2==0:
            result = result + mystring[i]
    return result        

print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))


# Given two strings, return True if either of the strings appears at the very end of a the other string.
def end_other(a, b):
    a = a.lower()
    b = b.lower()

    # return (b.endswith(a) or a.endswith(b))
    return a[-(len(b)):] == b or a == b[-len(a):]

print(end_other('abc', 'abXabc'))

# doble char
def doublechar(mystring):
    result = ''

    for i in mystring:
        result += i*2
    return result


print(doublechar('The'))
print(doublechar('AAbb'))
print(doublechar('Hi-There'))