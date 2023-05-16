from modulo_clase import ViajeroFrecuente
import csv
import sys

def menu(listaViajeros, idviaj, option, sumamillas, millascanjear):
    print("\n")
    print("Menú")
    print("1 - Consultar millas")
    print("2 - Acumular millas")
    print("3 - Canjear millas")
    print("-1 - Salir")
      
    while(option != -1):
        if(option == 1):
            listaViajeros[idviaj].cantidadTotalMillas()
        
        if(option == 2):
            # sumamillas = float(input("Ingrese millas a sumar > "))
            listaViajeros[idviaj].acumularMillas(sumamillas)
            print("Millas cargadas.")
        
        if(option == 3):
            # millascanjear = float(input("Ingrese la cantidad de millas a canjear > "))
            listaViajeros[idviaj].canjearMillas(millascanjear)
        
        option = -1 #Salida
            
def test():
    menu(listaViajeros, 1, 1, 0, 0) #Consulta millas viajero 1.
    menu(listaViajeros, 1, 2, 500, 0) #Suma 500 millas al viajero 1.
    menu(listaViajeros, 1, 1, 0, 0) #Consulta millas viajero 1.
    menu(listaViajeros, 1, 3, 0, 200) #Canjea millas viajero 1 y devuelve resto.
    

if __name__ == "__main__":  
    
    listaViajeros = []
    with open ("Ejercicio 2/dataviajeros.csv", 'r') as file_viajeros:
        next(file_viajeros)
        for file in file_viajeros:
            file = file.split(';')
            viaj = ViajeroFrecuente (file[0], file[1], file[2], file[3])
            listaViajeros.append(viaj)
        print("Info de viajeros cargada con éxito.")
    
    test()
    print("\n")
    
    print("La lista pesa ",sys.getsizeof(listaViajeros), "bytes")
    
    
    