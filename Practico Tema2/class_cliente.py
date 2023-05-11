class cliente:
    __dni = ""
    __apellido = ""
    __nombre = ""
    __telefono = ""
    __patente = ""
    __vehiculo = ""
    __estado = ""
    
    def __init__(self, dni, ap, nom, tel, pat, vehiculo, est):
        self.__dni = dni
        self.__apellido = ap
        self.__nombre = nom
        self.__telefono = tel
        self.__patente = pat
        self.__vehiculo = vehiculo
        self.__estado = est
        
    def getInfo(self):
        print(self.__apellido, self.__nombre,'>', self.__dni)
        
    def getDNI(self):
        return(self.__dni)
   
    def getPatente(self):
        return(self.__patente) 
    
    def getVehiculo(self):
        print(self.__vehiculo, self.__patente)
     
    def modificarEstado(self):
        self.__estado = 'T'

    def getEstado(self):
        return (self.__estado)   
    
