from modulo_clase import ViajeroFrecuente
import csv

def menu(listaViajeros):
    
    def buscarViajero(num, listaViajeros):
        i = 0
        punto = 0
        band = False
        while i < len(listaViajeros) and band == False:
            if listaViajeros[i].getNum() == num:
                punto = i
                band = True
            i += 1
        return punto

    print("Menú")
    print("1 - Buscar mayor")
    print("2 - Acumular millas")
    print("3 - Canjear millas")
    print("4 - Mostrar info")
    print("-1 - Salir")
    
    option = int(input("Opción > "))
    
    while(option != -1):
        
        if (option == 1):
            mayor = 0
            ind = 0
            for i in range(len(listaViajeros)):
                if listaViajeros[i] > mayor:
                    ind = i
                    mayor = listaViajeros[i].getMillas()
            print ("El viajero con mayor millas acumuladas es: ", listaViajeros[ind].getinfo())
        
        if(option == 2):
            num = int(input("Numero de viajero > "))
            ind = buscarViajero(num, listaViajeros)
            xmillas = float(input("Ingrese millas para acumular > "))
            listaViajeros[ind] + xmillas
            
        
        if(option == 3):
            num = int(input("Numero de viajero > "))
            ind = buscarViajero(num, listaViajeros)
            xmillas = int(input("Ingrese millas para canjear > "))
            listaViajeros[ind] - xmillas
        
        if(option == 4):
            for i in range(len(listaViajeros)):
                print(listaViajeros[i].getinfo())
        
        option = int(input("Opción > "))
        
if __name__ == "__main__":  
    
    listaViajeros = []
    with open ("Ejercicio 6/dataviajeros.csv", 'r') as file_viajeros:
        next(file_viajeros)
        for file in file_viajeros:
            file = file.split(';')
            viaj = ViajeroFrecuente (int(file[0]), file[1], file[2], file[3], int(file[4]))
            listaViajeros.append(viaj)
        print("Info de viajeros cargada con éxito.")
    
    menu(listaViajeros)
    
