bear_file_path = "./exercises/fileProcessing/files/bear.txt"

'''
On the side panel there's a bear.txt file. The existing code opens that file in read mode.
Below that code, please read the file content and print out the content.
'''
file = open(bear_file_path)
my_file = file.read()
file.close()
print(my_file)

'''
Read the bear.txt file, and print out the first 90 characters of its content.
'''
with open(bear_file_path, "r") as text:
    print(text.read()[:90])

'''
Define a function that gets a single string character and a filepath as parameters and returns the number of occurences of that character in the file.
'''
def foo(character,file_path):
    with open(file_path ,"r") as text:
        my_text = text.read()
        return my_text.count(character)
        
print(foo("a",bear_file_path))
'''
Use Python to create a file with name file.txt and write the text snail there.
'''
file_file_path = "./exercises/fileProcessing/files/file.txt"

with  open(file_file_path,"w") as file:
    file.write("snail")
'''
Create a first.txt file that contains the first 90 characters of bear.txt.

Note that you should read the content of bear.txt with Python, extract its first 90 characters with Python, and write those characters in first.txt with Python.
'''
first_file_path = "./exercises/fileProcessing/files/first.txt"
def read_file():
    with open(bear_file_path, "r") as file:
        return file.read()[:90]
    
with open(first_file_path , "w") as file:
    file.write(read_file())

'''
Append the text of bear1.txt to bear2.txt. In other words, bear2.txt should contain its text and the text of bear1.txt after that.
'''

bear1_file_path = "./exercises/fileProcessing/files/bear1.txt"
bear2_file_path = "./exercises/fileProcessing/files/bear2.txt"

bear1 = open(bear1_file_path)
bear1_txt = bear1.read()
bear1.close()

with open(bear2_file_path, "a") as file:
    file.write(bear1_txt)

'''
The existing content of data.txt looks like this:

1.3, 1.5

2.3, 2.7

Use Python to modify the content of data.txt so that its content looks like below:

1.3, 1.5

2.3, 2.7

1.3, 1.5

2.3, 2.7

1.3, 1.5

2.3, 2.7

So, you need to find a way to insert the existing content two more times.
'''

data_file_path = "./exercises/fileProcessing/files/data.txt"
with open(data_file_path, "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)