class taller:
    __idTaller = int
    __nombre = str
    __vacantes = int
    __montoInscripcion = int
    
    def __init__ (self, idtaller, nombre, vacantes, montoInsc):
        self.__idTaller = idtaller
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoInscripcion = montoInsc
        self.__inscripciones = []
        
    def getInfo(self):
        return(self.__nombre, "ID ", self.__idTaller)

    def ocupavacantes(self):
        if int(self.__vacantes) > 0:
            self.__vacantes = (self.__vacantes - 1)
        elif int(self.__vacantes) == 0:
            print("Ya no quedan vacantes disponibles.")
            
    def addInscripcion(self, inscripcion):
        self.ocupavacantes()
        self.__inscripciones.append(inscripcion)
        
    def getinfoins(self):
        return(self.__nombre)
    
    def getMonto(self):
        return self.__montoInscripcion
    
    def obtenerAlumnos(self):
        tieneAlumnos = False
        for i in range(len(self.__inscripciones)):
            self.__inscripciones[i].getPersona()
            tieneAlumnos = True
        if not tieneAlumnos:
            print("El taller que eligió no tiene alumnos inscriptos.")