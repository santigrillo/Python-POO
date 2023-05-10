from class_cliente import cliente

class manejadorClientes:        
    
    def carga(clientes): 
        with open ("Practico Tema2/archivos/clientes.csv", 'r') as fileCliente:
            next (fileCliente)
            for file in fileCliente:
                file = file.split(';')
                cl = cliente(file[0], file[1], file[2], file[3], file[4], file[5])
                clientes.append(cl)
                
        print("== Clientes cargados == ")
        
    def muestra(clientes):
        print("Apellido - Nombre - DNI")
        for i in range(len(clientes)):
            clientes[i].getInfo()         