import numpy as np
import csv 
from class_alumno import Alumno
from class_mataprobada import materiaAprobada
from manejador_alumnos import manejadorAl

def menu():
    
    #Carga numpy array
    with open ("Integrador/alumnos.csv", 'r') as file:
        alumnos = []
        next(file)
        for line in file:
            line = line.split(';')
            a = Alumno(line[0], line[1], line[2], line[3], int(line[4]))
            alumnos.append(a)
        np.array(alumnos)
    
    #Carga lista materias.
    with open ("Integrador/materiasAprobadas.csv", 'r') as filemat:
        materiasaprobadas = []
        next(filemat)
        for line in filemat:
            line = line.split(";")
            m = materiaAprobada(line[0], line[1], line[2], float(line[3]), line[4])
            materiasaprobadas.append(m)

    
    print("Menú")
    print("1 - Informar promedio de alumno.")
    print("2 - Ver aprobados como promocionales por materia")
    print("3 - Mostrar lista ordenada")
    option = int(input("Ingrese opcion > "))
    
    
    while (option != -1):
        
        if(option == 1):
            manejadorAl.promedio(alumnos, materiasaprobadas)

        if(option == 2):
            manejadorAl.promocionales(alumnos, materiasaprobadas)
            
        if (option == 3):
            manejadorAl.ordenar(alumnos)
                    
        option = int(input("Ingrese opcion > "))

if __name__ == "__main__":
    menu()
