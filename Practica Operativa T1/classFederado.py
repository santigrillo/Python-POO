class federado:
    __apellido = str
    __nombre = str
    __dni = str
    __edad = str
    __club = str
    
    def __init__ (self, ap, nom, dni, edad, club):
        self.__apellido = ap
        self.__nombre = nom
        self.__dni = dni
        self.__edad = edad
        self.__club = club
        
        
    def getDNI(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    def getInfo(self):
        return(self.__nombre, self.__apellido, self.__dni)
        