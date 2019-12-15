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
