class date:

    def __init__(self,day,month,year):
        self.__day = day
        self.__month = month
        self.__year = year

    getDay = lambda self : self.__day
    getMonth = lambda self : self.__month
    getYear = lambda self : self.__year

    def setDay(self, day):
        self.__day = day
    def setMonth(self, month):
        self.__month = month
    def setYear(self, year):
        self.__year = year
    def setDate(self, day,month,year):
        self.__day = day
        self.__month = month
        self.__year = year

    toString = lambda self : str(self.__day).zfill(2) + "/" + str(self.__month).zfill(2) + "/" + str(self.__year).zfill(4)

anying = date(1,2,3)
print(anying.toString())

