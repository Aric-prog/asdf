invitedNames = ['Jesus' , 'Mao Zhedong', 'Genghis Khan']

def sendInvite():
    for i in range(len(invitedNames)):
        print(invitedNames[i], end = ' , ')
    print(" is invited to the party")

sendInvite()

print(invitedNames.pop(0) + " couldn't make it\n")
invitedNames.insert(0,'God')
print(invitedNames[0] + " is invited instead")

print("\nLmao bigger table")

invitedNames.append('Hideo Kojima')
invitedNames.append('Reggie')
invitedNames.append('Obama')

print(invitedNames)
sendInvite()

print("\nLOL NO TABLES")

for i in range(4):
    print("Sorry " +invitedNames.pop(0)+ ", you're not invited anymore")

print("")
sendInvite()

del(invitedNames[0]) 
del(invitedNames[0])

print(invitedNames)
