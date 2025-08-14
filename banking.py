choice = 1
bankbalance = 0
amount = 0


while choice >= 0:
    print("    BANKING MENU   ")
    print("             1. DEPOSIT               ")
    print("             2. WITHDRAWAL            ")
    print("             3. CHECK BALANCE         ")
    print("             4. EXIT                  ")

    print("Choose any option (1, 2, 3, 4):")
    n = int(input("Enter choice: "))

    match n:
        case 1:
            amount = float(input("How much money do you want to deposit? "))
            if amount < 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                bankbalance += amount
                print(f"You have deposited {amount}. New balance: {bankbalance}")

        case 2:
            amount = float(input("How much money do you want to withdraw? "))
            if amount < 0:
                print("Invalid amount. Please enter a positive number.")
            elif amount > bankbalance:
                print("Insufficient Balance.")
            else:
                bankbalance -= amount
                print(f"You have withdrawn {amount}. Remaining balance: {bankbalance}")

        case 3:
            print("Your bank balance is:", bankbalance)

        case 4:
            print("Thank you for using the banking system.")
            choice = -1

        case _:
            print("Invalid choice. Please try again.")



#good job babu okk