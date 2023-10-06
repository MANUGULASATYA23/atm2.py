acctnumber=123456
pinnumber=1234
balance=150000

useracctnumber = input("enter accnumber:")
userpinnumber = input("enter pinnumber:")

if(useracctnumber.isnumeric() and userpinnumber.isnumeric()):
    #check acc number, pin number matched
    if(acctnumber == int(useracctnumber) and pinnumber == int(userpinnumber)):#matched asked a question
        option = input("enter a option 1. withdraw 2. check balance 3. deposit")
        if(option == "1" or option == "2" or option == "3"):
            if(option == "1"):#withdraw
                withdrawamount = input("enter amount to be withdraw:")  #check withdraw amount
                if(withdrawamount.isnumeric()):
                    withdrawamount = int(withdrawamount)
                    if(balance >= withdrawamount):
                        balance -= withdrawamount
                        print(f'balance amount: {balance}')
                    else:
                        print("in sufficient balance.")
                else:
                    print("entered invalid number.")
            elif(option == "2"):
                #check balance
                print(f'balance amount: {balance}')
            elif(option == "3"): #deposit
                depositamount = input("enter amount to be deposit:")
                balance += int(depositamount)
                print(balance)
        else:
            print("you have choosen invalid option.")
    else:
        print("enter valid account number and pin number.")
else:
    print("enter only numbers.")


