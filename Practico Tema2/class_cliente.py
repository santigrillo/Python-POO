class cliente:
    __dni = ""
    __apellido = ""
    __nombre = ""
    __telefono = ""
    __patente = ""
    __vehiculo = ""
    
    def __init__(self, dni, ap, nom, tel, pat, vehiculo):
        self.__dni = dni
        self.__apellido = ap
        self.__nombre = nom
        self.__telefono = tel
        self.__patente = pat
        self.__vehiculo = vehiculo
        
    def getInfo(self):
        print(self.__apellido, self.__nombre,'>', self.__dni)