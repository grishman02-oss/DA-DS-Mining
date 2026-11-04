#login register using file

#Register flow
#Ask username password from user
#Write the dictionary of username:password in file:
#We can only write string or json in file

#login flow
#Ask username password from user
#Read all creds in the file
#We can read the cred in the form of string or json
#Check for each cred if username and password matches or not
#login successfull if matched else login failed

# def operation(method):
#     username = input("Enter your username:")
#     password = input("Enter your password:")
#     if method == "register":
#         #register
#         pass
#     else:
#         #login 
#         pass


# def operation(method):
#     username = input("Enter your username:")
#     password = input("Enter your password:")
#     if method == "register":
#         #register code
#         dict_cred = {username:password}
#         file = open("Credentials.txt","a")
#         file.write(dict_cred)
#         file.close()  #doesnot run cause we can't write dictionary directly into the file
#     else:
           #login code
#           pass
        #'write arguments' must be string not dictionary
        #since python treat json as string and its structure is almost same to dictionary.
        #so change dictionary to json

#To convert it we need to import json
#json has two functions
#1. json.dumps()=> convert dictionary to json
#2. json.loads()=> convert json to dictionary

import json
def atm_task(method, username):
     file = open("Credentials2.txt", "r")
     content = file.read()
     file.close()
     list_creds = content.split("*")
     credentials = ""
     for i in list_creds:
                 if i != "":
                     dict_i = json.loads(i)
                     if dict_i.get("username")==username:
                          curr_balance = dict_i.get("balance")

                          if method == "view":
                            print(f"Your current balance is{curr_balance}") 
                            return 
                          else:
                            amount = float(input("Enter the amount:"))
                            if method == "add":
                                 new_balance = curr_balance + amount
                                 dict_i.update({"balance":new_balance})                      
                            else:
                                 new_balance = curr_balance - amount
                                 dict_i.update({"balance":new_balance})
                            credentials += json.dumps(dict_i)+"*"     
                     else:
                         credentials += json.dumps(dict_i)+"*"  
     file = open("Credentials2.txt", "w")
     file.write(credentials) 
     file.close()  
     
                                 
def operation(method):
    username = input("Enter your username:")
    password = input("Enter your password:")
    if method == "register":
        #register code
        #dict_cred = {username:password}
        dict_cred = {"username":username, "password":password, "balance":0}
        #file = open("Credentials.txt","a")
        file = open("Credentials2.txt","a")
        json_cred = json.dumps(dict_cred)
        file.write(json_cred + "*") # + and * is used to separate each credentials 
        file.close()

    else:
        #login code
        file = open("Credentials2.txt", "r")
        content = file.read()
        file.close()
        print(content)
        print(type(content))
        list_creds = content.split("*")
        is_login = False
        for i in list_creds:
            #print(i)
            if i != "":
                dict_i = json.loads(i)
                #if username in dict_i and dict_i.get(username) == password:
                if dict_i.get("username")==username and dict_i.get("password")==password:
                    print("Login successfull")
                    #break
                    is_login=True
                    while True:
                         choice = input("Enter 1 to add balance, 2 to withdraw balance, 3 to view balance, 4 to exit:")
                         match choice:
                              case '1':
                                   #add
                                   atm_task("Add", username)
                              case '2':
                                   #withdraw
                                   atm_task("withdraw", username)
                              case '3':
                                   #view
                                   atm_task("view", username)
                              case '4':
                                   print("Thank you for using our atm")
                                   break
                              case _:
                                   print("Invalid Input")
        #else:
        if not is_login:
                    print("Login failed")    

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
            print("Invalid Input")  

#Python Method: split() => dherai string xa vaney list ma convert hunca each words into an item
# here we split based on *                 

