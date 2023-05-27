from class_carrera import carrera
from class_facultad import facultad

class manejadorFacultad:
    
    def carga(facultades):
        
        with open("Unidad 3/Ejercicio 1/archivos/facultades.csv", 'r') as dataFacultad:
            for file in dataFacultad:
                file = file.split(';')
                if ("facultad" in file[1].lower()):
                    unaFacultad = facultad(file[0], file[1],file[2],file[3],file[4])
                    facultades.append(unaFacultad)
                    ind = int(file[0])
                elif ("facultad" not in file[1].lower()):
                    unaCarrera = carrera(file[0], file[1],file[2],file[3],file[4])
                    facultades[ind-1].addCarrera(unaCarrera)                    
                
            
    def modulo1(facultades):
        for i in range(len(facultades)):
            print(facultades[i].getCeI())
            
        codigoFacultad = int(input("Ingrese codigo de facultad > "))
        facultades[codigoFacultad-1].infoModulo1()
        
    def modulo2(facultades):
        carreraFind = input("Ingrese el nombre de la carrera a buscar > ")
        for i in range(len(facultades)):
            facultades[i].infomd2(carreraFind)