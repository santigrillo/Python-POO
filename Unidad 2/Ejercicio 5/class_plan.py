class planAhorro:
    __codigo = 0
    __modelo = ' '
    __version = ' '
    __valor = 0
    __cant_cuotas = 0
    __cant_cuotas_licitar = 0
    
    def __init__(self, cod, mod, ver, value, cuot, lic):
        self.__codigo = cod
        self.__modelo = mod
        self.__version = ver
        self.__valor = value
        self.__cant_cuotas = cuot
        self.__cant_cuotas_licitar = lic
    
    def getInfo(self):
        return(self.__codigo, self.__modelo, self.__version)
        
    def getCode(self):
        return (self.__codigo)
    
    def getvalorCuota(self):
        return(self.__valor / self.__cant_cuotas) + (self.__valor * 0.10)
    
    def cambioCuotas(self):
        ncuotas = int(input("Ingrese nueva cantidad de cuotas > "))
        self.__cant_cuotas_licitar = ncuotas
        
    def changeCarValue(self):
        print ("Codigo > ", self.__codigo, "\n Modelo > ", self.__modelo, "\n Version > ", self.__version)
        nvalor = input ("Ingrese nuevo valor > ")
        self.__valor = nvalor
    
    def total_licitar(self):
        print("Para licitar el plan ", self.__codigo, "debe abonar $",self.__cant_cuotas_licitar*self.getvalorCuota())
    
    