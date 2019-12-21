import matplotlib.pyplot as plt
import numpy as np
from random import randint
from math import ceil
import csv

weekday : dict = {}
weekend : dict = {}
averagedWeekday : dict
averagedWeekend : dict

# used to determine whether a day is a weekend or weekday
# weekend is determined by modulo 7 or 8 (saturday and sunday)
count = 1

f = open('activity.csv','r')
dateList =[]
lines = f.readlines()
lines.pop(0)
def averageOfDicts(targetDict):
    totalDay = count
    for i in targetDict:
        targetDict[i] = targetDict[i] / totalDay

def initializeArrays(count):
    for i in lines:
        i = i.replace('"',"")
        i = i.replace("\n","")
        i = i.split(',') 
        
        if((count % 6) == 0 or (count % 7) == 0):
            if(i[0] != "NA"):
                if(str(i[2]) not in weekend):
                    weekend[str(i[2])] = int(i[0])
                else:
                    weekend[str(i[2])] += int(i[0])
            else:
                if(str(i[2]) not in weekend):
                    weekend[str(i[2])] = 0
        
        else:
            if(i[0] != "NA"):
                if(str(i[2]) not in weekday):
                    weekday[str(i[2])] = int(i[0])
                else:
                    weekday[str(i[2])] += int(i[0])
            else:
                if(str(i[2]) not in weekday):
                    weekday[str(i[2])] = 0
        
        if(i[1] not in dateList):
            dateList.append(i[1])
            count+=1
            
    averageOfDicts(weekday)
    averageOfDicts(weekend)
            
f.close()
initializeArrays(1)
interval = list(weekday.keys())
weekdayValues = []
weekendValues = []
for key in weekday:
    weekdayValues.append(weekday[key])
for key in weekend:
    weekendValues.append(weekday[key])
plt.plot(interval,weekdayValues)
plt.plot(interval,weekendValues)
plt.show()

