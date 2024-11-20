
def hello(name = "World"):
    print(f"hello,{name}")


hello()
name = input("What's your name? ")
hello(name)


"""
def main():
    name = input("What's your name? ")
    hello(name)

def hello(name):
    print(f"hello,{name}")

main()
"""

def main():
    x = int(input("What's x?"))
    print("x square is:",square(x))

def square(x):
    return x * x
    ## return n ** 2
    ## return pow(n ,2)

main()

'''
Define a function that:

(1) takes a temperature as a parameter

(2) returns "Warm" if the temperature is greater than 7

(3) returns "Cold" if the temperature is equal to or less than 7

If I called your function with foo(10) it would return Warm. If I called it with foo(7) or foo(5) it would return Cold in both cases, and so on.
'''
def temp(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
        
print(temp(7))
'''
Define a function that:

(1) takes a string as a parameter

(2) returns False if the string contains less than 8 characters

(3) returns True if the string contains 8 or more characters

In other words, if I called your function with foo("mypass") it would return False. If I called it with foo("mylongpassword") it would return True, and so on.
'''
def length_verifier(string):
    if len(string) >=8:
        return True
    else:
        return False
        
print(length_verifier("12345678"))

'''
Define a function that:

(1) takes a temperature as a parameter

(2) returns "Hot" if the temperature is greater than 25

(3) returns "Warm" if the temperature is between 15 and 25, including 15 and 25.

(4) returns "Cold" if the temperature is less than 15.

If I called your function with foo(10) it would return "Cold". 

foo(15) or foo(16) or foo(25) would all return "Warm" and foo(26) would return "Hot".
'''
def temp(temperature):
    if temperature > 25:
        return "Hot"
    elif temperature >= 15 and temperature <= 25:
        return "Warm"
    else:
        return "Cold"
        
print(temp(10))