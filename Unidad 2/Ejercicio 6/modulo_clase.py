class ViajeroFrecuente:
    __numviajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millasacum = 0
    
    def __init__(self, num, dni, nombre, apellido, millas):
        self.__numviajero = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasacum = millas
    
    def getinfo(self):
        return(self.__nombre, self.__apellido, "Nro viaj > ", self.__numviajero, " Millas > ",  self.__millasacum)
    
    def getNum(self):
        return (self.__numviajero)
    
    def getMillas(self):
        return (self.__millasacum)
        
    def __gt__ (self, mayor):
        return (self.__millasacum > mayor)
        
    def __add__ (self, suma):
        self.__millasacum += suma
        return self.__millasacum
    
    def __sub__ (self, resta):
        self.__millasacum -= resta
        return self.__millasacum
        
                    