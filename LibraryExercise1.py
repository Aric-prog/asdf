import matplotlib.pyplot as plt
import numpy as np
from math import ceil
import csv

daysSteps : dict = {}
daysDivider : dict ={}
dayArray = []
barNames = []
#togetMedian
daysStepsArray : dict ={}

f = open('activity.csv','r')
lines = f.readlines()
def initializeArrays():
    for i in lines:
        i = i.replace('"',"")
        i = i.replace("\n","")
        i = i.split(',')

        if(i[1] not in daysSteps):
            if(i[0] != 'NA'):
                daysSteps[i[1]] = int(i[0])
                daysDivider[i[1]] = 1
                daysStepsArray[i[1]] = [i[0]]
        else:
            if(i[0] != 'NA'):
                daysSteps[i[1]] += int(i[0])
                daysDivider[i[1]] += 1
                daysStepsArray[i[1]].append(i[0])

initializeArrays()
keys = list(daysSteps.keys())
bars = int(input("Enter number of bars :"))
#change the magic number to display more or less bars
for i in range(bars):
    dayArray.append(daysSteps[keys[i]])
    barNames.append(keys[i])

for i in range(bars):
    print("Median of day " + str(keys[i]) + " : ", end ="")
    

    if(len(daysStepsArray[keys[i]])%2 == 1):
        daysStepsArray[keys[i]].sort()
        medianLocation = ceil(len(daysStepsArray[keys[i]]))/2
        print(daysStepsArray[keys[medianLocation]])

    else:
        daysStepsArray[keys[i]].sort()
        medianLocation =  ceil(len(daysStepsArray[keys[i]]) / 2)
        print(float(int(daysStepsArray[keys[i]][medianLocation]) + int(daysStepsArray[keys[i]][medianLocation+1]) / 2))

    print("Means of day " + str(keys[i]) + " : ", end = "")
    print(daysSteps[keys[i]] / daysDivider[keys[i]] , "\n")
    
plt.bar(barNames,dayArray)
plt.show()

