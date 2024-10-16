'''
Loop over the colors items and print out the item in every loop. So, the expected output of your code would be:

11
34
98
43
45
54
54
'''
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    print(color)

'''
Loop over the colors items and print out the item in every loop only if the item is greater than 50. So, the output of your program would be:

98
54
54
'''
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)

'''
Loop over the colors items and print out the item in every loop only if the item is an integer. So, the output of your program would be:

11
43
54
54
'''
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if type(color) == int:
        print(color)

'''
Loop over the colors items and print out the item in every loop only if the item is an integer and it is greater than 50. So, the output of your program would be:

54
54
'''
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if type(color) == int and color > 50:
        print(color)
