from class_registro import registro
from class_registro import calcular_promedio_temperatura_por_hora
from class_registro import listar_valores_dia
from class_registro import mostrar_valores_extremos
import csv


def menu(registros):
    
        with open("Ejercicio 3/registro.csv", "r") as archivo:
            for linea in archivo:
                dia, hora, temperatura, humedad, presion = linea.strip().split(",")
                registros.append(((int(dia), int(hora)), registro(float(temperatura), float(humedad), float(presion))))
    
    
        lista_bidimensional = [[None for _ in range(24)] for _ in range(31)]
        for (dia, hora), registro in registros:
            lista_bidimensional[dia - 1][hora] = registro
        

        print("Menú:")
        print("1 - Mostrar valores extremos")
        print("2 -Calcular promedio de temperatura por hora")
        print("3 - Listar valores de un día")
        print("-1 - Salir")

        option = int(input("Ingrese opcion > "))

        while(option != -1):
            
            if option == 1:
                mostrar_valores_extremos(lista_bidimensional)
            elif option == 2:
                calcular_promedio_temperatura_por_hora(lista_bidimensional)
            elif option == 3:
                dia = int(input("Ingrese el número de día: "))
                listar_valores_dia(dia, lista_bidimensional)
            else:
                print("Opción invalida")
            
            option = int(input("Ingrese el número de la opción deseada: "))

if __name__ == "__main__":
    registros = []
    menu(registros)