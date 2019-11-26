def temp():
    celcius = convert_to_celc(fahrenheit)
    print("The temperature in Fahrenheit is : " + str(fahrenheit))
    print("The temperature in Celcius is : " + str(celcius))
    print("The temperature in Kelvin is : " + str(convert_to_kelv(celcius)))
def convert_to_celc(fahrenheit):
    return 5/9*(fahrenheit-32)
def convert_to_kelv(celcius):
    return celcius + 273.15

fahrenheit = int(input("Input fahrenheit : "))
temp()
    
