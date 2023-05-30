class evaluacion:
    __dni = str
    __presentacion = str
    __nota1 = 0
    __nota2 = 0
    __nota3 = 0
    
    def __init__ (self, dni, pres, n1, n2, n3):
        self.__dni = dni
        self.__presentacion = pres
        self.__nota1 = n1
        self.__nota2 = n2
        self.__nota3 = n3
        
    def getDNI(self):
        return self.__dni
    
    def getEstilo(self):
        return self.__presentacion
        
    def getProm(self):
        notas = (self.__nota1 + self.__nota2 + self.__nota3) 
        return notas / 3

    def notas(self):
        return self.__nota1, self.__nota2, self.__nota3