'''
Implements a function that takes two strings as parameters, concatenates them, and returns the result.
'''
def foo(a,b):
    return a + b

'''
Define a function that takes an indefinite number of numbers as arguments and returns their average. If I called your function with foo(10, 20, 30, 40) it should return the 25, the average of those numbers.
'''
def foo(*args):
    return sum(args) / len(args)
    
print(foo(10, 20, 30, 40))

'''
Define a function that takes an indefinite number of strings as parameters and returns a list containing all the strings in UPPERCASE and sorted alphabetically. For example, if I called your function with foo("snow", "glacier", "iceberg") it should return ["GLACIER", "ICEBERG", "SNOW"].
'''
def foo(*args):
    myList = [arg.upper() for arg in args]
    
    return sorted(myList)
    
print(foo("snow", "glacier", "iceberg"))

'''
Enter the correct parameters inside find_sum() so that the output of the code is 9.
'''
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=3,b=3,c=3))