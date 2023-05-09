from class_federado import federado
import csv

class manejadorFederados:
    
    def carga(federados):
        with open ("Practica Tema1/archivos/federados.csv", 'r') as ArchivoFederados:
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