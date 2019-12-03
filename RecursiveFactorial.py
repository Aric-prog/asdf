def factorial(num):
    if(num > 1):
        return factorial(num-1) * num
    elif(num >= 0 and num <= 1):
        return 1
    else:
        return "Error"

print(factorial(5))
