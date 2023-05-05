from class_conjunto import conjunto

def menu():
    
    print("Ingrese los elementos del primer conjunto, separados por ',' > ")
    elementA = list(map(int, input().split(",")))
    conjA = conjunto(elementA)
    
    print("Ingrese los elementos del segundo conjunto, separados por ',' >")
    elementB = list(map(int, input().split(",")))
    conjB = conjunto(elementB)
    
    print("Menú")
    print("1 - Unir conjuntos")
    print("2 - Diferencia de conjuntos")
    print("3 - Comprobar si los conjuntos son iguales") 
    print(" -1 Salir ")
    
    option = int(input("Ingrese opcion > "))
    
    while option != -1:
           
        if option == 1:
               unidad = conjA + conjB
               print("Unidad de ambos conjuntos > ", unidad)
            
        if option == 2:
            dif = conjA - conjB
            print("Diferencia de ambos conjuntos > ", dif)
            
        if option == 3:
            igualdad = (conjA == conjB)
            if(igualdad == True):
                print("Los conjuntos son iguales")
            if(igualdad == False):
                print("Los conjuntos no son iguales")        
           
        option = int(input("Ingrese opcion > "))
    
if __name__ == "__main__":
    menu()