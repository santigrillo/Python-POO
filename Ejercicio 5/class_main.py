from class_plan import planAhorro
import csv

def menu(listaplanes):
    print("Menú")
    print("1 - Informar cada plan.")
    print("2 - Actualizar valor de cada plan.")
    print("3 - Mostrar planes inferiores.")
    print("4 - Cuotas para licitar.")
    print("5 - Cambiar cuotas para licitar")
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
        
        if(option == 4):
            for i in range(len(listaplanes)):
                listaplanes[i].total_licitar()

        if (option == 5):
            ind = 0
            band = False
            codigo = input("Ingrese codigo de plan > ")
            while ind < len(listaplanes) and band == False:
                if (listaplanes[ind].getCode() == codigo):
                    listaplanes[ind].cambioCuotas()
                    band = True
                ind += 1
            
        option = int(input("Ingrese opcion > ")) 
    
if __name__ == "__main__":
    
    listaplanes = []
    
    with open("Ejercicio 5/planes.csv",'r') as fileplanes:
        next(fileplanes)
        for file in fileplanes:
            file = file.split(';')
            plan = planAhorro(file[0], file[1], file[2], int(file[3]), int(file[4]), int(file[5]))
            listaplanes.append(plan)
        print("Planes cargados con exito. ")            
    
    menu(listaplanes)