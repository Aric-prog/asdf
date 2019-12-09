class InvoiceItem:
    __id : str
    __desc : str
    __qty : int
    __unitPrice : float

    def __init__(self,id,desc,qty,unitPrice):
        self.__id = id
        self.__desc = desc
        self.__qty = qty
        self.__unitPrice = unitPrice
    
    def setQty(self,qty):
        self.__qty = qty
    
    def setUnitPrice(self, unitPrice):
        self.__unitPrice = unitPrice

    getID = lambda self : self.__id
    getDesc = lambda self : self.__desc
    getQty = lambda self : self.__qty
    getUnitPrice = lambda self : self.__unitPrice
    getTotal = lambda self : self.__unitPrice * float(self.__qty)
    toString = lambda self : "InvoiceItem[id = " + self.__id + ", desc = " + self.__desc + ", qty = " + str(self.__qty) + ", unitPrice = " + str(self.__unitPrice)

invoice1 = InvoiceItem("111" , "asdflkj", 23, 2.500)
print(invoice1.getTotal())