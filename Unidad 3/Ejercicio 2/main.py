from mSabores import manejadorSabores as mS
from mHelados import manejadorHelados as mH

def test():
    sabores = []
    mS.carga(sabores)
    
    helados = []
    
    print("Menu")
    print("1 - Vender helado")
    print("2 - Mostrar helados mas vendidos.")
    print("3 - Informacion de pedidos.")
    option = int(input("Ingrese opcion = "))
    
    while option != 0:
        if option == 1:
            mH.ventaHelado(helados, sabores)
            
        if option == 2: 
            mS.modulo2(sabores)
            
        if option == 3:
            mH.muestraSaboresPorHelado(helados)

        option = int(input("Ingrese opcion = "))

    
    
if __name__ == "__main__":
    test()