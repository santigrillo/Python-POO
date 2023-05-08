from class_inscripto import inscripto

class ManejadorIns:
    def carga(inscriptos):
        with open ("Integrador 1/inscriptosVac.csv", 'r') as fileinscriptos:
            next (fileinscriptos)
            for file in fileinscriptos:
                file = file.split(";")
                i = inscripto(file[0], file[1], file[2], int(file[3]), file[4], file[5], file[6])
                inscriptos.append(i)
        return inscriptos
                  
    def muestra(inscriptos):
        for i in range(len(inscriptos)):
            print(inscriptos[i].getInfo())
            
    def informacion(inscriptos):
        edad = int(input("Ingrese edad > "))
        cantSinFactor = 0
        cantConFactor = 0
        for i in range(len(inscriptos)):
                if (inscriptos[i].getEdad()== edad) and (inscriptos[i].getFactor() == "Ninguno"):
                    cantSinFactor += 1
                elif (inscriptos[i].getEdad()== edad) and (inscriptos[i].getFactor() != "Ninguno"):
                    cantConFactor += 1
                        
        print("Con ", edad, " años, hay ", cantSinFactor, " inscriptos sin factor")
        print("Con ", edad, " años, hay ", cantConFactor, " inscriptos con factor")

            
    def ordenarPrioridad(inscriptos):
        zona = input("Ingrese zona > ")
        listazona = []
        for i in range(len(inscriptos)):
            if(inscriptos[i].getZona()==zona):
                listazona.append(inscriptos[i])
        
        listazona.sort(reverse=False)            
        for i in range(len(listazona)):
            print(listazona[i].getInfo())
        
    
                
                
        