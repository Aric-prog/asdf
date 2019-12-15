hapaxCandidate : dict = {}
with open('BookExample.txt','r',encoding= 'utf-8') as a:
    count = 0
    rawLines = a.read()
    rawLines = rawLines.replace('“',"").replace('”',"").replace('’',"").replace('!',"").replace('.',"").replace(':',"")
    
    wordArray = rawLines.split()
    hapax = []
    for a in wordArray:
        wordArray[wordArray.index(a)] = a.upper()
    for i in wordArray:
        if i not in hapaxCandidate:
            hapaxCandidate[i] = 1
        else:
            hapaxCandidate[i] +=1
    
    for i in hapaxCandidate:
        if(hapaxCandidate[i] == 1):
            hapax.append(i)
        else:
            continue

    print(hapax)