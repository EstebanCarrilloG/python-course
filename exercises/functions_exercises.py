'''
Define a function that calculates the area of a square.

For example, if I was to call your function with foo(7) the output would be 49. If I called it with foo(3)  it would return 9, and so on. Note that you don't have to name your function foo. Give it any name you want.
'''
def square_area(side):
    return side ** 2

print(square_area(7))


'''
Define a function that converts fluid ounces to milliliters knowing that 1 fluid ounce is equal to 29.57353 milliliters. For example, I was to call your function with foo(1) I would get an output of 29.57353. If I called it with  foo(5) I would get 147.86765, and so on.
'''

def conver_function(val):
    return val * 29.57353
    
print(conver_function(5))