class cliente:
    __idCliente = 0
    __NyA = ""
    __domicilio =""
    __facturas = list 

    def __init__ (self, xid, nya, direccion):
        self.__idCliente = xid
        self.__NyA = nya
        self.__domicilio = direccion
        self.__facturas = []

    def addFactura(self, unafactura):
        self.__facturas.append(unafactura)
        
    def muestraFacturas(self):
        print("Nro Factura\tFecha\t\tImporte")
        for i in range(len(self.__facturas)):
            self.__facturas[i].getFactura()

class factura:
    __numeroFactura = 0
    __fecha = ""
    __importe = float(0)
    __cuit = ""
    __denominacionNegocio = ""

    def __init__(self, nrof, date, importe, cuit, denominacionNeg): 
        self.__numeroFactura = nrof
        self.__fecha = date
        self.__importe = importe
        self.__cuit = cuit
        self.__denominacionNegocio = denominacionNeg
        
    def getFactura(self):
        print(self.__numeroFactura, "\t\t", self.__fecha, "\t",self.__importe)
        
def test():
    uncliente = cliente(1, "Mateo Perez", "Av. Libertador")
    
    factura1 = factura('223','27/01/2020',4500, '30-33333323-1', 'Calzados la Zapa')
    uncliente.addFactura(factura1)
    
    factura2 = factura('441','27/01/2020',6500, '27-12334333-1', 'Deportes ABC')
    uncliente.addFactura(factura2)
    
    factura3 = factura('223','27/01/2020',8500, '20-31333333-1', 'Bicicletería la BICI')
    uncliente.addFactura(factura3)
    
    uncliente.muestraFacturas()
    
if __name__ == "__main__":
    test()
        