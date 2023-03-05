#file handing:

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists



#1-reads file:
"""#1:
f= open("05.03.2023.demo.txt","r")
print(f.read())"""


"""#2:By default the read() method returns the whole text, but you can also specify how many characters you want to return:

f=open("05.03.2023.demo.txt","r")
print(f.read(5))"""


"""#3: readline()-return one line :

f=open("05.03.2023.demo.txt","r")

print(f.readline())
print(f.readline())"""


"""#4: By looping through the lines of the file, you can read the whole file, line by line:

f=open("05.03.2023.demo.txt","r")
for x in f:
    print(x)"""
    
    
"""#5:Close Files->It is a good practice to always close the file when you are done with it.

f=open("05.03.2023.demo.txt","r")
print(f.readline())
f.close()"""





#2:write and create file:

#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content

"""#2.1:Open the file "demofile2.txt" and append content to the file:

f=open("05.03.2023.demo.txt","a")
f.write("Now the file has more content!")
f.close()

##open and read the file after the appending:
f=open("05.03.2023.demo.txt","r")
print(f.read())"""


"""#2.2:Open the file "demofile3.txt" and overwrite the content:

f=open("05.03.2023.demo.txt","w")
f.write("Woops! I have deleted the content!")
f.close()

f=open("05.03.2023.demo.txt","r")
print(f.read())"""


#2.3: create file->Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

"""f=open("06.03.2023.txt","x")

f=open("06.03.2023.txt","a")
f.write("hello!")
f.close()

f=open("06.03.2023.txt","r")
print(f.read())"""


#3: Delete a File->To delete a file, you must import the OS module, and run its os.remove() function:

"""#3.1
import os

os.remove("06.03.2023.txt")"""


"""#3.2

import os

if os.path.exists("06.03.2023.txt"):
    os.remove("06.03.2023.txt")
else:
    print("file there does not exist")"""