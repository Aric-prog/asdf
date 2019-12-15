with open('BookExample.txt','r',encoding= 'utf-8') as a:
    count = 0
    rawLines = a.read()
    rawLines = rawLines.replace('“',"").replace('”',"").replace('”',"").replace('!',"")

    wordArray = rawLines.split()
    for i in wordArray:
        for characters in i:
            count += 1
    print(count / len(wordArray))    