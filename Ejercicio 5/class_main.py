from class_plan import planAhorro
import csv

def menu(listaplanes):
    print("Menú")
    print("1 - Informar cada plan.")
    print("2 - Actualizar valor de cada plan.")
    print("3 - Mostrar planes inferiores")
    print("4")
    print("-1 - Salir")
    
    option = int(input("Ingrese opcion > "))  
    
    while (option != -1):
        
        if(option == 1):
            for i in range(len(listaplanes)):
                listaplanes[i].getInfo()
        
        if(option == 2):
            for i in range(len(listaplanes)):
                listaplanes[i].changeCarValue()
                
        if(option == 3):
            xvalor = float(input("Ingrese valor >"))
            for i in range(len(listaplanes)):
                if(listaplanes[i].getvalorCuota() < xvalor):
                    print(listaplanes[i].getInfo())
        
        option = -1
    
    
    
if __name__ == "__main__":
    
    listaplanes = []
    
    with open("Ejercicio 5/planes.csv",'r') as fileplanes:
        next(fileplanes)
        for file in fileplanes:
            file = file.split(';')
            plan = planAhorro(file[0], file[1], file[2], file[3], file[4], file[5])
            listaplanes.append(plan)
        print("Planes cargados con exito. ")            
    
    menu(listaplanes)