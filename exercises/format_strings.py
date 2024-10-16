'''
Implement a function that gets a person's name as a parameter and greets the person with Hi Person. For example, if I called your function using foo("Marry") the function should return Hi Marry .
'''
def say_hello(name):
    return f"hi {name}"
    
print(say_hello("Esteban"))

'''
Implement a function that gets a person's name (e.g. john) as a parameter and returns a greeting (e.g. Hi John). Note that the first letter of the person's name should always be uppercase.
'''
def say_hello(name):
    name = name.capitalize()
    return f"Hi {name}"
    
print(say_hello("esteban"))