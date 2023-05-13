class registroCivil:
    __denominacion = ""
    __domicilio = ""
    __actas = list
    __actaActual = 100
    __libroActual = 5
    
    def __init__(self, denominacion, domicilio):
        self.__denominacion = denominacion
        self.__domicilio = domicilio
        self.__actas = []
        
    @classmethod
    def getActaActual(cls):
        cls.__actaActual += 1
        return(cls.__actaActual)
        
    @classmethod
    def getLibroActual(cls):
        return cls.__libroActual
    
    def inscribirPersona(self, persona, date):
        numeroActa = self.getActaActual()
        libro = self.getLibroActual()
        acta = ActaNacimiento(numeroActa, libro, date, persona, self)
        self.__actas.append(acta)
        
    def mostrarActas(self):
        for i in range(len(self.__actas)):
            print("\n")
            self.__actas[i].getInfo()
        
class persona:
    __dni = 0
    __NyA = ""
    
    def __init__(self, dni, nya):
        self.__dni = dni
        self.__NyA = nya
        
    def getDNI(self):
        return(self.__dni)
    
    def getNombre(self):
        return(self.__NyA)
        
class ActaNacimiento:
    __fechaInscripcicion = ""
    __numeroLibro = ""
    __numeroActa = ""
    __persona = object
    __registroCivil = object

    def __init__ (self, nroActa, nroLibro, fechaInscripcion, persona, registroCivil):
        self.__numeroActa = nroActa
        self.__numeroLibro = nroLibro
        self.__fechaInscripcicion = fechaInscripcion
        self.__persona = persona
        self.__registroCivil = registroCivil
        
    def getInfo(self):
        print("Fecha inscripcion ", self.__fechaInscripcicion)
        print("Libro ", self.__registroCivil.getLibroActual(), " Acta ", self.__registroCivil.getActaActual())
        print("DNI ", self.__persona.getDNI())
        print("Nombre ", self.__persona.getNombre())
        

def test():
    print("\n")
    reg = registroCivil ('Capital', 'Libertador y Rawson')
    p1 = persona(44349219, "Juan Perez")
    p2 = persona(40220192, "Mateo Gomez")
    
    reg.inscribirPersona(p1, "13/5/2023")
    reg.inscribirPersona(p2, "13/5/2023")
    
    reg.mostrarActas()

if __name__ == "__main__":
    test()
        
        