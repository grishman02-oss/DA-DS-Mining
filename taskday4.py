#Create a list of usernames
#Input a username from the user
#Check if the username is present in the list or not

usernames = ["Abhi", "Shyam", "Grish", "Grishma", "Ram", "Sita"]
username = input("Enter your username: ")
if username in usernames :  #in => membership operator
    print("Username is found")
else:
    print("Username not found")    


if username not in usernames: #not in => membership operator
    print("name not found")
else:
    print("name found")    



#2. Create a dictionary of usernames and passwords,
#extract all the usernames from the dictionary and 	input username
#from the user and check if the 	username is present in the
# extracted list of usernames

users = {
    "Grishma" : "1245",  # usernames : password -> key:value pair
    "Shyam" : "abcg",
    "Abhi" : "12ds",
    "Ram" : "9111"
}

#extract all the usernames which is key so use key() method
print(users.keys()) # to extract usernames

Extractedusername = users.keys() #to extract usernames
print(Extractedusername)

username = input("Enter your username: ")
if username in Extractedusername :
    print("Username is present in the extractedusernames")
else:
    print("Username isnot present in the extractedusernames")    