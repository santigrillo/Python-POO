from class_reparaciones import reparacion
from manejadorClientes import manejadorClientes

class manejadorReparaciones:

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
            
    
    