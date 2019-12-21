from statistics import mean
sortedNames : list =[]
sortedTable = []
with open('data.txt',mode='r') as f:
    lines = f.readlines()
    index = 0
    for a in lines:
        lines[index] = a.replace('\n',"").split('#')
        index+=1
    
for i in range(len(lines)):
    sortedNames.append(lines[i][1])
sortedNames.sort()

for name in sortedNames:
    for element in lines:
        if(name in element):
            sortedTable.append(element)
    
def checkUnique(candidateID):
    for i in sortedTable:
        if(candidateID in i):
            return True
        else:
            return False 

def showTable():
    print("|ID"+"     "+"\t"+"|Name"+"   "+"\t"+"|Position"+"   "+"\t"+"|Salary"+"   "+"\t"+"|".expandtabs(50))
    for x in sortedTable:
        for y in x:
            print("|"+y+"   "+" \t",end="")
        print("|")
        
def addStaff():
    roleList = ['Staff','Officer','Manager']
    newEmployeeData = []
    IDEntered=False
    while(not IDEntered):
        IDTempStr : str = input("Input employee ID[SXXXX] : ")
        if(len(IDTempStr) !=5):
            continue
        elif(IDTempStr[0] !='S'):
            continue
        elif(checkUnique(IDTempStr)):
            continue

        try:
            tester = int(IDTempStr[1:])
        except ValueError:
            continue
        else:
            newEmployeeData.append(IDTempStr)
            print(newEmployeeData)
            IDEntered=True
    
    nameEntered = False
    while(not nameEntered):
        nameTempStr = input("Input employee Name[0..20] : ")
        if(len(nameTempStr)<=20 and len(nameTempStr)> 0):
            newEmployeeData.append(nameTempStr)
            nameEntered=True
        else:
            continue

    jobEntered = False
    while(not jobEntered):
        jobTempStr = input("Input position[Staff|Officer|Manager] : ")
        if(jobTempStr.lower() in roleList):
            newEmployeeData.append(jobTempStr.title())
            jobEntered = True
        else:
            continue
    
    salaryEntered = False
    while(not salaryEntered):
        salaryTempStr = input("Input salary for " +newEmployeeData[2]+" : ")
        if(newEmployeeData[2].lower() == "staff"):
            if(salaryTempStr >= 3500000 and salaryTempStr<=7000000):
                newEmployeeData.append(salaryTempStr)
                salaryEntered = True
        if(newEmployeeData[2].lower() == "officer"):
            if(salaryTempStr >= 7000001 and salaryTempStr<=10000000):
                newEmployeeData.append(salaryTempStr)
                salaryEntered = True
        if(newEmployeeData[2].lower() == "manager"):
            if(salaryTempStr >= 10000000):
                newEmployeeData.append(salaryTempStr)
                salaryEntered = True
    
    sortedTable.append(newEmployeeData)

def deleteStaff():
    employeeID = input("Input ID[SXXX]: ")
    for i in range(sortedTable):
        if(employeeID in sortedTable[i]):
            sortedTable.pop(i)
            print("Data has been successfully deleted")
            break
        elif(i<len(sortedTable-1)):
            continue
        else:
            print("Data not found")

def viewSummaryData():
    roleSalaryDict = {}
    for i in sortedTable:
        if(i[2] not in roleSalaryDict):
            roleSalaryDict[i[2]] = [int(i[3])]
        else:
            roleSalaryDict[i[2]].append(int(i[3]))
    count = 1
    for i in roleSalaryDict:
        print(str(count) +". "+ i)
        print("Minimum Salary : "+ min(roleSalaryDict[i]))
        print("Maximum Salary : "+ max(roleSalaryDict[i]))
        print("Average Salaary: "+ mean(roleSalaryDict[i]))

def SaveExit():
    with open('data.txt',mode = 'w') as b:
        for x in sortedTable:
            for y in x:
                b.write(y[0]+"#"+y[1]+"#"+y[2]+"#"+y[3])
        exit()

while(True):
    showTable()
    print("\n\n")
    print("1. New Staff")
    print("2. Delete Staff")
    print("3. View Summary Data")
    print("4. Save & Exit\n")
    
    option = int(input("Input Choice : "))
    if(option == 1):
        print("New Staff ")
        addStaff()
    elif(option == 2):
        print("Delete Staff")
        deleteStaff()
    elif(option == 3):
        print("View Summary Data")
        viewSummaryData()
    elif(option == 4):
        print("Save & Exit")
        SaveExit()
    else:
        continue