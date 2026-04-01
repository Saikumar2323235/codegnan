'''table_num=int(input("Enter the required table number"))
for j in range(1,11):
    print(f"{table_num}*{j}= {table_num*j}" )


    #finding no of capitals and smaller aplhabets in giving strings


string : [String is immutable cant be modified]
string in a sequence of character
that are closed in quotes {'',"",}
 ex :- a = "python"
 b ="sai"
 count()
join()
strip()
replace()
split()
capatalize()
casefold()
isaplha()
is decimal()
is digit()
is lower()
is upper()

an = "Python IS a Programming Language"
count_u=0
count_l=0
for ch in an:
    if ch.isupper():
        count_u+=1
    elif ch.islower():
        count_l+=1
print(f"there are the total number of {count_u} Cap l")
print(f"there are the total number of {count_l} small l")



an = "Python IS a Programming Language"
Cap_l= []
Small_l=[]
for ch in an:
  if ch.isupper():
      Cap_l.append(ch)
  elif ch.islower():
      Small_l.append(ch)
print(f"{Cap_l} contain all the Cap L")
print("f{Small_l} contain all the Small L")

ICICI_saikumar_ac_details={"Name": "saikumar", "ATM PIN" : "0066" }
print ("welcoming to ICICI ATM")
print("please insert your ATM card")
ICICI_user_pin =input("please enter the 4 digits ATM pin")
if len(ICICI_user_pin)==4:
    if ICICI_user_pin in ICICI_saikumar_ac_details['ATM PIN']:
       print ("the correct pin")
    else :
        print("you have entered the invalid pin")
else :
     print ("please enter the correct pin")   

        '''

per_num= int(input("enter a number"))
fact_all = 0
for j in range(1,per_num):
    if per_num % j == 0:
        fact_all +=j
if fact_all == per_num:
    print(f"{per_num} is the perfect num")
else:
    print(f"{per_num} is not a perfect num")
        
