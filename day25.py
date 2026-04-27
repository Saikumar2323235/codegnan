'''encapsulation
-----------------
-->The principle of building data(Attributes) and methods that operate on that data into a single unit ,
which is a class
'''
'''class BankAC:
    def __init__(self, balance):
        self.__balance = balance
    def deposite(self,amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
Acc = BankAC(15000)
Acc.deposite(7000)
print(Acc.get_balance())'''


'''inheritance
-----------
--> this allows a child class (subclass) to acquire the attandence and method
of a parent class (Base class) this is called inheritance
1.single inheritance
2.multiple


super()
--------
--> this is used to call methods of the parent class from the child class'''

'''class parent:
    def display1(self):
        print("this is parent method")
class child(parent):
    def display2(self):
        super().display1()
        print("this is child method")
objp = parent()
objp.display1()
objc = child()
objc.display2()'''


'''#multiple inheritance
class father:
    def skill_1(self):
        print("father : hardworking")
class mother:
    def skill_2(self):
        print("mother : cooking")
class child(father,mother):
    def all_skills(self):
        super().skill_1()
        super().skill_2()
        print("child : coding")
c = child()
c.all_skills()'''

'''multi-level
-----------
--> This occurs when a class inherits from a child class , creating a
grandparent --> Parent --> child in this structure.
'''
'''class Grandparent:
     def Show_GrandParent (Self):
         print("I'm Grandparent")

class Parent(Grandparent):
    def Show_Parent(self):
        print("I'm Parent")

class child(Parent):
    def Show_Child(self):
        print("I'm child")

any = child()
any.Show_GrandParent()
any.Show_Parent()
any.Show_Child()'''


'''Hierarical
------------
--> This occurs when multiple child classes inherit from a single parent class
this process is hierarical
class parent:
    def Parent_(self):
        print("I am Parent")


class child_1(parent):
    def child_(self):
        print("I am 1st child")


class child_2(parent):
    def _child(self):
        print("I am 2nd child")


class child_3(child_1, child_2):
    def child(self):
        print("I am the child")


thing = child_3()
thing.Parent_()
thing.child_()
thing._child()
thing.child()

hybrid inheritance
-------------------
--> This is a combination of two or more types of inheritance, such as single,
multiple, multilevel, or hierarichal , all this in a single class ...'''


'''class parent:
    def Parent_(self):
        print("I am Parent")


class child_1(parent):
    def child_(self):
        print("I am 1st child")


class child_2(parent):
    def _child(self):
        print("I am 2nd child")


class child_3(child_1, child_2):
    def child(self):
        print("I am 3rd child")


thing = child_3()
thing.Parent_()
thing.child_()
thing._child()
thing.child()
'''
'''
polymorphism
 -------------> this allows a object of different classes to be treated as instance
of the same base class , with methods behaving differently based on the actual object type

eg ....
-------------
print(len("Python")
print(len([1,2,3])

-------------------------------------------------------------------------------------------------------
method overloading
--> this defines multiple with the same name but the different parameter
      (number, type , or order ) in the same class
      '''
'''
class calculator:
      def add(self, a , b=0 , c=0):
          return a+b+c
Cal= calculator()
print(Cal.add(2))
print(Cal.add(3,4))
print(Cal.add(5,7,8))
'''
'''--> this is customizes operator like +, - for user-defined classes by implementing special methods
eg... __add__ , __sub__
'''
'''
class someone:
    def __init__(self, a, b):
        self.a = b
        self.b = b
    def __add__ (self, other):
        return someone(self, other):
    def __str__ (self):
        return f"({self.a}, {self.b})"
any = someone(2,3)
so = someone(5,9)
print(any + so)'''

'''------------------------------------------------------------
method overriding
---->
this occurs in the child class, redifining a parent class method with the same
signature for runtime'''

'''class animal:
    def speak(self):
        return "sound"
class dog (animal):
    def speak(self):
        return "Woof"
'''
'''
-----------------------------------------------
Abstraction--> this hides complex implementation details, exposing only essential
features via abstract class or interface
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)
print(circle.area())















































      







































