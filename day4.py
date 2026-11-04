#Conditional Statements
# Statements executes according to the condition
# IF ELSE, LOOP, MATCH

#IF ELSE => executes the code according to the condition
# Syntax:
# if condition:
      #if condition is satisfied, statements to be executed
# else:
     # code to be executed when condition is false

age =   int(input("Enter your name:"))
if age > 18:
    print("You are an adult")
else:
    print("You are a kid")

#Types of IF ELSE
# 1. Simple If => Only if block is written
if age > 60:
     print("You are a old person")
# Condition satisfy bhayo vaney output aauxa like age=65 otherwise sastify
# bhayena vaney kei result aaudaina like age=20.
 
 
# 2. IF ELSE
if age>18:
   print("You are an adult")
else:
   print("You are a kid")


# 3. ELIF Ladder => use elif ladder when you have multiple conditions
percentage = float(input("Enter your percentage:"))
if percentage>90:
      print("A+")
elif percentage >= 80 and percentage < 90:
      print("A")
elif percentage >= 70 and percentage < 80:
      print("B+")
elif percentage >= 60 and percentage < 70:
      print("B")
else:
     print("Failed")


# Membership Operator => using if else here
usernames = ["Hari", "Shyam", "Rita", "Grishma", "Mohit"]
username = input("Enter your username: ")
if username in usernames:
     print("Username Found")
else:
     print("Username not found")          