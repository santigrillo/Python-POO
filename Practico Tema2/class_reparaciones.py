class reparacion:
    __patente = ""
    __reparacion = ""
    __repuesto = ""
    __precioRepuesto = ""
    __precioManoDeObra = ""
    __estado = ""
    
    def __init__(self, pat, rep, repuesto, pR, pMO, est):
        self.__patente = pat
        self.__reparacion = rep
        self.__repuesto = repuesto
        self.__precioRepuesto = pR
        self.__precioManoDeObra = pMO
        self.__estado = est
        
    def getInfo(self):
        print(self.__patente, self.__reparacion)