class beca:
    __idbeca = int
    __tipo = str
    __importe = float
    
    def __init__(self, idbeca, tipo, importe):
        self.__idbeca = idbeca
        self.__tipo = tipo
        self.__importe = importe
        
    def getnombre(self):
        return(self.__tipo)
        
    
    def getid(self):
        return self.__idbeca
    
    def gettotal(self):
        return self.__importe
    