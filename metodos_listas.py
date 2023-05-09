class auto:
    __nombreAuto = ' '
    __tipoDeCombustible = ' '
    __capacidadTanque = ' '

    def __init__ (self, xnombreAuto, xtipoDeCombustible, xcapacidadTanque):
        self.__nombreAuto = xnombreAuto
        self.__tipoDeCombustible = xtipoDeCombustible
        self.__capacidadTanque = xcapacidadTanque
    
    def __str__ (self):
        return f'el auto es: {self.__nombreAuto}'
        
    def getAuto(self):
        return(self.__nombreAuto)
    
    def getCapacidad(self):
        return(self.__capacidadTanque)
        

def crearAuto():
    print("Ingrese los siguientes datos:")
    xnombreAuto = input("Nombre del auto: ")
    xtipoDeCombustile = input("Tipo de combustible: ")
    xcapacidadTanque = float(input("Capacidad del tanque(en litros): "))
    print("\n")
    AutoCreado = auto(xnombreAuto, xtipoDeCombustile, xcapacidadTanque)
    return AutoCreado

def cargaAutos(listaAutos, long):
    for i in range(long):
     a = crearAuto()
     listaAutos.append(a)

def borrarAuto(listaAutos):
    borrado = False
    auto_borrar = input("Ingrese nombre del auto a borrar: ")
    while i<len(listaAutos) and (borrado == False):
        if i.getAuto() == auto_borrar:
            listaAutos.remove(i)
            borrado = True
            
def funcionOrdenar(listaAutos):
    listaAutos.sort(key=lambda i: i.getCapacidad(), reverse = True)
     
if __name__ == '__main__':
    listaAutos = []
    long = int(input("Cuantas autos quiere cargar: "))
    cargaAutos(listaAutos, long)
    # funcionOrdenar(listaAutos)
    for i in range(len(listaAutos)):
        print(listaAutos[i])

    # almacena_valor = listaAutos.pop()
    # print('El auto eliminado y almacenado es:',  almacena_valor)
    
    # for i in range(len(listaAutos)):
    #     print(listaAutos[i])
    
    listaAutos.clear()
    print("Lista de autos disponibles.")
    for i in range(len(listaAutos)):
        print(listaAutos[i])
