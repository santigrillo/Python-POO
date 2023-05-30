class beneficiario:
    __dni = str
    __nombre = str
    __apellido = str
    __carrera = str
    __siglaFacultad = str
    __AAAAcursa = str
    __promedio = float
    __idBeca = int
    
    def __init__ (self, dni, nombre, apellido, carrera, sigla, AAAA, promedio, idBeca):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__siglaFacultad = sigla
        self.__AAAAcursa = AAAA
        self.__promedio = promedio
        self.__idBeca = idBeca
        
    def getBeca(self):
        return self.__idBeca

    def getInfo(self):
        return self.__nombre, self.__apellido, self.__idBeca
    
    def getDNI(self):
        return self.__dni
    
    def infomd2(self):
        return (self.__nombre, self.__apellido, self.__carrera, self.__siglaFacultad)
    
    def getPromedio(self):
        return float(self.__promedio)
    
    def getcursa(self):
        return self.__AAAAcursa
    
    def __gt__(self, otro):
        var1 =  str(self.getcursa()) + str(self.getPromedio()) 
        var2 =  str(otro.getcursa()) + str(otro.getPromedio())
        return var1 > var2
    
    def getinfomd3(self):
        return(self.__apellido, self.__nombre, self.__AAAAcursa, self.__promedio)
    
    def getinfomd4(self):
        return(self.__apellido, self.__nombre, "ID beca ", self.__idBeca)