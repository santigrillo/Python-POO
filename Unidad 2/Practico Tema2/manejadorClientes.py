from class_cliente import cliente
from manejadorReparaciones import manejadorReparacion

class manejadorClientes:        
    
    def carga(clientes): 
        with open ("Practico Tema2/archivos/clientes.csv", 'r') as fileCliente:
            next (fileCliente)
            for file in fileCliente:
                file = file.split(';')
                cl = cliente(file[0], file[1], file[2], file[3], file[4], file[5], file[6])
                clientes.append(cl)
                
        print("== Clientes cargados == ")
        
    def muestra(clientes):
        print("Apellido - Nombre - DNI")
        for i in range(len(clientes)):
            clientes[i].getInfo()         
            
    def getPatente (clientes, dni):
        pat = ""
        for i in range(len(clientes)):
            if(clientes[i].getDNI() == dni):
                pat = clientes[i].getPatente()
        return pat
    
    def getClienteByDNI (clientes, dni):
        band = False
        i = 0
        while i < len(clientes) and band == False:
            if(clientes[i].getDNI() == dni):
             band = True
            else:
                i+=1
        return i  
    
            
            
    def modulo1(clientes, reparaciones):
        dni = "21111223" #input("Ingrese DNI > ")
        patente = manejadorClientes.getPatente(clientes, dni)
        cID = manejadorClientes.getClienteByDNI(clientes, dni)
        print("\n")
        clientes[cID].getInfo()
        clientes[cID].getVehiculo()
        manejadorReparacion.getReparacionesByPatente(reparaciones, patente)
        