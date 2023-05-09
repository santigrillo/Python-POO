class federado: 
    __apellido = ""
    __nombre = ""
    __dni = ""
    __edad = 0
    __club = ""
    
    def __init__(self, apellido, nombre, dni, edad, club):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        self.__edad = edad
        self.__club = club
    
    def getDNI(self):
        return(self.__dni)
    
    def getInfo(self):
        print(self.__nombre, self.__apellido)
    
    def getEdad(self):
        return(self.__edad)