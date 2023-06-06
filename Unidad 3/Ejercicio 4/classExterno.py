from classEmpleado import empleado

class externo(empleado):
    __descripcionTarea = str
    __fechaInicio = str
    __fechaFin = str
    __montoViatico = float
    __costoObra = float
    __montoSeguroDeVida = float
    __estado = str
    
    def __init__(self, dni, nom, tel, descripcion, fechaInicio, fechaFin, montoViatico, costoObra, montoSDV, estado):
        self.__descripcionTarea = descripcion
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__montoViatico = montoViatico
        self.__costoObra = costoObra
        self.__montoSeguroDeVida = montoSDV
        self.__estado = estado
        super().__init__(dni, nom, tel)
  
    def calcularSueldo(self):
        return int(self.__costoObra - self.__montoViatico - self.__montoSeguroDeVida)
        
    def getTarea(self):
        return self.__descripcionTarea
    
    def getEstadoTarea(self):
        return str(self.__estado)
    
    def getInformacionTarea(self):
        super().getInfoEmpleado()
        print(self.__descripcionTarea)
        print(self.__estado)
    
    def getCostoTarea(self):
        return self.__costoObra