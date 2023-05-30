from class_taller import taller


class manejadorTalleres:
        
    def __init__ (self):
        self.__talleres = []
        
    def carga(self):
        with open("Unidad 3/Ejercicio 3/talleres.csv", 'r') as fileTalleres:
            next (fileTalleres)
            for file in fileTalleres:
                file = file.split(';')
                untaller = taller(file[0], file[1],file[2],file[3])
                self.__talleres.append(untaller)
                
    def muestraTalleres(self):
        print("\nTalleres disponibles.")
        for i in range(len(self.__talleres)):
            print(self.__talleres[i].getInfo())