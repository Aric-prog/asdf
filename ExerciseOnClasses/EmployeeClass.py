class employee:
    __id : int
    __firstName : str
    __lastName : str
    __salary : int

    def __init__(self,id,firstName,lastName,salary):
        self.__id = id
        self.__firstName = firstName
        self.__lastName = lastName
        self.__salary = salary

    def setSalary(self,salary):
        self.__salary = salary

    def raiseSalary(self, percent):
        self.__salary = self.__salary * ((100 + percent) / 100)
        return self.__salary

    getID = lambda self : self.__id
    getFirstName = lambda self : self.__firstName
    getName = lambda self : self.__firstName + " " + self.__lastName
    getSalary = lambda self : self.__salary
    getAnnualSalary = lambda self : self.__salary * 12
    toString = lambda self : "Employee [id = " + str(self.__id) + ", name = " + self.getName() + ", salary = " + str(self.__salary) + "]"

employee1 = employee(2301,"Bentele","Edoson",500)
print(employee1.toString())