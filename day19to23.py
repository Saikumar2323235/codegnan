'''lambda function()
-----------------------
--> this is also called anonymous function ..
--> a lambda function can take a number of arguments but have only one expression

syntax
---------
          lambda (keyword) arguments : expression
             
any = lambda so :so +10
print(any(16)) #output==-26
print(any(10))
some = lambda an , how : how -an
print (some(10,20)) # we can pass any arguments at a time like this
                    #by increasing n:of arguments after lambda keyword and pass
                    #that no of arguments while calling

some = lambda an, how , do : (how- an)*do
print(some(4,9,2))

money = lambda rupee,paisa,dollar : (dollar-rupee)/paisa
print(money(50,25,100))

--------------------------------------------------------------------------------
list comprehension:
--> this is offers the shorter syntax when you want to create a new left from the existing list
from the existing list
syntax
------ variable_name = [expression loop and addition]


oldlist = [1,2,3,4]
newlist =[j for j in oldlist]
print(newlist)

evenlist = [j for j in oldlist if j%2==0]
print("even list",evenlist)
---------------------------------------------------------------------------------------------------------
generators -----
-----> This is a special type of function that return as ITERATOR which one at a time 

yield -----
---> it will take a pause and again resume , this is not a normal keyword can not be used in normal functions
---> this is used to produce a value and pause execution

next ---
This is used to get next value from a generator
when the value is finished , it will stop the iterator'''
'''-----------

def my_generator():
    yield 1
    yield 2
    yield 3
an = my_generator()

print(next(an))
print(next(an))
print(next(an))

#next example

def square_gen(n):
    for i in range(n):
        yield i*i

for val in square_gen(5):
    print(val)
 '''
'''-------------------------------------------------------------------------------------------------------
#MODULES
---------
--> a module in a python is simply file that contain python code (Function, classes , variables)
--> to use modules , we have to use a keyword called import before the modules

                           Types of modules :-

                    1. built in or inbuilt
                    2. user defined

user define module :
this is developed by the user or programmer inside a file of python code and used by called
import with file names

syntax --> import(keyword) file_name

using of the functionilty of the existing of the file_name.functionality

import module
print(module.add(2,3))
print(module.namereverse("kumar"))

#buitlnin or in built
--> these are comes with installization of python and we can use it by importing
a certain module and can access their functionality as same like in userbuilt
modules
 syntax-
         modulename.function()
    for importing - import module
example
import match
math.add 
import math
print(math.sqrt(25))
print(math.pow(50,10))
print(math.factorial(11))
print(math.floor(5.3))
print(math.exp(10))
print(math.comb(70,10))
'''
import pyttsx3

engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
speak_text("Hello I am your assistance")

    


















 
