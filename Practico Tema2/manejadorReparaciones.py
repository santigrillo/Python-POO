from class_reparaciones import reparacion

class manejadorReparacion:

    def carga (reparaciones):
        with open ("Practico Tema2/archivos/reparaciones.csv", 'r') as fileR:
            next(fileR)
            for file in fileR:
                file = file.split(';')
                rp = reparacion(file[0], file[1], file[2], float(file[3]), float(file[4]), file[5])
                reparaciones.append(rp)
                
            print("== Reparaciones Cargadas ==")
            
    def muestra (reparaciones):
        for i in range(len(reparaciones)):
            reparaciones[i].getInfo()
            
    def getReparacionesByPatente(reparaciones, patente):
        total = 0
        for i in range(len(reparaciones)):
            if(reparaciones[i].getPatente()==patente):
                print("Reparacion = ",reparaciones[i].getReparacion(), "Precio de repuesto = $",reparaciones[i].getPrecioRp(), " Precio mano de obra = $", reparaciones[i].getPrecioMo(), "Subtotal = $", (reparaciones[i].getPrecioRp()+reparaciones[i].getPrecioMo()))
                total += reparaciones[i].getTotal()
        print("Total a pagar $", total)
    
    def modificarEstadoByPatente(clientes, patente):
        i = 0
        band = False
        
        while i < len(clientes) and band == False:
            if(clientes[i].getPatente() == patente):
                    clientes[i].modificarEstado()
                    band = True
            else: 
                i+=1         
                
        print("Estado cambiado")
  
         
    
    def modulo2(reparaciones, clientes):
        band = False
        patente = "AC001CA" #input("Ingrese patente > ")
        i = 0
        
        while i < len(reparaciones) and band == False:
            if (reparaciones[i].getPatente() == patente) and (reparaciones[i].getEstado() == 'P'):
                band = True
            else: 
                i+=1
                
        if band == True:
            print("Hay reparaciones pendientes")
        else:
            print("Todas las reparaciones están terminadas")
        
        manejadorReparacion.modificarEstadoByPatente(clientes, patente)
        print("Patente ", patente)
        manejadorReparacion.getReparacionesByPatente(reparaciones, patente)