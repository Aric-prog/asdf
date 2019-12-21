import matplotlib.pyplot as plt
import numpy as np
from random import randint
from math import ceil
import csv

daysSteps : dict = {}
daysDivider : dict ={}
dayArray = []
barNames = []
intervals = []

#togetMedian
daysStepsArray : dict ={}

f = open('activity.csv','r')
lines = f.readlines()
lines.pop(0)
def initializeArrays():
    for i in lines:
        i = i.replace('"',"")
        i = i.replace("\n","")
        i = i.split(',')
        temp = randint(0,300)
        if(i[1] not in daysSteps):
            if(i[0] != 'NA'):
                daysSteps[i[1]] = int(i[0])
                daysDivider[i[1]] = 1
                daysStepsArray[i[1]] = [i[0]]
            else:
                daysSteps[i[1]] = temp
                daysDivider[i[1]] = 1
                daysStepsArray[i[1]] = [temp]
        else:
            if(i[0] != 'NA'):
                daysSteps[i[1]] += int(i[0])
                daysDivider[i[1]] += 1
                daysStepsArray[i[1]].append(i[0])
            else:
                daysSteps[i[1]] += temp
                daysDivider[i[1]] += 1
                daysStepsArray[i[1]].append(temp)

        if(i[2] not in intervals):
            intervals.append(i[2])
f.close()
initializeArrays()
keys = list(daysSteps.keys())
#change the magic number to display more or less bars
for i in range(len(keys)):
    print("Median of day " + str(keys[i]) + " : ", end ="")
    dayArray.append(daysSteps[keys[i]])
    barNames.append(keys[i])
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

with open("newStepsData.csv",'w+') as wr:
    wr.write('"Steps,"Dates","Interval"')
    for key in daysStepsArray:
        count = 0
        for elements in daysStepsArray[key]:
            wr.write(str(elements)+","+key+","+intervals[count]+"\n")
            count+=1
            if(count == len(intervals)):
                count=0 


plt.bar(barNames,dayArray)
plt.show()


