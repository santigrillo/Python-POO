from class_evaluacion import evaluacion
from class_manejadorFederado import manejadorFederados
import csv

class ManejadorEvaluaciones:
    
    def carga(evaluaciones):
        with open ("Practica Tema1/archivos/evaluacion.csv", 'r') as ArchivoEvaluaciones:
            for file in ArchivoEvaluaciones:
                file = file.split(';')
                ev = evaluacion(file[0], file[1], float(file[2]), float(file[3]), float(file[4]))
                evaluaciones.append(ev)
                
    
    def option1(evaluaciones, federados):
        estilo = input("Ingrese estilo > ")
        edad = int(input("Ingrese edad > "))
        dni = 0
        for i in range(len(evaluaciones)):
            if(evaluaciones[i].getEstilo() == estilo):
                dni = evaluaciones[i].getDNI()
                xid = manejadorFederados.getAlumno(federados, dni)
                if federados[xid].getEdad() == edad:
                    federados[xid].getInfo()
        
