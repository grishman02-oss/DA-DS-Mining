#login register with ATM task

credentials = []
def operation(method):
    username = input("Enter your username:")
    password = input("Enter your password:")
    if method == 'register':
     #register code
     #dict_cred = {username:password}
     dict_cred = {"username":username, "password":password, "balance":0}
     credentials.append(dict_cred)
     print("Registration Successfull")
     print(credentials)
    else:
       for cred in credentials:
          if username == username and cred.get(username)==password:
             print("Login successfull")
             user_atm = input("Do you want to use ATM? (y/n):")
             if user_atm.lower() == "y":
               while True:
             #ATM Menu
                  atm_choice = input("Enter 1 to add balance, 2 to withdraw, 3 to view balance, 4 to exit:")
                  match atm_choice:
                   case '1':
                    #add
                    pass
                   case '2':
                    #withdraw
                    pass
                   case '3':
                   #view
                     for cred in credentials:
                        if cred.get(username)==username:
                           print(f"Current Balance = {cred.get("balance")}") 
                    
                   case '4':
                    print("Thank you for using our atm")
                    break
                   case _:
                    print("Invalid choice")
                    
                   

             else:
                return
                

             break
          else:
             print("Login failed")

             #login code
while True:
      choice = input("Enter 1 for register, 2 for login, 3 for exit:")
      match choice:
            case '1':
               operation('register')
            case '2':
               operation('login')
            case '3':
               print("Thank you")
               break
            case _:
               print("Invalid Choice")      
        

    