from class_lugares import lugar

class ManejadorL:    
    def carga(lugares):
        with open ("Integrador 1/lugaresVac.csv", 'r') as fileLugares:
            next (fileLugares)
            for file in fileLugares:
                file = file.split(";")
                l = lugar(file[0], file[1])
                lugares.append(l)
        return lugares
                  
    def muestra(lugares):
        for i in range(len(lugares)):
            print(lugares[i].getInfo())