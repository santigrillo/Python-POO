
class inscripcion:
    __fechaInscripcion = str
    __pago = False
    
    def __init__ (self, fecha, persona, taller):
        self.__fechaInscripcion = fecha
        self.__persona = persona
        self.__taller = taller

    def getInfo(self):
        print("Informacion de inscripcion")
        print("Inscripcion realizada a ", self.__persona.getNombre())
        print("Se inscribió al taller de > ", self.__taller.getInfo())
    
    def getDniInscripto(self):
        return self.__persona.getDNI()
    
    def getInfoTaller(self):
        print(self.__taller.getInfo())
    
    def getEstado(self):
        return self.__pago 
    
    def getMonto(self):
        return self.__taller.getMonto()

    def getPersona(self):
        print(self.__persona.getNombre())
    
    def pagar(self):
        self.__pago = True
        print("Pago realizado con éxito.")