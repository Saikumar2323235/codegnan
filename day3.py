'''
Operators --> An operator is a symbol that performs an operation on one or more values (operands) and produces a
result
Operators are primarily used :
--> Calculate values
-->Compare values/ inputs
-->Make decisions
-->Control the program flow

There are major seven categories of operators in python

-->Arithmetic Operators
-->Assignment Operators
-->Comparision Operators
-->Membership Operators (in,not in)
-->Identity Operators (is,is not)
-->Bitwise Operators
-->Logical Operators (and,or,not)
'''
 #Arithemtic Operators -->Arithmetic Operators performs mathematical operations
# + -->Addition, - -->Subtraction , * -->Multiplication, / -->Division
# ** -->Exponent , % -->Modulus ,// -->Integer Division
'''a = 5
b = 3
print (a+b)
print (a-b)
print (a*b)
print (a/b) #returns the result in float values
print (a**b) #returns the exponential value

print (a%b) #modulus  division --> returns remainder
print (a//b)#floor / integer Division -->returns the quotient discards

#f-string notation
num1 = int(input ("enter the first value:"))
num2 = float(input("enter the second value"))
result = (num1 + num2)*4
print("the result is",result) #standard notation

 #f-string notation
print(f'The result is {result}')
print(f'the number of {num1} and {num2} is {result}, {num1*num2}')

#Assignment Operators
#--> = Assign, +=Addition Assignment ,
#-= -->Subtract Assignment,*=,/=,%=,//=,**=

#They are majorly used for code repetition in application usage

a = 4
b = 3
a+=2 #--> a =a+2
print (a)
b+=a
print(b)

#in similar way check for -=, *=, **=,/=, %=, //=

b-=3 #b= b-3
print (b)
b *= a#b =b*a
print(b)


#Relational or comparision Operators -->They always return the boolean values
# == is equal to , != not equal to
# < less than , > greater than , >=,<=

a = int (input("enter the value:"))
b = int(input("enter the value:"))
print(a ==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)



#Membership Operators -->They check for the existance of an object in a
#Collection --> in,not in

a= "codegnan"
print(type(a))
print('a' in a)
print('z' in 'saikumar')
print('z' not in 'codegnan')

b = [12,6,3,2]
c = int (input("enter the value"))
print(c)
print(c in b)
print(c not in b)

#Logical operators --> They are used to combine multiple conditions
#and,or,not

age = int(input("enter the age:"))
vote_right = True
print (age >=18 and vote_right)#both conditions to be true then only True
print (age <=18 or vote_right) #any one condition is True then result is True 
print (age <=18 , not vote_right)


#Identify Operatos -->They check the/compare the memory location  and validate we use
#(id) function it is different from == operator --> is , is not

a = [1,2,4]
b = [1,2,4]
print(a == b)
print(id(a))#returns the identify of an object
print (id (b))
print (a is b)
print (a is not b)

c = b
print(c) #assigning b to c 
print(id(c)) #then b and c have same memory location
print(c is b) #returns true because b,c have the same memory location  
'''

#bitwise operators -->Bitwise AND & ,Bitwise or | perform bitwise operators
#we get the result (remember the binary conversion)
print(5&3) 
print(bin(5)) #returns binary number

#Task --> Now you all operators create a checker task
#git add .
#git commit -m "operator usage"
#
