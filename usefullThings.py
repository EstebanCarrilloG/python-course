#Works on python interactive shell.
dir(int) #show all the things you can do with an specific type. 

"""
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
"""
dir(__builtins__) #shows a complete list of integrated functions that we can use.
help(str.upper) #shows info about methods or properties 

"""
Help on method_descriptor:
upper(self, /)
    Return a copy of the string converted to uppercase.
"""

## list slice
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[3:8] #Get items from index 3 to index 7. "8 is not included."
print(b) #Output: [4, 5, 6, 7, 8]

b= a[:8] #Get items from index 0 to index 7. "8 is not included."
print(b) #Output: [1, 2, 3, 4, 5, 6, 7, 8]

b = a[3:] #Get items from index 3 to the end
print(b) #Output: [4, 5, 6, 7, 8, 9, 10]

#Negative index
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[-3:] #Get items from index -3 to the end
print(b) #Output: [8, 9, 10]

b = a[:-3] #Get items from index 0 to -3
print(b) #Output: [1, 2, 3, 4, 5, 6, 7]

## End list slice

## Accessing Item in Dictionaries

a = {"a": 1, "b": 2, "c": 3}
print(a["a"]) #Output: 1

## End Accessing Item in Dictionaries