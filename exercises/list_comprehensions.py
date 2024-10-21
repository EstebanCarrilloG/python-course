'''
Define a function that takes as a parameter a list that contains both integers and strings and returns the list containing only the integers. For example, if I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 95, 94].
'''
def remove_strings(list_to_edit):
    return [item for item in list_to_edit if isinstance(item, int)]
    
print(remove_strings([99, 'no data', 95, 94, 'no data']))

'''
Define a function that takes as parameter list of numbers and returns the list containing only the numbers that are greater than 0. For example, I called your function with foo([-5, 3, -1, 101]) it should return [3, 101].
'''
def foo(numbers):
    return [number for number in numbers if number > 0]
    
print(foo([-5, 3, -1, 101]))

'''
Define a function that takes as parameter a list that contains both numbers and strings and returns the same list but with zeros instead of strings. For example, I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 0, 95, 94, 0].
'''
def foo(d):
    return [i if i != "no data" else 0 for i in d]
    
print(foo([99, 'no data', 95, 94, 'no data']))
'''
Define a function that takes as parameter a list that contains decimal numbers as strings and returns the sum of those numbers. For example, I called your function with foo(['1.2', '2.6', '3.3']) it should return 7.1. Note that the floats of the input list are string datatypes.
'''
def foo(i):
    return sum([float(j) for j in i])
    
print(foo(['1.2', '2.6', '3.3']))