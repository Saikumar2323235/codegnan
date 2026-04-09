'''functions()
-----------------------------------
--> this is a block of code which is reusable
--> thw types 1.built_in or in build-in
              2. user define
 
1. built-in or in - build
--------------------
-->they comes with program and those are already defined....
eg..
----
print(),sum(), map()...........

 2 . user define
 -----------------
 --> this is created by person who is developing or using for development

 note ;_
 -->
 its starts with def keyboard followed by func name
 -->
 and it has calling fuction ....

 syntax :-
 def func_name(a,b)--->parameters 
   *****************************
   *****************************
   *****************************
   func_name()..........arguments

even or odd number checking in user define----------------------
def check_even_odd(n):
   if n %2==0:
    print("even number")
   else:
    print ("odd number")
num = int(input("enter a number :"))
check_even_odd(num)
--------------------------------------------------------------------   
num =int(input("enter a number : "))
def check_even_odd(num):
    if num % 2==0:
        print("even number")
    else:
        print("odd number")
check_even_odd(num)   
--------------------------------------------------------------------
ways to pass arguments in calling function

required arguments
-----------------------------------
it should match the same number variables in calling the def

num =9
num_2=10
def add (num,num_2):
    print(num)
add (num,num_2)
------------------------------------------------------------------
Default arguments

my_name="sai"
def sum_num(my_name):
    print(my_name)
sum_num(my_name="kumar")
sum_num(my_name="motupalli")
----------------------------------------------------------------
n = int(input("enter a number"))
def even(n):
   if n%2==0 :
      print("even number")
   else :
      print(" odd number")
even(n)

def prime_num(num,count):
    for j in range(1,num+1):
        if num % j == 0:
            count+=1
    if count ==2:
        print(f"{num} is a prime")
    else:
        print(f"{num} is not a prime")
prime_num(num=9,count=0)
prime_num(num = 47, count = 0)

----------------------------------------------------------------
Keyword arguments
---> above num = 47 is called key word arguments
def any(num,num_3,num_2):
    print(f"num= {num}, num_2={num_2},num_3={num_3}")
any(num_2=7,num=0,num_3=90)
----------------------------------------------------------------

def name(**candidate_):
    print(candidate_[2])
name("teja","sai","shekar")
----------------------------------------------------------------
recursion is a programming technique where a function calls itself either directly or
indirectly to solve a problem by breaking it into smaller , simpler subproblems .
recurssion is a espically useful for problems that can be divided into identical small tasks such
as mathematical calculations , tree traversal or divide and conquer algorithms.

def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("Enter 4 digit PIN: ")

        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print("Welcome to the ATM")
            return True
        else:
            self.remaining_attempts -= 1

            if self.remaining_attempts > 0:
                print(f"Invalid PIN. Attempts left: {self.remaining_attempts}")
            else:
                print("Card blocked. Please contact customer care")
                return False   
--------------------------------------------------------------------------------------
any = "Python is a program language"
vowel_list =[]
COn_list =[]
def Vowel_con(any,Vowel_list,COn_list):
    for j in any:
        if j in "AEIOUaeiou":
            Vowel_list.append(j)
        else:
            COn_list.append(j)
    print(f"{vowel_list} these are all vowel in the string")
Vowel_con(any,vowel_list,COn_list)
--------------------------------------------------------------------------------------
ICICI_saikumar_ac_details = {
    "Name": "saikumar",
    "ATM PIN": "0066",
    "balance": 10000
}

print("Welcome to ICICI ATM")
print("Please insert your ATM card")

ICICI_user_pin = input("Please enter the 4 digit ATM PIN: ")

# PIN validation
if len(ICICI_user_pin) == 4:
    if ICICI_user_pin == ICICI_saikumar_ac_details["ATM PIN"]:
        print("PIN is correct")

        user_choice = int(input("Enter:\n1. Withdraw\n2. Deposit\n"))

        # ✅ Withdraw
        if user_choice == 1:
            money_w = int(input("Enter money you want to withdraw: "))

            if money_w <= ICICI_saikumar_ac_details["balance"]:
                ICICI_saikumar_ac_details["balance"] -= money_w
                print("Transaction successful")
                print("Remaining balance:", ICICI_saikumar_ac_details["balance"])
            else:
                print("Insufficient balance")

        # ✅ Deposit
        elif user_choice == 2:
            deposit_m = int(input("Enter money you want to deposit: "))

            # condition from your image code
            if deposit_m % 100 == 0 and deposit_m >= 500:
                ICICI_saikumar_ac_details["balance"] += deposit_m
                print(f"You have deposited {deposit_m}")
                print("Total balance:", ICICI_saikumar_ac_details["balance"])
            else:
                print("Invalid deposit amount (minimum 500 and multiples of 100 only)")

        # ✅ Invalid choice
        else:
            print("Invalid option selected")

    else:
        print("You have entered an invalid PIN")

else:
    print("Please enter a valid 4-digit PIN")
----------------------------------------------------------------------'''
