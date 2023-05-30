from class_taller import taller


class manejadorTalleres:
        
    def __init__ (self):
        self.__talleres = []
        
    def carga(self):
        with open("Unidad 3/Ejercicio 3/talleres.csv", 'r') as fileTalleres:
            next (fileTalleres)
            for file in fileTalleres:
                file = file.split(';')
                untaller = taller(file[0], file[1],int(file[2]),file[3])
                self.__talleres.append(untaller)
                
    def muestraTalleres(self):
        print("\nTalleres disponibles.")
        for i in range(len(self.__talleres)):
            print(self.__talleres[i].getInfo())
            
    def getTaller(self, tallerID):
        return self.__talleres[tallerID-1]
    
    def setInscripcion(self, tallerID, unainscripcion):
        self.__talleres[tallerID-1].addInscripcion(unainscripcion)
        
    def muestrainscriptos(self):
        self.muestraTalleres()
        xIDTaller = int(input("Ingrese ID de taller > "))
        self.__talleres[xIDTaller-1].obtenerAlumnos()