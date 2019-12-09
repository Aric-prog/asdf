class time:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    getHour = lambda self : self.__hour
    getMinute = lambda self : self.__minute
    getSecond = lambda self : self.__second
    toString = lambda self : str(self.__hour).zfill(2) +":" +str(self.__minute).zfill(2) + ":" + str(self.__second).zfill(2)

    def setHour(self,hour):
        self.__hour = hour
    def setMinute(self,minute):
        self.__minute = minute
    def setHour(self,second):
        self.__second = second
    def setHour(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def nextSecond(self):
        x = self.__hour
        y = self.__minute
        z = self.__second

        z += 1
        if(z >= 60):
            z = 0
            y +=1
        if(y >= 60):
            y = 0
            x += 1
        if(x >=24):
            x = 0
        
        return time(x,y,z)

    def previousSecond(self):
        x = self.__hour
        y = self.__minute
        z = self.__second

        z -=1
        if(z < 0):
            z =59
            y-=1
        if(y < 0):
            y =59
            x-=1
        if(x < 0):
            x =23
        
        return time(x,y,z)

a = time(0,0,0)
print(a.toString())
b = a.nextSecond()
print(b.toString())
c = a.previousSecond()
print(c.toString())