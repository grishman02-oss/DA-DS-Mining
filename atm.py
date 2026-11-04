#ATM task
#After login successfull => function and without function


#using if elif else statment
Balance = int(input("Enter your balance:"))
choice = input("Enter 1 for withdraw, 2 for deposit, 3 for check balance, 4 for exit:")

if choice == '1':
    withdraw_amount = int(input("Enter amount to withdraw:"))
    if withdraw_amount <= Balance:
        Balance = Balance - withdraw_amount
        print("Your remaining balance is:", Balance)
        print("Withdrawal successfull")
    else:
        print("Insufficient balance")

elif choice == '2':
    deposit_amount = int(input("Enter amount to deposit:")) 
    Balance = Balance + deposit_amount 
    print("Your New Balance is:", Balance)
elif choice == '3':
    print("Your Balance is :", Balance)
else:
    print("Invalid choice")



#using function
balance = float(input("Enter your balance:"))

def withdraw(balance):  #function defined
    amount = float(input("Enter amount to withdraw:"))
    if amount <= balance:
        balance = balance - amount
        print("Your remaining balance is:", balance)
    else:
        print("Insufficient balance")
            

def deposit(balance):
    dp_amount = float(input("Enter amount to deposit:"))
    balance = balance + dp_amount
    print("Your New Balance is:", balance)

def check_balance(balance):
    print("Your Balance is:", balance)

choice = input("Enter 1 for withdraw, 2 for deposit, 3 for check balance, 4 for exit:")
match choice:
    case '1':
        withdraw(balance) #function called
    case '2':
        deposit(balance)
    case '3':
        check_balance(balance)
    case '4':
        print("Thank you")
    case _:
        print("Invalid choice")       


#atm login 
account = {
    "Grishma":1234,
    "Uditi":9876,
    "Ram":9854,
    "Shyam":5643
}  




balance = float(input("Enter your balance:"))

def withdraw(balance):  #function defined
    amount = float(input("Enter amount to withdraw:"))
    if amount <= balance:
        balance = balance - amount
        print("Your remaining balance is:", balance)
    else:
        print("Insufficient balance")
            

def deposit(balance):
    dp_amount = float(input("Enter amount to deposit:"))
    balance = balance + dp_amount
    print("Your New Balance is:", balance)

def check_balance(balance):
    print("Your Balance is:", balance)

while True:
    username = input("Enter your username:")
    pin = input("Enter your pin:")
    choice =  input("Enter 1 for withdraw, 2 for deposit, 3 for check balance, 4 for exit:")
    for i in account:
        if username in i and i.get(username)==pin:
            print("Login successfull")
            break
        else:
            print("Login failed")



    