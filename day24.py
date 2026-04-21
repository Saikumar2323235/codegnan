'''introduction to oops
classes
objects
attributes
methods

oop's
---------[
    object oriented language (oop) is a style of programming where we model real - world things as objects
    real-world things as objects that contain both data and functions()
    --> reusable of code
    --> and also scalable
class
-----
class is a blue print or template

object
------
-->instance of class or an object is a real instance created from a class , it is the actual thing that
exists in memory while the program running

Attributes
----------
-->these are variables that store data related to a class or object

'''
'''class car:
    def _init_(self,brand,color):
        self.brand = brand
        self.color = color
car_1 = car("Toyato","white")
car_2 = car("thar","Red")
print(car_1.brand)'''



'''-------------------------------------------------------------
constructor(__init__)
---> A constructor is a special method used to initiallize object data
__init__()
'''

'''class student:
    def __init__(self,name,ID):
        self.name = name
        self.ID  = ID
        
    def display(self):
        print(self.name,self.ID)
stu_1 = student("Sai",123)
stu_1.display()
'''
'''---------------
access specifiers
1. public
syntax :-
name
we can use it anywhere in the program

2. protected
syntax:-name
this is only used for internal use

3. private
syntax:-
this one is restricted

self
--- thiskeyword is instance variable and unique for each object
'''

'''class some:
    def __init__(self):
        self.public = "public"
        self.protected = "protected"
        self.private = "private"

any = some()
print(any.public)
print(any.protected)
print(any.private)'''
'''#print(any._protected) this is given error because of calling protected variable
#print(any.__private) same as above we use private variable i.e using __name

'''














