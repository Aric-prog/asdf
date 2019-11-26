def convert_to_days():
    hours = float(input("Input Hours : "))
    minutes = float(input("Input Minutes : "))
    seconds = float(input("Input Seconds : "))
    days = (get_days(hours,minutes,seconds))
    print("The number of days is : " + str(days))

def get_days(hours,minutes,seconds):
    minutes = minutes + seconds / 60
    hours = hours + minutes / 60
    day = hours / 24
    return round(day,4)

convert_to_days()