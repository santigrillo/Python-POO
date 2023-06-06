class empleado:
    __dni = str
    __nombre = str
    __telefono = str
    
    def __init__(self, dni, nombre, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__telefono = telefono
        
    def calcularSueldo(self):
        pass
    
    def getDNI(self):
        return self.__dni
    
    def sumarHoras(self):
        pass
    
    def getInfoEmpleado(self):
        print("Empleado", self.__nombre)
        
    def getTarea(self):
        pass
    
    def getEstadoTarea(self):
        pass
    
    def getInformacionTarea(self):
        pass
    
    def getCostoTarea(self):
        pass