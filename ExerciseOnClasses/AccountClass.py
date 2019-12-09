class account:
    __id : str
    __name : str
    __balance : int

    def __init__(self,id,name,balance = 0):
        self.__id = id
        self.__name = name
        self.__balance = balance

    def debit(self,amount):
        self.__balance -= amount if amount <= self.__balance else print('Amount exceeded balance')
        return self.__balance
    
    credit = lambda self,amount : self.__balance + amount

    def transferTo(self, another, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            another.__balance = another.credit(amount)
        else:
            print("Amount exceeded balance")
        
        return self.__balance

    toString = lambda self : "Account [id = " + str(self.__id) + ", name = " + self.__name + ", balance = " + str(self.__balance) + "]"

account1 = account("2301", "aric", 150000)
account2 = account("1234", "jeremy", 0)

print(account1.transferTo(account2, 50000))
print(account1.credit(30000))
print(account2.toString())
        


