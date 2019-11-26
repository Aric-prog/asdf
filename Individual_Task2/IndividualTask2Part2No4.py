def calc_new_weight():
    #image has m and n units of hw
    #image is bigger than the width that your blog has 
    oldWidth = int(input("Enter current width : "))
    oldHeight =  int(input("Enter current height : "))
    newWidth = int(input("Enter current new width : "))
    
    newHeight = (oldHeight / oldWidth) * newWidth
    print("The corresponding height is : " + str(newHeight))

calc_new_weight()