def reversal(arr):
    x = []
    result = ""
    for counter in range(len(arr), 0 , -1):
        x.append(arr[counter-1])
    for i in x:
        result += i
    return result
      
word = str(input("Insert a string :" ))
arr = list(word)
print(reversal(arr))