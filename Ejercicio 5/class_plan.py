class planAhorro:
    __codigo = 0
    __modelo = ' '
    __version = ' '
    __valor = 0
    __cant_cuotas = 0
    __cant_cuotas_licitar = 0
    
    def __init__(self, cod, mod, ver, value, cuotas, cantlicitar):
        self.__codigo = cod
        self.__modelo = mod
        self.__version = ver
        self.__valor = value
        self.__cant_cuotas = cuotas
        self.__cant_cuotas_licitar = cantlicitar
    
    def getInfo(self):
        print(self.__codigo, self.__modelo, self.__version)
        
    def getCode(self):
        return self.__codigo
        
    def getvalorCuota(self):
        return self.__valor / self.__cant_cuotas + self.__valor * 0.10
    
    def cambioCuotas(self):
        ncuotas = input("Ingrese nueva cantidad de cuotas > ")
        self.__cant_cuotas_licitar = ncuotas
        
    def changeCarValue(self):
        print ("Codigo > ", self.__codigo, "\n Modelo > ", self.__modelo, "\n Version > ", self.__version)
        nvalor = input ("Ingrese nuevo valor > ")
        self.__valor = nvalor
    
    def total_licitar(self):
        return (self.__cant_cuotas_licitar*self.getinfo())
    
    def cambiarCuotas(self, listaplanes):
        ind = 0
        band = False
        codigo = int(input("Ingrese codigo de plan > "))
        while ind < len(listaplanes) and band == False:
            if (listaplanes[ind].getCode() == codigo):
                listaplanes[ind].cambioCuotas
                band = True
            ind += 1
    