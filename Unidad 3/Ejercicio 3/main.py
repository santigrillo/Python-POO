from manejadorInscripciones import manejadorInscripciones
from manejadorPersonas import manejadorPersonas
from manejadorTalleres import manejadorTalleres

def menu():
    print("Menu")
    print("1 - Carga inscripción.")
    print("2 - Muestra inscripciones.")
    print("3 - Muestra inscripciones por persona.")
    print("4 - Muestra inscriptos por taller.")
    print("5 - Registrar pago.")
    print("6 - Generar archivo.")

def test():
    mT = manejadorTalleres()
    mT.carga()
    
    mI = manejadorInscripciones()
    mP = manejadorPersonas()
    
    menu()
    option = int(input("Ingrese opcion > "))
    
    while option != 0:
        if option == 1:
            print("\n")
            mI.inscribir(mT, mP)    

        if option == 2:
            print("\n")
            mI.muestraInscripciones()
            
        if option == 3: 
            print("\n")
            mI.muestraInscripcionesPorPersona()
        
        if option == 4:
            print("\n")
            mT.muestrainscriptos()

        if option == 5:
            print("\n")
            mI.registrarPago()

        if option == 6:
            mI.generarArchivo()

            
        print("\n")
        menu()
        option = int(input("Ingrese opcion > "))
        
    
if __name__ == "__main__":
    test()