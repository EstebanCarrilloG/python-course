**Tip: Converting Between Datatypes**

Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

**From tuple to list:**

```python   
>>> cool_tuple = (1, 2, 3)
>>> cool_list = list(cool_tuple)
>>> cool_list
[1, 2, 3]
```

**From list to tuple:**

```python   
>>> cool_list = [1, 2, 3]
>>> cool_tuple = tuple(cool_list)
>>> cool_tuple
(1, 2, 3)
```

**From string to list:**

```python   
>>> cool_string = "Hello"
>>> cool_list = list(cool_string)
>>> cool_list
['H', 'e', 'l', 'l', 'o']
```

**From list to string:**

```python   
>>> cool_list = ['H', 'e', 'l', 'l', 'o']
>>> cool_string = str.join("", cool_list)
>>> cool_string
'Hello'
```

As can be seen above, converting a list into a string is more complex. Here str() is not sufficient. We need str.join(). Try running the code above again, but this time using str.join("---", cool\_list) in the second line. You will understand how str.join() works.
