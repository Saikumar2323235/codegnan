'''
Variables -->Variables is basically named storage location that is used to dat in the memory ,
                 to make it simple itis the label which points
              out to a value --> storage place holders


            Rules for defining varaiables
            -->A-,a-z,0-9
            -->start with uppercase,lowercase letters , even with a underscore
            -->But you cannot start with symbols (@,#,$...), even numbers also

            Better preferable way is to go with general purpose -->you want to store
                                                  your details name,email,account_number..

 '''
a=1
b=2
a=25
#Python is dynamically typed ,you need not define the data type and also
#only the recent value to the variable with same name is pointed

print(a)
print(b)
#1a23 = 25 #Syntax error

#@werf = 4.5 #Invalid error

#$dsf = 12 #Invalid Syntax
#Store your personal details

name="Codegnan"
location="Visakhapatnam"
age=7
email_id ="cmo@codegnan.com"
print (name,location,age,email_id)
#How to assign multiple values to a variable
akash,praneeth,ajay=21,20,22
print (akash)
print (praneeth)
print (ajay)
#assign same value to multiple varaiables

x = y = z = 21
print(x,y,z)
#keywords are reserved words which will have specific us
#there are 35 keywords in Python
#never use keywords as Identifiers

#if =23
#lambda = 'saketh'
#false = 0 #cannot assign

#Pyhton is case-sensitive
false =25

#Identifiers are names given to variables ,functions,classes,objectives...

#Literals are fixed values to a Identifier
name=25

#name is Identifier,25 is literal

#Built-in Datatype -->numeric,boolean,collections
#Numeric datatypes -->int,float,complex
#int -->count,values,quantities
#float -->temperature,percentage,price
#complex--> specific conversions (real and imaginary)
count = 40
print(count)
print(type(count))

price= 175.25
print(price)
print (type(price))

j3=25
value = 2+j3
print (value)
print (type(value))
value = 2+3j
print (value)
print (type(value))

#Typecasting -->converting one type to another

#int -->float,complex

age = 25
print(type(age))

b = float(age)
print(b)
print(type(b))
c = complex (age)
print (c)
print (type(c))

#float,complex
price = 275.25
print (type(price))
d = int (price)

#boolean datatype -->validation True/False
a= True
print(a)
print (type(a))
    
#type conversion of bool
b=int (a)
print(b)
c= float(a)
print(c)
d = complex(float())
print(c)

d = complex(float(int(False)))
print(d)
print(type(d))

# Input / Output
a = 5
print(a)

a = input("enter a value: ")
print(a)
print(type(a))

# Integer input
b = int(input("enter an integer value: "))
print(b)
print(type(b))

# Float input
c = float(input("enter float data: "))
print(c)
print(type(c))

# Case Study: Fee Calculator
name = input("enter the student name: ")

admission_fee = int(input("enter the admission fee: "))
tuition_fee = float(input("enter the tuition fee: "))
hostel_fee = float(input("enter the hostel fee: "))

total_fee = admission_fee + tuition_fee + hostel_fee

print("-----------")
print("student name:", name)
print("Admission fee:", admission_fee)
print("tuition fee:", tuition_fee)
print("hostel fee:", hostel_fee)
print("total fee:", total_fee)

    
       

