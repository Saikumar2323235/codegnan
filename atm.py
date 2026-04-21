ICICI_saikumar_ac_details = {
    "Name": "saikumar",
    "ATM PIN": "0066",
    "balance": 10000
}

print("Welcome to ICICI ATM")
print("Please insert your ATM card")

attempts_remaining = 3

while attempts_remaining > 0:
    ICICI_user_pin = input("Enter your 4 digit ATM PIN: ")

    if len(ICICI_user_pin) != 4:
        print("Please enter a valid 4-digit PIN")
        continue

    if ICICI_user_pin == ICICI_saikumar_ac_details["ATM PIN"]:
        print("✅ PIN is correct")

        while True:
            print("\nChoose an option:")
            user_choice = int(input("1. Withdraw\n2. Deposit\n3. Change PIN\n4. Exit\n"))

            # ✅ Withdraw
            if user_choice == 1:
                money_w = int(input("Enter amount to withdraw: "))

                if money_w <= ICICI_saikumar_ac_details["balance"]:
                    ICICI_saikumar_ac_details["balance"] -= money_w
                    print("Transaction successful")
                    print("Remaining balance:", ICICI_saikumar_ac_details["balance"])
                else:
                    print("Insufficient balance")

            # ✅ Deposit
            elif user_choice == 2:
                deposit_m = int(input("Enter amount to deposit: "))

                if deposit_m >= 500 and deposit_m % 100 == 0:
                    ICICI_saikumar_ac_details["balance"] += deposit_m
                    print(f"You deposited {deposit_m}")
                    print("Total balance:", ICICI_saikumar_ac_details["balance"])
                else:
                    print("Invalid deposit (min 500 & multiples of 100)")

            # ✅ Change PIN (with attempts like image)
            elif user_choice == 3:
                pin_attempts = 3

                while pin_attempts > 0:
                    old_pin = input("Enter your old PIN: ")

                    if old_pin == ICICI_saikumar_ac_details["ATM PIN"]:
                        new_pin = input("Enter new 4 digit PIN: ")

                        if len(new_pin) == 4:
                            ICICI_saikumar_ac_details["ATM PIN"] = new_pin
                            print("✅ PIN updated successfully")
                            break
                        else:
                            print("PIN must be 4 digits")
                    else:
                        pin_attempts -= 1
                        print(f"❌ Wrong PIN. Attempts left: {pin_attempts}")

                if pin_attempts == 0:
                    print("⚠ Too many wrong attempts. PIN change blocked.")

            # ✅ Exit
            elif user_choice == 4:
                print("Thank you for using ICICI ATM")
                break

            else:
                print("Invalid option")

        break  # Exit main PIN loop after success

    else:
        attempts_remaining -= 1
        print(f"❌ Invalid PIN. Attempts left: {attempts_remaining}")

if attempts_remaining == 0:
    print("🚫 Card blocked due to too many wrong attempts")
