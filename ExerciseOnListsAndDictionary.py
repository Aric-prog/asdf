#1

inventory = {
    'pocket' : ['seashell', 'strangeberry', 'lint'], 
    'gold': 500,
    'pouch':['flint','twine','gemstone'],
    'backpack':['xylophone','dagger','bedroll','breadloaf']
}

inventory['pocket'].sort()
inventory['backpack'].extend(inventory['pocket'])
inventory['gold'] += 50

inventory['backpack'].remove('dagger')
print(inventory['backpack'])

#2

total = 0 
prices = {
    "banana": 4,
    "apple":  2,
    "orange": 1.5,
    "pear":   3
}

stock = {
    "banana": 1,
    "apple":  2,
    "orange": 2,
    "pear"  : 2
}
for i in prices:
    print(str(prices) + "\nprice : " + str(prices[i]) + "\nstock : " + str(stock[i])) 

for i in prices:
    total += prices[i] * stock[i]
print(total)

#3

groceries = ['banana','orange','apple']
stock={"banana" : 6,"apple" : 0,"orange" : 32,"pear" : 15}
prices={"banana" : 4,"apple" : 2,"orange" : 1.5,"pear" : 3}

def compute_bill(groceries):
    bill = 0
    for i in groceries:
        if(stock[i] > 0):
            stock[i] -= 1
            bill += prices[i]
    return bill
print(compute_bill(groceries))

#4

eren = {
    "name" : "Eren",
    "homework" : [90.0,97.0,75.0,92.0],
    "quizzes" : [88.0,40.0,94.0],
    "tests" : [75.0, 90.0]
}

mikasa = {
    "name" : "Mikasa",
    "homework" : [100.0,92.0,98.0,100.0],
    "quizzes" : [82.0,83.0,91.0],
    "tests" : [89.0,97.0]        
}
armin = {
    "name" : "Armin",
    "homework" : [0.0,87.0,75.0,22.0],
    "quizzes" : [0.0,75.0,78.0],
    "tests" : [100.0,100.0]  
}

students = [eren,mikasa,armin]
for i in students:
    for j in i:
        print(j , ": " , i[j])
    print("")

def average(numbers:list):
    total = float(sum(numbers)/len(numbers))
    return total

def get_average(student):
    homework = average(student["homework"]) * 0.1
    quizzes = average(student["quizzes"]) * 0.3
    tests = average(student["tests"]) * 0.6

    return homework + quizzes + tests

def get_letter_grade(score):
    if score >=90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"
score = get_letter_grade(get_average(eren))

def get_class_average(stud : list):
    results = []
    for i in stud:
        score = get_average(i)
        results.append(score)
    return average(results)

print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))