#print a multiplication table of the number that is input by the user

#using for loop
number = int(input("Enter your number:"))
for i in range(1,11):
     result = number * i
     print(number, "x", i, "=", result)

#using function

def table(number):
     for i in range(1,11):
         result = number * i
         print(number, "x", i, "=", result )

number = int(input("Enter a number:"))
table(number) 


#Check if the given number is even or odd

num = int(input("Enter a number:"))
if num%2 == 0:
     print("Even Number")
else:
     print("Odd Number")  


#Check if the given number is palindrome or not
#A palindrome is a number that reads the same forward and backward

number = input("Enter a number:")

if number == number[::-1]:
     print("Palindrome number")
else:
     print("Not palindrome")    


#Make a simple login system without registration using functions
username = "Grishma"
password = "grishma123"

def login():
    user = input("Enter your username:")
    pwd = input("Enter your password:")

    if user == username and pwd == password:
        print("login successfull")
    else:
        print("Login failed")

login() 


#Make a login system using registration using function
usernames_list = [{'Grishma': 'grishma123'}, {'Purvi': 'purvi123'}, {'Fatima': 'fatima123'}, {'Hari': 'hari123'}]
def register():
    username = input("Enter your username:")
    password = input("Enter your password:")

    dict = {username:password}
    usernames_list.append(dict)
    print(usernames_list)
    print("Registration Successfull")

def login():
      username = input("Enter your username:")
      password = input("Enter your password:")  

      for cred in usernames_list:
        if username in cred and cred.get(username) == password:
            print("Login successfull")
            break
        else:
            print("Login failed")

while True:
    choice = input("Enter 1 for registration, 2 for login, 3 for exit:")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exit from the program")
        break
    else:
        print("Invalid choice")                        


#Print all the even number in a list of numbers

numlist = [12,13,15,19,36,20,5,6,8]

def even_number():
    for i in numlist:
        if i%2 == 0:
            print("Even")
        else:
            print("Odd") 

even_number()            

    

        