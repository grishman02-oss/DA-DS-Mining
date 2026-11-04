#Login Register Program

#Register flow:
#Ask Username and Password from user
#Convert them into dictionary
#Append the dictionary in the list

#Login Flow:
#Ask username and password from user
#Loop in the list of dictionary
#Check if username == username and dict.get(username) == password

#Note: Use while loop so that whenever user wants to exit 

user_credentials = [{'Fatima': 'fatima123'}, {'Shyam': 'shyam123'}, {'Grish': 'grish123'}, {'Mohit': 'mohit123'}, {'grishma': 'grishma123'}] #list where dictionary will be stored after register
while True: #boolean true or false
 choice = input("Enter 1 for Register, 2 for Login, 3 for Exit: ")
 match choice:
        case '1':
            #code to register user
            username = input("Enter your Username:")
            password = input("Enter your Password:")
            dict_cred = {username : password} #dictionary created 
            user_credentials.append(dict_cred) #append each dict in the list
            print(user_credentials)
        case '2':
            #code to login user
            username = input("Enter your Username:")
            password = input("Enter your Password:")
            for cred in user_credentials: #loop in the list of dictionary
             print(cred)
             if username in cred and cred.get(username) == password:
                #get()=> return the value of the specified key
                print("Login Successful")
                break
             else:
                print("Login Failed")
        case 3:
          print("Exiting the program")  
          break
        case _:
          print("Invalid Choice")      

               

