#Functions
#Function is a block of code that performs a specific task.
#functions are used to avoid repetition of code and to make the code more organized and readable.
#Function makes our code structured
#Function helps in code reusability
#To define a function we use the keyword 'def' followed by the function name and parentheses.
#syntax:
#def function_name(parameters):
#block of code

#Parameters are the variables that receive the value for the function
#def sum(a,b):
    #print(a+b)

#By only defining the function doesnot works, we need to call the function.
# To call a function, function_name(arguments) is used.
# Arguments are the values passed to the function
# sum(10,20) function call 
# Positional Arguments: The parameter receives the value according to the position
# Keyword Arguments: The argument passed in key=value format.
# key should be the parameter name and value should be the value to be passed to the parameter. 
# sum(b=20, a=10)
# 
# local variable: The variable defined inside the function is a local variable
# can be accessed only inside the function
# Global variable: The variable defined outside the function is global variable.
# can be accessed from anywhere, either from inside the function or from outside the function


#Task: update calculator program and login register program using function
#DRY : Don't Repeat Yourself

#Login Register Program
#Register flow:
#Ask username and password from user
#Convert them into dictionary
#Append the dictionary in the list

#Login flow:
#Ask username and password from user
#Loop in the list of dictionary
#Check if username == username and dict.get(username) == password

credentials = [] #list

def operation(method):
    username = input("Enter your username:")
    password = input("Enter your password:")
    if method == "register":
        #register code
        dict_cred = {username:password}
        credentials.append(dict_cred)
        print(credentials)
        print("Registration Successfull")
    else:
        for cred in credentials:
            if username == username and cred.get(username) == password:
                print("Login Successfull")
                break
            else:
                print("Login failed")
                #login code

while True:
        choice = input("Enter 1 for register, 2 for login, 3 for exit:")
        match choice:
            case '1':
                operation("register") #function is called
            case '2':
                operation("login")
            case '3':
                print("Thank you") 
                break
            case _:
                print("Invalid choice")                      