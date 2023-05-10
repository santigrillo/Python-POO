from manejadorClientes import manejadorClientes as mC
from manejadorReparaciones import manejadorReparaciones as mR

def menu():
    
    clientes = []
    mC.carga(clientes)
    # mC.muestra(clientes)
    
    reparaciones = []
    mR.carga(reparaciones)
    # mR.muestra(reparaciones)












if __name__ == "__main__":
    menu()