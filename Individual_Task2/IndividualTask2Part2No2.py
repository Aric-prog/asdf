def calc_weight_on_planet(weight, gravity = 23.1):
    #calculate mass first 
    weight = (weight / 9.8) * gravity
    print(weight)

calc_weight_on_planet(120,9.8)
calc_weight_on_planet(120)
calc_weight_on_planet(120,23.1)