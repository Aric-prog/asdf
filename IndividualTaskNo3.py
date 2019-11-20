def outputText(num1,num2,num3):
    print("Class 1 : " + str(num1))
    print("Class 2 : " + str(num2))
    print("Class 3 : " + str(num3))

class1 = 32
class2 = 45
class3 = 51

group1 = class1 // 5
group2 = class2 // 7
group3 = class3 // 6

leftover1 = class1 % 5
leftover2 = class2 % 7
leftover3 = class3 % 6

print("Number of students in each group.")
outputText(group1,group2,group3)

print("Number of students leftover.")
outputText(leftover1,leftover2,leftover3)
