with open('SentenceExample.txt','r', encoding='utf-8') as sen:
    titles = ['mr','mrs','dr','jr']
    sentences : list = []
    fullText = sen.read()
    fullText = fullText.replace('\n'," ")
    newSentence : str = ""
    textLength = len(fullText)
    
    for currentLetter in range(textLength):
        newSentence += fullText[currentLetter]
        
        if(fullText[currentLetter] == '.'):
            try:
                if(fullText[currentLetter+1] != " "):
                    continue
                elif(fullText[currentLetter+2].islower()):
                    continue
                elif((fullText[currentLetter-2] + fullText[currentLetter-1]).lower() in titles):
                    continue
                elif((fullText[currentLetter-3] + fullText[currentLetter-2] + fullText[currentLetter-1]).lower() in titles):
                    continue
                else:
                    sentences.append(newSentence)
                    newSentence = ""
            except IndexError:
                sentences.append(newSentence)
                continue
    
    for i in sentences:
        print(i.strip())