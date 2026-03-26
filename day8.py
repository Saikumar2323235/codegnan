'''lista=[1,2,3,"saikumar",["venkat","sai"]]
listb=["bunty","allubhai",[1,2,"bhai"]]
print(lista[4][1][2])
print (listb[2][2][2])
print(9+8)
print("python" + "language")
print([1,2]+[3,4])

concatenation
 this is nothing but , a (+) behaviour,,
 case 1
 integers --> this will act as addiction for int
 case 2
 if we try to do concatenation on different datatypes we cant and get a type error 

tuple ()-->

#is a collacation of different datatype and this is represented by parathesis ()
#and seperated by comm ,
Thing =(1,"Teja",[12,4],(6,7))
print (Thing)
'''
Thing =(12,89,"python",(22,"sandy",[67,"python is a language",(7,9)],[8,("python",[34,9])]))
print(Thing[3][2][1][9])

year = int(input("enter a year:"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is  not leap year")
