#Agregación I 
#Un objeto de una clase contiene como partes a objetos de otras partes.
#La destrucción del objeto continente no implica la destruccion de sus partes.
#Los tiempos de vida de los objetos continentes y contenido no están acoplados, de modo que se pueden crear y destruir instancias de cada clase independiente.

#Orden contiene un objeto/s de bebida, objeto/s de plato y un mozo.

class bebida: 
    __denominacion = str
    __presentacion = str
    __precio = float
    
    def __init__(self, denominacion, presentacion, precio):
        self.__denominacion = denominacion
        self.__presentacion = presentacion
        self.__precio = precio
    
    def getPrecio(self):
        return self.__precio
    
    def getDenominacion(self):
        return self.__denominacion, self.__precio
class plato:
    __descripcion = str
    __precio = float

    def __init__(self, descripcion, precio):
        self.__descripcion = descripcion
        self.__precio = precio
        
    def getPrecio(self):
        return self.__precio
    
    def getDescripcion(self):
        return self.__descripcion, self.__precio 
class mozo:
    __idMozo = int
    __apellido = str
    __nombre = str
    
    def __init__(self, idmozo, apellido, nombre):
        self.__idMozo = idmozo
        self.__apellido=apellido
        self.__nombre=nombre
class pedido:
    __cantPedidos = 0
    __idPedido = int
    __nroMesa = int
    __mozo = object
    __bebidas = []
    __platos = []
    
    def __init__(self, nromesa, mozo, bebida = None, plato = None):
        self.__mozo = mozo
        self.__nroMesa = nromesa
        self.__idPedido = self.getIdPedido()
            
    @classmethod
    def getIdPedido(cls):
        cls.__cantPedidos += 1
        return (cls.__cantPedidos)
    
    def addBebida(self, bebida, cantidad):
        for i in range(cantidad):
            self.__bebidas.append(bebida)
            
    def addPlato(self, plato, cantidad):
        for i in range(cantidad):
            self.__platos.append(plato)
            
    def cerrarPedido(self):
        print("Pedido nro > ", self.__idPedido)
        total = 0
        print("\n")
        print("Bebidas")
        for bebida in self.__bebidas:
            precio = bebida.getPrecio()
            print(bebida.getDenominacion())
            total += precio
            
        print("\n")
        print("Platos")
        for plato in self.__platos:
            precio = plato.getPrecio()
            print(plato.getDescripcion())
            total += precio
        print("\n")
        print("Total a pagar $", total)
        

def test():    
    
    print ("Menu pedidos")
    print("Opcion 1 - Crear pedido.")
    print("Opcion 2 - Agregar bebida.")
    print("Opcion 3 - Agregar plato.")
    print("Opcion 4 - Cerrar pedido.")
    
    option = int(input("Ingrese opcion > "))
    while option != -1:
        if option == 1:
            xid = 1
            nombmozo = "Mateo"
            appmozo = "Gomez"
            mozo1 = (xid, nombmozo, appmozo)
            pedido1 = pedido(mozo1, bebida, plato)
        
        if option == 2:
            producto = input("Ingrese bebida > ")
            descripcion = input("Ingrese contenido > ")
            precio = float(input("Ingese precio > "))
            b1 = bebida(producto, descripcion, precio)
            cant = int(input("Ingrese cantidad de " + producto + " "))
            pedido1.addBebida(b1, cant)
        
        if option == 3:
            descripcion = input("Ingrese plato > ")
            precio = float(input("Ingrese precio > "))
            p1 = plato(descripcion, precio)
            cant = int(input("Ingrese cantidad de " + descripcion + " "))
            pedido1.addPlato(p1, cant)
            
        if option == 4:
            pedido1.cerrarPedido()
            
        option = int(input("Ingrese opcion > "))
        
if __name__ == "__main__":
    test()