from manejadorClientes import manejadorClientes as mC
from manejadorReparaciones import manejadorReparacion as mR

def menu():
    
    clientes = []
    mC.carga(clientes)
    # mC.muestra(clientes)
    
    reparaciones = []
    mR.carga(reparaciones)
    # mR.muestra(reparaciones)


    #Modulo 1 = Leer un DNI por teclado e informar los datos del cliente y todas las reparaciones hechas al vehiculo.
    mC.modulo1(clientes, reparaciones)

    #Leer una patente por teclado, determinar si todas las reparaciones estan terminadas, en caso afirmativo, cambiar el estado del cliente, y mostrar nombre y apellido del cliente, el telefono, el vehiculo y total a pagar.
    print("\n")
    mR.modulo2(reparaciones, clientes)

if __name__ == "__main__":
    menu()