def calculate(hours,rate):
    pay = 0
    if(hours > 40):
        pay = (40 * rate) + ((hours - 40) * (1.5 * rate))
    else:
        pay = hours * rate
    return pay

x = int(input("Hours worked : "))
rate = int(input("Wage : "))
print("Pay :",calculate(x,rate))