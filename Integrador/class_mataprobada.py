class materiaAprobada:
    __dni = " "
    __nombreMat = " "
    __fecha = " "
    __nota = float()
    __aprobacion = " "
    
    def __init__(self, dni, nombreMat, fecha, nota, aprobacion):
        self.__dni = dni
        self.__nombreMat = nombreMat 
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion
        
    def getDNI(self):
        return(self.__dni)

    def getNota(self):
        return(self.__nota)
    
    def getNomb(self):
        return(self.__nombreMat)

    def getCondicion(self):
        return(self.__aprobacion)
    
    def getFecha(self):
        return (self.__fecha)
    