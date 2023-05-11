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
                print("Reparacion = ",reparaciones[i].getReparacion(), "Precio de repuesto = $",reparaciones[i].getPrecioRp(), " Precio mano de obra = $", reparaciones[i].getPrecioMo(), "Subtotal = $", (reparaciones[i].getPrecioRp()+reparaciones[i].getPrecioMo()), "\n")
                total += reparaciones[i].getTotal()
            
        print("Total a pagar $", total)
    