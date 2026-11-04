#Pythong String Methods
#1. upper()-Converts everything to uppercase.
#2. lower()-Converts everything to lowercase.
#3. capitalize()-Makes the first letter uppercase.
#4. title()-Makes the first letter of each word uppercase.
#5. strip()-Removes unnecessary spaces from the beginning and end.
#6. replace()-Replaces one piece of text with another.
#7. split()-Breaks a string into a list.
#8. join()-Joins multiple strings together.
#9. count()-counts how many times something appear in a string
#11. startswith()-Checks whether a string starts with something(T/F)
#12. endswith()-Checks whether a string ends with something.


#University = "Tribhuvan University"
#print(University.upper()) #changes the text to upper case
#print(University.lower()) #changes the text to lower case

#book = "Software Engineering"
#print(book.capitalize()) # makes the first letter capital
#print(book.title()) #makes the first letter of each word uppercase

#name = "  grishma  neupane  "
#print(name.strip()) #removes unwanted spaces from the beginning and end

#text = "Stores a sequence of characters"
#print(text.replace("sequence", "order")) #replace one information with another
#print(text.split()) #break a string into a list

#subjects = ["C++", "JAVA", "OPPS", "Math"]
#result = ", ".join(subjects) #joins multiple string together
#print(result)
#SUBJECT = ("I LOVE JAVA")
#print(SUBJECT.find("JAVA")) #7 ANS, START COUNTING FROM 0 TILL J OF JAVA
#print(SUBJECT.count("V"))
#print(SUBJECT.startswith("Python")) #string starts from what to return true or false
#print(SUBJECT.endswith("JAVA"))

#13. isdigit()-Checks whether all characters are digits(T/F)
#14. isalpha()-Checks whether all characters are letters(T/F)
#15. isalnum()-Checks whether all characters are letters or numbers
#16. isspace()-Checks whether the string contains only spaces.
#17. islower()-Checks whether all letters are lowercase.
#18. isupper()-Checks whether all letters are uppercase.
#19. isdecimal()-Checks whether all characters are decimal.
#20. isascii()-Checks whether all characters are ASCII characters.
#21. isnumeric()-Checks whether all characters are numeric.
#22. isidentifier()-Checks whether the string can be used as a valid Python identifier (such as a variable name)
#23. isprintable()-Checks whether all characters are printable.
#24. istitle()-checks whether string follow rules of a title
#num = "abcd"
#print(num.isdigit())
#print(num.isalpha())
#print(num.isalnum())
#nums = "12345"
#print(nums.isdigit())
#nums1 = "abcd"
#print(nums1.isidentifier())
#n ="abc123"
#print(n.isalnum())
#print(n.isspace())

#a = " "
#print(a.isspace())
#b = "a b c d"
#print(b.isspace()) # true if it contains space only otherwise false

#c = "grisHMMmaaaa"
#print(c.encode())
#print(c.islower()) #all letter lower - true
#print(c.isupper())# all letter upper - true

#text = "data science course"
#print(text.encode()) # return an encoded version of the string

#name = "Grishma"
#print(name.center(15, "-"))
#print(name.casefold()) #convert string into lowercase

#25.format()- method allows you to put variables/values into a string using {} placeholders.
#26. center()-put the string in the center and fill the remaining space
#27. format_map()-put values using dictionary

country = "nepal"
place = "bharatpur"
text = "My country is {}. But i am actually from {}." 
print(text.format(country, place))

student = {
    "name" : "Grishma",
    "age" : 23,
    "course" : "BSC CSIT"
}
text1 = "My name is {name}. I am {age} years old and I study {course}."
print(text1.format_map(student))

#28. swapcase()-Changes uppercase → lowercase and lowercase → uppercase
#29. rfind()-Finds the last occurrence of something.
#30. index()-Similar to find().
#31. rindex()-Finds the last occurrence, similar to rfind()
#32. rsplit()-Splits from the right side.
#33. find()-finds the position of a piece of text
#34. splitlines()-Splits text at line breaks.
#35. lstrip()-Removes spaces from the left side.
#36. rstrip()-Removes spaces from the right side
#37. zfill()-Adds zeros to the left until the string reaches a specified length.
#38. ljust()-Moves the text toward the left and fills the remaining space
#39. rjust()-Moves the text toward the right and fills the remaining space.
#40.partition()-Splits a string into three parts:before separator, separator, after separator
#41. rpartition()-Similar to partition(), but searches for the separator from the right side.
#42. translate()-Replaces characters according to a translation table
#43. maketrans()-Creates a translation table that can be used with translate()


#swap = "SwAPCasE"
#print(swap.swapcase())

#fin = "data science course"
#print(fin.rfind("science"))
#print(fin.rfind("data"))
#print(fin.index("course"))
#print(fin.rindex("science"))
#print(fin.rsplit())

#fin1 = "data\nscience\ncourse"
#print(fin1.splitlines())

#fin2 = "  funnn workk  "
#print(fin2.lstrip())
#print(fin2.rstrip())

#num1 = "345"
#print(num1.zfill(8))
#print(num1.ljust(10,"-"))
#print(num1.rjust(10,"#"))

#text = "Recent flood cause devastating damage"
#print(text.partition("cause"))
#print(text.partition("damage"))
#print(text.rpartition("devastating"))

#txt = "abc-nhg-tyu"
#print(txt.rpartition("-"))

#trans = "doing translate methods"
#table = str.maketrans("t", "T")
#table = str.maketrans("translate", "changesss")
#print(trans.translate(table))

table = str.maketrans("abc", "123")

text = "abc"

print(text.translate(table))


str = input("Enter a string:")
length = len(str)
print(length)
print(str.upper())

movie = []
user = input("Enter your favorite movie:")
movie.append(user)
print(movie)
