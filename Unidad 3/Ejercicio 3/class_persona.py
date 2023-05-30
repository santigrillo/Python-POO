class persona: 
    __nombre = str
    __direccion = str
    __dni = str
    
    def __init__ (self, nombre, direccion, dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni
        self.__inscripcion = object
        
    def setinscripcion(self, inscripcion):
        self.__inscripcion = inscripcion
    
    def getInfoins(self):
        print("Nombre y apellido", self.__nombre, "\nDireccion",self.__direccion, "\nDocumento", self.__dni)
        
    def getNombre(self):
        return(self.__nombre)
    
    def getDNI(self):
        return self.__dni