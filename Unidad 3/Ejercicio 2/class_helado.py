class helado:
    __gramos = float
    __precio = float
    
    def __init__ (self, gramos):
        self.__gramos = gramos
        self.__sabores = []
    
    def addSabor(self, sabor):
        self.__sabores.append(sabor)
    
    def setPrecio(self):
        return self.__gramos/100 * 400
        
    def getTicket(self):
        for i in range(len(self.__sabores)):
            print("Sabor", i+1, self.__sabores[i].getNombre())
        total = self.setPrecio()
        print("Total = $", total)
    
    def getSabores(self):
        for i in range(len(self.__sabores)):
           print(self.__sabores[i].getNombre())