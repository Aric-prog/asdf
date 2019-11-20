T = (1,2,3,4) #is a tuple
L = [1,2,3,4] #is a list

print(id(T)) # prints out the memory adress

#tuple is immutable 
#for example, below will produce an error
#T[0] = 2
#but 
T = (2,3,4,5)
#works and it assigns the new value in a new memory block
print(id(T))

#btw, since python is smart,
print(id(T[0]) == id(L[1]))
#they occupy the same memory adress

#1st Version