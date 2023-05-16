class inscripto:
    __apellido = ""
    __nombre = ""
    __dni = ""
    __edad = 0
    __telefono = ""
    __zona = ""
    __factorRiesgo = ""
    
    def __init__(self, apellido, nombre, dni, edad, telefono, zona, factorRiesgo):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        self.__edad = edad
        self.__telefono = telefono
        self.__zona = zona
        self.__factorRiesgo = factorRiesgo
    
    def getInfo(self):
        return(self.__apellido, self.__nombre, self.__edad, self.__factorRiesgo, "Prioridad =", self.getPriority())
    
    def getEdad(self):
        return(self.__edad)
    
    def getFactor(self):
        return(self.__factorRiesgo)
    
    def getPriority(self):
        if self.__factorRiesgo == "Diabetes" or self.__factorRiesgo  == "Obesidad":
            return(self.__edad + 50)
        elif self.__factorRiesgo == "Cardiovascular" or self.__factorRiesgo  == "Renal" or self.__factorRiesgo  == "Respiratoria":
            return(self.__edad + 40)
        elif self.__factorRiesgo == "Cirrosis" or self.__factorRiesgo == "HIV":
            return(self.__edad + 30)
        elif self.__factorRiesgo == "Ninguno":
            return(self.__edad)
        
    def getZona(self):
        return self.__zona
    
    def __gt__(self, otroobj):
        return self.getPriority()>otroobj.getPriority()