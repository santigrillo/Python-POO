class provincia:
    __nombre = ""
    __cant_hab = 0 
    __gobernador = object
    
    def __init__(self, nombre, cant, gobernador = None):
        self.__nombre = nombre
        self.__cant_hab = cant
        self.__gobernador = gobernador
        
    def setGob(self, gobernador):
        self.__gobernador = gobernador
        
    def getGobernador(self):
        return(self.__gobernador.getNyA())
    
    def getProv(self):
        return(self.__nombre)
        
class gobernador:
    __dni = ""
    __NyA = ""
    __provincia = object
    
    def __init__(self, dni, NyA, provincia = None):
        self.__dni = dni
        self.__NyA = NyA
        self.__provincia = provincia
    
    def getNyA(self):
        return(self.__NyA)
    
    def getProvincia(self):
        return(self.__provincia.getProv())


def test():

    print("\n")
    print("Relacion Provincia <gobierna Gobierno")
    nombre = input("Ingrese nombre de la provincia > ")
    cant = int(input("Ingrese cantidad de habitantes de " + nombre + " > "))
    p = provincia(nombre, cant)
    
    NyA = input("Ingrese nombre y apellido del gobernador de " + nombre + " > ")
    dni = input("Ingrese DNI de " + NyA + " > ")
    g = gobernador(dni, NyA, p)
    
    p.setGob(g)
    
    print("En ", g.getProvincia(), " gobierna ", p.getGobernador())

if __name__ == "__main__":
    test()
        