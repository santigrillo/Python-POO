from class_inscripcion import inscripcion
import csv

class manejadorInscripciones:
    
    def __init__(self):
        self.__inscripciones = []
        
    def addInscripcion (self, inscripcion):
        self.__inscripciones.append(inscripcion)

    def inscribir(self, mT, mP):
        nombre = input("Ingrese nombre y apellido > ")
        direccion = input("Ingrese direccion de "+ nombre +" > ")   
        dni = input("Ingrese dni de " + nombre + " > ")   

        unapersona = mP.addPersona(nombre, direccion, dni)        
        
        mT.muestraTalleres()
        tallerID = int(input("\n Ingrese ID al que se va a inscribir = "))
        
        unainscripcion = inscripcion("29/05/2023", unapersona, mT.getTaller(tallerID))
        
        self.addInscripcion(unainscripcion)
        
        mT.setInscripcion(tallerID, unainscripcion)
        
        print("Inscripcion realizada.\n")
        unainscripcion.getInfo()
        
    def muestraInscripciones(self):
        print("Lista de inscripciones.")
        for i in range(len(self.__inscripciones)):
            self.__inscripciones[i].getInfo()
            
    def muestraInscripcionesPorPersona(self):
        xDNI = input("Ingrese DNI de la persona a buscar > ")
        total = 0
        cont = 0
        for i in range(len(self.__inscripciones)):
            if(self.__inscripciones[i].getDniInscripto() == xDNI):
                self.__inscripciones[i].getInfoTaller()
                if(self.__inscripciones[i].getEstado() == False):
                    cont += 1
                    total += int(self.__inscripciones[i].getMonto())
        if(total != 0):
            print("Debe pagar", cont, "taller/es, el monto es $", total)
        else:
            print("El alumno no tiene o no debe abonar nada.")
            
    def registrarPago(self):
        debecurso = False
        xDNI = input("Ingrese DNI del alumno > ")
        for i in range(len(self.__inscripciones)):
            if(self.__inscripciones[i].getDniInscripto() == xDNI):
                if(self.__inscripciones[i].getEstado() == False):
                    self.__inscripciones[i].getInfoTaller()
                    print("Indice de inscripcion = ", i)
                    print("El monto es $", self.__inscripciones[i].getMonto())
                    debecurso = True
        if debecurso:
            xID = int(input("\nIngrese indice de inscripción a pagar = "))
            self.__inscripciones[xID].pagar()
        if not debecurso:
            print("El alumno no debe cursos.")    
            
    def generarArchivo(self):
        with open("Unidad 3/Ejercicio 3/archivogenerado.csv", 'a', newline='') as NewFile:
            newline = csv.writer(NewFile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for inscripcion in self.__inscripciones:
                line = (inscripcion.getDniInscripto(), inscripcion.getIDTaller(), inscripcion.getFecha(), inscripcion.getEstado2())
                newline.writerow(line)
                
                            