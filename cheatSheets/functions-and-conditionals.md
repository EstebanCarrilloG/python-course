**Cheatsheet: Functions and Conditionals**

In this section, you learned to:

*   Define **functions**:
    

```python   
def cube_volume(a):    
    return a * a * a   
```

*   Write **if-else** **conditionals**:
    

```python   
message = "hello there" 
if "hello" in message:    
    print("hi")
else:    
    print("I don't understand")   
```

*   Write **if-elif-else conditionals:**
    

```python   
message = "hello there" 
if "hello" in message:    
    print("hi")
elif "hi" in message:    
    print("hi")
elif "hey" in message:    
    print("hi")
else:    
    print("I don't understand")   
```

*   Use the and operator to check if **both conditions** are True at the same time:
    

```python   
x = 1
y = 1 
if x == 1 and y==1:    
    print("Yes")
else:    
    print("No")   
```

*   Use the or operator to check if **at least one condition** is True:
    

```python   
x = 1
y = 2 
if x == 1 or y==2:    
    print("Yes")
else:    
    print("No")   
```

*   Check if a value is of a particular **type** with **isinstance**:
    

```python   
isinstance("abc", str)
isinstance([1, 2, 3], list)   
```

or directly:

```python   
type("abc") == str
type([1, 2, 3]) == lst   
```