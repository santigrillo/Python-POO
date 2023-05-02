from modulo_clase import registro
import csv

def menu(info):
    print("Menú")
    print("1 - Cargar información.")
    
    option = int(input("Ingrese opcion > "))
    while(option != -1):
        if (option == 1):
            with open("Ejercicio 3/inforegistros.csv", 'r') as data:
                data_reader = csv.reader(data, delimiter=';')
                for line in data_reader:
                    line = line.split(';')
                    dia = int(line[0])
                    hora = int(line[1])
                    info[hora][dia-1] = registro(float(line[2]), float(line[3]), float(line[4]))
                print("Registros cargados con éxito.")
        
        if (option == 2):
            encontrar_min_max(info, 'temperatura')
        
        
        option = int(input("Ingrese opcion > "))  





if __name__ == "__main__":
    info = [[registro(0, 0, 0) for i in range(31)] for i in range(24)]
    menu(info)