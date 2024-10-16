#Ask for user name
name = input("What is your name?").strip().title()
"""
#Get length of string
len(name) 
#Remove whitespaces from string
name = name.strip()
#Capitalize first word only
name = name.capitalize()
#Capitalize every word
name = name.title()
"""
#Split users name into first name and last name
first, last = name.split(" ")
print(f"hello, {first}")



#Say hello to user
#print(f"hello, {name}")


