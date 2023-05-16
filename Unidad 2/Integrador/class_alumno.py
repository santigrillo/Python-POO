class Alumno:
    __dni = ""
    __apellido= ""
    __nombre = ""
    __carrera = ""
    __AAAAcursa = 0
    
    def __init__ (self, dni, apellido, nombre, carrera, AAAAcursa):
        self.__dni = dni
        self.__apellido = apellido 
        self.__nombre = nombre
        self.__carrera = carrera
        self.__AAAAcursa  = AAAAcursa                       
    
    def getDNI(self):
        return(self.__dni)

    def getNyA(self):
        return(self.__apellido, self.__nombre)
    
    def getAAAA(self):
        return(self.__AAAAcursa)
    
    def __gt__(self, otro):
        return self.getNyA() > otro.getNyA()