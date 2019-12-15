from os import path

# for i in range(1,10):
#     temp = "newTextFile" + str(i)+".txt"
#     f = open(temp,"w+")
if(path.isfile("SecondAssignment/newTextfil.txt")):
    src = path.realpath("SecondAssignment/newTextfile.txt")

print(src)
a,b = path.split(src)
