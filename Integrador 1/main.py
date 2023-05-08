from manejadorLugar import ManejadorL
from class_lugares import lugar
from manejadorInscriptos import ManejadorIns
import csv

def menu():
    lugares = []
    ManejadorL.carga(lugares)
    
    
    print("\n")
    
    inscriptos = []
    ManejadorIns.carga(inscriptos)
    ManejadorIns.muestra(inscriptos)
    
    print("Menú")
    print("1 - Opcion 1")
    print("2 - Ingresar zona y ordenar por prioridad")
    
    option = int(input("Ingrese opcion > "))

    while option != -1:
        if  option == 1:
            ManejadorIns.informacion(inscriptos)
        elif option == 2:
            print("\n")
            ManejadorIns.ordenarPrioridad(inscriptos)
        
        option = int(input("Ingrese opcion > "))
    

if __name__ == "__main__":
    menu()