'''
Append the value of current to the end of the list seconds Please use the list.append() method to do that.
'''
seconds = [1.23, 1.45, 1.02]
current = 1.11

seconds.append(current)

'''
Remove item 1.45 from seconds.
'''
seconds = [1.23, 1.45, 1.02, 1.11]
#dir(list)
seconds.remove(1.45)

'''
Remove items 1.45, 1.02, and 1.11 from seconds.
'''
seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)
seconds.remove(1.02)
seconds.remove(1.11)