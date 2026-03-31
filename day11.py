'''prime_num = int(input("enter a number:"))
count = 0
for j in range (1,prime_num+1):
    print(j)    
    if prime_num % j ==0:
        count +=1
        print(count)
    if count == 2:
        print (f"{prime_num} is a prime number")
    else:
        print (f"{prime_num} is not a prime number")
            
 ---- ---------------
for an in range (2,1000):
    count = 0
    for j in range (1, an+1):
        if an % j == 0:
            count +=1
    if count ==2:
        print (f"{an} is a prime number")
    else:
        print(f"{an} is not a prime number")
        
numbers = [1057, 197, 9, 86, 17673]

for num in numbers:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


Any = [2, 356, 8, 6, 3, 2, 8]

empty_ = []
for j in Any:
    if j not in empty_:
        empty_.append(j)

print(empty_)
'''
So = int(input("enter any number"))
length_ = len(str (so))
Amstr_= 0
for j in str (So) :
    Amstr_+ = int(j) ** length_
    print(Amstr)

        
            
        


