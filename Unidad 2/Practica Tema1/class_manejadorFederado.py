from class_federado import federado
import csv

class manejadorFederados:
    
    def carga(federados):
        with open ("Unidad 2/Practica Tema1/archivos/federados.csv", 'r') as ArchivoFederados:
            for file in ArchivoFederados:
                file = file.split(';')
                fed = federado(file[0], file[1], file[2], int(file[3]), file[4])
                federados.append(fed)
              
    def getAlumno(federados, dni):
        i=0
        valorRetorno = -1
        Bandera = False
        while i < len(federados) and not Bandera:
            if federados[i].getDNI() == dni:
                Bandera = True
                valorRetorno = i
            else:
                i+=1
        return valorRetorno
    
    def option2(evaluaciones, federados):
        evaluaciones.sort(key=lambda i: i.getPromedio(), reverse=True)
        dni = evaluaciones[0].getDNI()
        idAl = manejadorFederados.getAlumno(federados, dni)
        print("El alumno con mayor promedio es ", federados[idAl].getInfo2(), " con ", evaluaciones[0].getPromedio())