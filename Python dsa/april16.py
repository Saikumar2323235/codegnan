'''number = list(map(int,input().split()))
for i in number:
    print(i)'''
'''a = list(map(int,input().split()))
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[j]<a[i]:
          a[j],a[i]= a[i],a[j]
print(a)'''
'''----------------------------------------------------------------------------------'''
'''type conversion and type error'''
'''length = len("Saikumar")
print("your name has : " + str(length)+ " " + "in character")'''




'''length = len("Saikumar")
print ("length has" + " " + str(length) +" "+  "\ncharacters")
new_length= str(length)
print(new_length)'''

number = input("enter any two digit number :")
first_digit = number[0]
second_digit = number[1]
print (int(first_digit) +  int(second_digit))