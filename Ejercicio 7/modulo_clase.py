class ViajeroFrecuente:
    __numviajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millasacum = int()
    
    def __init__(self, num, dni, nombre, apellido, millas):
        self.__numviajero = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasacum = millas
    
    def getInfo(self):
        print(self.__nombre, self.__apellido, "Nro viaj > ", self.__numviajero, " Millas > ",  self.__millasacum)
    
    def getNum(self):
        return (self.__numviajero)
    
    def getMillas(self):
        return (self.__millasacum)
        
    def __eq__ (self, valcomparar):
        return self.__millasacum == valcomparar
    
    def __req__(self, valcomparar):
        self.__eq__(valcomparar)
        
    def __add__(self, suma):
        self.__millasacum += suma

    def __sub__(self, suma):
        self.__millasacum -= suma
 

        

            
    