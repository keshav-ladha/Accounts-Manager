accounts = {}
account_balance = {}
yesornot = input("Do You Want to add any account?: Y or N")
if yesornot == 'y' or yesornot == 'Y':
    accountname = int(input("Add Account Number:"))
    accountpass = int(input("Add Account Password:"))
    accounts[accountname] = accountpass
    account_balance[accountname] = 0
    print("You have successfully added Your Account.....")
yesornot2 = input("Do You Want To Access Your Account?: Y or N")
if yesornot2 == 'y' or yesornot2 == 'Y':
    account_number = int(input("Enter Your Account Number:"))
    account_password = int(input("Enter Your Account Password:"))
    print("We have Successfully Accessed Your Account Details")
    print("Your Current Account Balance is ", account_balance[account_number])
    while True:
        todo = int(input("What Do you want to do:\n1.Withdraw Funds\n2.Deposit Funds\n3.Check Balance\n4.Exit"))
        if todo == 1:
            funds = int(input("Amount You Want To Withdraw?:"))
            account_balance[account_number] = account_balance[account_number] - funds
            print("\nYour New Account Balance Is ", account_balance[account_number], end="$\n")
        elif todo == 2:
            fundsdepo = int(input("Amount You Want To Deposit?:"))
            account_balance[account_number] = account_balance[account_number] + fundsdepo
            print("\nYour New Account Balance Is ", account_balance[account_number], end="$\n")
        elif todo == 3:
            print("\nYour Current Balance is ", account_balance[account_number], end="$\n")
        elif todo == 4:
            print("Thanks For Joining Us!")
            exit()