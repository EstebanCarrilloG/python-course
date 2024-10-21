'''
Make the code print out the following output using a for loop:

John Smith: +37682929928

Marry Simpons: +423998200919

So, the code should loop over the dictionary items and in each iteration should print out the dictionary key, a colon, a space, and the corresponding value.
'''

users = {"John Smith":"+37682929928", "Marry Simpons":"+423998200919"}

for key , value in users.items():
    print(f'{key}: {value}')
    
