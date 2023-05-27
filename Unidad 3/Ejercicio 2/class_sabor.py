class sabor: 
    __id = int
    __ingredientes = str
    __nombreSabor = str
    __vecespedido = 0
    
    def __init__(self, hid, ingredientes, nombre):
        self.__id = hid
        self.__ingredientes = ingredientes
        self.__nombreSabor = nombre
        
    def getNombre(self):
        return self.__nombreSabor
    
    def getSabor(self):
        return self.__nombreSabor, self.__id
    
    def sumapedido(self):
        self.__vecespedido += 1
        
    def getVecesPedido(self):
        return(self.__vecespedido)