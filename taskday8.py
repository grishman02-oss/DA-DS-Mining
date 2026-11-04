#task
## Task: 
# "Ujjwal Neupane"
#{"U":2,
 #"j":2,
 #"w":1,
 #"a":2,
 #"l":1,
 #"N":2,
 #"e":2,
 #"p":1,
 #" ":1
 #}


name = "Ujjwal Neupane"

count = {}
print(type(count))

for char in name:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print(count)        