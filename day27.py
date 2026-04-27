# File Handling
'''
file handler is an object of file to maintain several files


# How to open a file
# -------------------
# 1. open()

This open() function takes 2 parameters and in this we have to close
the file by calling close() function after program.
1. file name
2. mode


# 2. with open()
# ----------------

# Modes ("r", "w", "a", "x", "t")

# 1. "r" -- read

To read the file we will use this mode and if the file doesn't exist,
it will throw the error
'''

'''
any = open("demofile.txt","r")
print(any.read())
any.close()'''

'''----------------------------------
2. write 
to write the text into the the file we will use the mode an it will create the file if it doesnot exist

any = open("demofile.txt", "w")
any.write("Hello Saikumar")
any.close()'''
'''------------------------------------
3. append
is used to add data without deleting old data:

any = open("demofile.txt","a")
any.write("\n I am a codegnan student")
any.close()

-------------------------------------------
4. create
this is used to create a file , but it is already stored in the system so it doesn't exit

any = open("demofile.txt","x")
any.close()

------------------------------------------
* read a file
1. read()-> this method is  used to read the entire the file chunk by chunk we can also specify the size

any = open("demofile.txt","r")
print(any.read(1000))
any.close()

2. read the line()-> this method can read the file line by line

any = open("demofile.txt","r")
print(any.readline())
print(any.readline())#-> continues to the second line 
any.close()


3. readlines ()'''

import os
any = open("demofile.txt", "a")
print(any.write("\nThis line is appended using a mode"))
any.close()
os.remove
any.write("this is a append")






































