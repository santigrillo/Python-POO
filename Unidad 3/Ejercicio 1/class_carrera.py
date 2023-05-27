class carrera: 
    __codigo = str
    __nombre = str
    __titulo = str
    __duracion = str
    __tipo = str
    
    def __init__ (self, cod, nom, tit, dur, tip):
        self.__codigo = cod
        self.__nombre = nom
        self.__titulo = tit
        self.__duracion = dur
        self.__tipo = tip
        
    def infomd1(self):
        print("Nombre ", self.__nombre, " Duracion ", self.__duracion)
    
    def getCodigoFacultad(self):
        cod = self.__codigo.split(',')
        return cod[0]
    
    def getCod(self):
        return self.__codigo
    
    def getnomb(self):
        return self.__nombre