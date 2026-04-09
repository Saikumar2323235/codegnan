'''lambda function()
-----------------------
--> this is also called anonymous function ..
--> a lambda function can take a number of arguments but have only one expression

syntax
---------
          lambda (keyword) arguments : expression
             
any = lambda so :so +10
print(any(16)) #output==-26
print(any(10))
some = lambda an , how : how -an
print (some(10,20)) # we can pass any arguments at a time like this
                    #by increasing n:of arguments after lambda keyword and pass
                    #that no of arguments while calling

some = lambda an, how , do : (how- an)*do
print(some(4,9,2))

money = lambda rupee,paisa,dollar : (dollar-rupee)/paisa
print(money(50,25,100))

--------------------------------------------------------------------------------
list comprehension:
--> this is offers the shorter syntax when you want to create a new left from the existing list
from the existing list
syntax
------ variable_name = [expression loop and addition]


oldlist = [1,2,3,4]
newlist =[j for j in oldlist]
print(newlist)

evenlist = [j for j in oldlist if j%2==0]
print("even list",evenlist)'''

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

        user_choice = int(input("Enter:\n1. Withdraw\n2. Deposit\n3. Change PIN\n"))

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

            if deposit_m % 100 == 0 and deposit_m >= 500:
                ICICI_saikumar_ac_details["balance"] += deposit_m
                print(f"You have deposited {deposit_m}")
                print("Total balance:", ICICI_saikumar_ac_details["balance"])
            else:
                print("Invalid deposit amount (minimum 500 and multiples of 100 only)")

        # ✅ Change PIN (from your image logic)
        elif user_choice == 3:
            attempts_remaining = 3

            while attempts_remaining > 0:
                old_pin = input("Enter your old ATM PIN: ")

                if len(old_pin) == 4:
                    if old_pin == ICICI_saikumar_ac_details["ATM PIN"]:
                        new_pin = input("Enter a new 4 digit ATM PIN: ")

                        if len(new_pin) == 4:
                            ICICI_saikumar_ac_details["ATM PIN"] = new_pin
                            print("New PIN is updated successfully")
                            break
                        else:
                            print("New PIN must be 4 digits")
                    else:
                        attempts_remaining -= 1
                        print("Wrong PIN. Attempts left:", attempts_remaining)
                else:
                    print("PIN must be 4 digits")

            if attempts_remaining == 0:
                print("Too many wrong attempts. Try again later.")

        # ✅ Invalid choice
        else:
            print("Invalid option selected")

    else:
        print("You have entered an invalid PIN")

else:
    print("Please enter a valid 4-digit PIN")
