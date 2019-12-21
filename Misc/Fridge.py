class Fridge():
    user = ""
    password = ""
    row1,row2,row3 = {"CARROT":1,"AVOCADO":2},{"TOMATO":3,"PAPAYA":4},{}
    rows = [row1,row2,row3]
    
    def __init__(self,user,password):
        self.user = user
        self.password = password
    
    def login(self):
        print("______      _      _              ")
        print("|  ___|    (_)    | |             ")
        print("| |_  _ __  _   __| |  __ _   ___ ")
        print("|  _|| '__|| | / _` | / _` | / _ \\")
        print("| |  | |   | || (_| || (_| ||  __/")
        print("\_|  |_|   |_| \__,_| \__, | \___|")
        print("                       __/ |      ")
        print("                      |___/       ")

        
        for i in range(3):
            x = str(input("Username : "))
            y = str(input("Password : "))
            if(x == self.user and y == self.password):
                print("\nWelcome, " , self.user)
                return True
            else:
                print("\nInvalid username or password")
                print("Please try again")
                print("----------------------------\n")
        print("Access denied.")
        return False
    
    def view_fridge(self):
        print(" _==============_")
        print("/                \\")
        
        for r in self.rows:
            print("")
            for elements in r:
                print("  ", elements, " :", r[elements])
            
            print("__________________")
    
    def store(self,no,key,value):
        index = no-1
        key = key.upper()

        if(key in self.rows[index].keys()):
            (self.rows[index])[key] += value
        else:    
            (self.rows[index])[key] = value
         
    def retrieve(self,no,key,value):
        index = no-1
        key = key.upper()

        if(key in self.rows[index].keys()):
            if((self.rows[index])[key] >= value):
                (self.rows[index])[key] -= value
            else:
                
                del (self.rows[index])[key]
        else:
            print(key ," is not in the fridge row")


user1 = Fridge("aric", "aric")
FridgeAccess = True
print("Please enter your login information : ")
FridgeAccess = user1.login()

while(FridgeAccess):
    print("What would you like to do? (View / Store / Retrieve / Logout)")
    option = str(input("")).lower()
    if(option == "view"):
        user1.view_fridge()
    elif(option == "store"):
        x = int(input("Row no. ( 1-3 ) : "))
        y = str(input("What do you want to store : "))
        z = int(input("How much do you want to store : "))
        user1.store(x,y,z)
    elif(option == "retrieve"):
        x = int(input("Row no. : "))
        y = str(input("What do you want to retrieve : "))
        z = int(input("How much do you want to retrieve : "))
        user1.retrieve(x,y,z)
    elif(option == "logout"):
        print("Please enter your login information : ")
        FridgeAccess = user1.login()
    else:
        print("Invalid syntax")
        
        
