#practice for login register

# usernames = [{'Grishma': 'grishma123'}, {'Fatima': 'fatima123'}, {'Shyam': 'shyam123'}]
# choice = input("Enter 1 for register, 2 for login, 3 for exit:")
# match choice: #match case statement
#     case '1':
#         username = input("Enter your username:")
#         password = input("Enter your password:")
#         dict1 = {username:password}
#         usernames.append(dict1)
#         print(usernames)
#     case '2':
#         username = input("Enter your username:")
#         if username in usernames:
#             print("Login successfull")

#         else:
#            print("Login failed")
#     case '3':
#          print("Exit from the program")
#     case _:
#         print("Invalide choice")
#break => only used within loop                            
#dict got append to the list and with previous dict shown and present too in the output 


# usernames = [{'Grishma': 'grishma123'},{'Mohit': 'mohit123'}]
#  #After register and running the code, the dict is copy and pasted here, so we can login 
# choice = input("Enter 1 for register, 2 for login, 3 for exit:")
# match choice: #match case statement
#      case '1':
#           username = input("Enter your username:")
#           password = input("Enter your password:")
#           dict1 = {username:password}
#           usernames.append(dict1)
#           print(usernames)
#      case '2':
#            username = input("Enter your username:")
#            password = input("Enter your password:")
#            for user in usernames:
#                 if username in user and user.get(username) == password:
#                      print("Login successfull")
#                      break 
#                 else:
#                      print("Login failed")
#      case '3':
#            print("Exit from the program")
#      case _:
#            print("Invalid choice")   



# user_credentials = [{'Fatima': 'fatima123'}, {'Shyam': 'shyam123'}, {'Grish': 'grish123'}, {'Mohit': 'mohit123'}, {'grishma': 'grishma123'}] #list where dictionary will be stored after register
# while True: #boolean true or false
#  choice = input("Enter 1 for Register, 2 for Login, 3 for Exit: ")
#  match choice:
#         case '1':
#             #code to register user
#             username = input("Enter your Username:")
#             password = input("Enter your Password:")
#             dict_cred = {username : password} #dictionary created 
#             user_credentials.append(dict_cred) #append each dict in the list
#             print(user_credentials)
#         case '2':
#             #code to login user
#             username = input("Enter your Username:")
#             password = input("Enter your Password:")
#             for cred in user_credentials: #loop in the list of dictionary
#              print(cred)
#              if username in cred and cred.get(username) == password:
#                 #get()=> return the value of the specified key
#                 print("Login Successful")
#                 break
#              else:
#                 print("Login Failed")
#         case 3:
#           print("Exiting the program")  
#           break
#         case _:
#           print("Invalid Choice") 