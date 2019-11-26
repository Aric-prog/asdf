def getAverage(student1,student2,student3):
    average = (student1 + student2 + student3) / (3 * 100)
    return average

student1 = 80.0
student2 = 90.0
student3 = 66.5

average = getAverage(student1,student2,student3)
print(average * 100)
