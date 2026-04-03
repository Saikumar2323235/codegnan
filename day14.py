'''#star pattern, number pattern
num = int(input("enter the limit:"))
for j in range (num):
    for i in range (j):
        print (i,end = "")
    print()

    
     #square pattern
num = int(input("enter the limit:"))
for j in range (num):
     for i in range (num):
         print("*",end ="")
     print()   

    #reverse pattern
num = int(input("enter the limit"))
for i in range(num):
    for j in range(num-i):
        print("*",end="")
    print()


#pyramid pattern
print("pyramid pattern output\n")
for i in range(num):
    print()
print ("pyramid pattern output\n")
num = int(input("enter the limit :"))
for j in range(num):
    print(" " *(num-j),end ="")
    for i in range(j+1):
        print("*", end =" ")
    print()
'''

ICICI_saikumar_ac_details={"Name": "saikumar", "ATM PIN" : "0066","balance":10000}
print ("welcoming to ICICI ATM")
print("please insert your ATM card")
ICICI_user_pin =input("please enter the 4 digits ATM pin")
if len(ICICI_user_pin)==4:
    if ICICI_user_pin in ICICI_saikumar_ac_details['ATM PIN']:
        print("pin is correct")
        user_choice = int(input("enter \n1.withdraw:"))
        if user_choice ==1:
            money_w= int(input("enter money you want to withdraw: "))
            if money_w <=ICICI_saikumar_ac_details['balance']:
                ICICI_saikumar_ac_details['balance']-= money_w
                print("balance", ICICI_saikumar_ac_details['balance'])
            else:
                print("insufficient")
      
    else :
        print("you have entered the invalid pin")
else :
     print ("please enter the correct pin")   

