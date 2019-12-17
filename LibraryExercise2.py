import matplotlib.pyplot as plt
import numpy as np
from math import ceil
import csv

intervalsAndSums : dict = {}
totalDays = 61
f = open('activity.csv','r')
lines = f.readlines()
lines.pop(0)
def initializeArrays():
    for i in lines:
        i = i.replace('"',"")
        i = i.replace("\n","")
        i = i.split(',')

        if(i[0] != "NA"):
            if(str(i[2]) not in intervalsAndSums):
                intervalsAndSums[str(i[2])] = int(i[0])
            else:
                intervalsAndSums[str(i[2])] += int(i[0])
f.close()
initializeArrays()

intervalKeys = list(intervalsAndSums.keys())
intervalValues = []
for a in intervalsAndSums:
    intervalValues.append(intervalsAndSums[a]/61)
print("The interval with maximum steps is : ")
maxValue = max(intervalValues)
print("Interval : " + intervalKeys[intervalValues.index(maxValue)])
print("Averaged Step : " + str(maxValue))
plt.bar(intervalKeys,intervalValues)
plt.xlabel("Intervals")
plt.ylabel("Averaged Steps")
plt.show()