from modulo_clase import ViajeroFrecuente
import csv
import sys

def menu(listaViajeros, idviaj):
    print("Menú")
    print("1 - Consultar millas")
    print("2 - Acumular millas")
    print("3 - Canjear millas")
    print("-1 - Salir")
    
    option = int(input("Opción > "))
    
    while(option != -1):
        if(option == 1):
            listaViajeros[idviaj].cantidadTotalMillas()
        
        if(option == 2):
            sumamillas = float(input("Ingrese millas a sumar > "))
            listaViajeros[idviaj].acumularMillas(sumamillas)
        
        if(option == 3):
            millascanjear = float(input("Ingrese la cantidad de millas a canjear > "))
            listaViajeros[idviaj].canjearMillas(millascanjear)
            
        option = int(input("Opción > "))
        
if __name__ == "__main__":  
    
    listaViajeros = []
    with open ("Ejercicio 2/dataviajeros.csv", 'r') as file_viajeros:
        next(file_viajeros)
        for file in file_viajeros:
            file = file.split(';')
            viaj = ViajeroFrecuente (file[0], file[1], file[2], file[3])
            listaViajeros.append(viaj)
        print("Info de viajeros cargada con éxito.")
    
    idviaj = int(input("Ingrese numero de viajero > "))
    menu(listaViajeros, idviaj)
    
    print("La lista pesa ",sys.getsizeof(listaViajeros), "bytes")
    
    
    