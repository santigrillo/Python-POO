class ViajeroFrecuente:
    __numviajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millasacum = 0
    
    def __init__(self, num, dni, nombre, apellido):
        self.__numviajero = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
    
    def getData(self):
        return("Nombre y apellido > ", self.__nombre, self.__apellido, " DNI > ", self.__dni, " Numero > ", self.__numviajero, " Millas >", self.__millasacum)
    
    def getNum(self):
        return(self.__numviajero)

    def cantidadTotalMillas(self):
        print("Millas acumuladas > ", self.__millasacum)
    
    def acumularMillas(self, sumamillas):
        self.__millasacum += sumamillas
        return ("El total de millas ahora es > ", self. __millasacum)
    
    def canjearMillas(self, millascanje):
        if(millascanje <= self.__millasacum):
            self.__millasacum = self.__millasacum - millascanje
        else:
            print("La suma de millas ingresadas es superior a la que posee, su cantidad de millas: ", self.__millasacum)
        print(self.cantidadTotalMillas())
    
                    