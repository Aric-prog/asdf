newTextFile = open('lineByLineOutput.txt','w+')
with open('LinebyLine.txt') as fp:
    count = 1
    lines = fp.readlines()
    for i in lines:
        newTextFile.write("Line " + str(count) + " : " + i)
        count += 1