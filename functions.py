"""
def hello(name = "World"):
    print(f"hello,{name}")


hello();
name = input("What's your name? ")
hello(name)
"""

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

main()
    
