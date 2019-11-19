var = True
difference = 0
number = 5
count = 5
string = ""
for i in range(number):
    string += "*"
    print(string)

print("")

for i in range(number):
    for i in range(count):
        print("*" , end = '')
    count -= 1    
    print("")

print("")

count = 5
for i in range(number):
    difference = 5 - count
    for i in range(difference):
        print(" ", end = '')
    
    for i in range(count):
        print("*" , end = '')
    count -= 1    
    print("")
    
print("")

for i in range(number):
    difference = 4 - count
    if(count <5):
        count += 1 
    for i in range(difference):
        print(" ", end = '')
    
    for i in range(count):
        print("*" , end = '')
    
    print("")

print("")
lolspaceiguess = " "
starthing = "*"
height = 5
alternator = True
counter = 1
difference = 0

for i in range(height):
    difference = 5 - counter
    
    print(lolspaceiguess * (difference//2), end = '')
    print(starthing * counter)

    if(counter == 5):
        alternator = False

    if(alternator == True):
        counter +=2
    if(alternator == False):
        counter -=2
