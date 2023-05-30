from classEvaluacion import evaluacion
from classFederado import federado

class manejador:

    __federados = list
    __evaluaciones = list
    
    def __init__(self):
        self.__federados = []
        self.__evaluaciones = []
        
    def cargaFederados(self):
        with open("Practica Operativa T1/archivos/federados.csv", 'r') as fileFederados:
            for file in fileFederados:
                file = file.split(';')
                f = federado(file[0], file[1], file[2], file[3], file[4])
                self.__federados.append(f)
    
    def cargaEvaluaciones(self):
        with open("Practica Operativa T1/archivos/evaluacion.csv", 'r') as fileEv:
            for file in fileEv:
                file = file.split(';')
                ev = evaluacion(file[0], file[1], float(file[2]), float(file[3]), float(file[4]))
                self.__evaluaciones.append(ev)
                
    def buscarAlByDNI(self, xDNI):
        i=0
        valorRetorno = 0
        Bandera = False
        while i < len(self.__federados) and Bandera == False:
            if (self.__federados[i].getDNI() == xDNI):
                valorRetorno = i
                Bandera = True
            else:
                i+=1
        return valorRetorno
                
    def modulo1(self):
        style = input("Ingrese estilo > ")
        edad = input("Ingrese edad > ")

        for i in range(len(self.__evaluaciones)):
            if self.__evaluaciones[i].getEstilo().lower() == style:
                xDNI = self.__evaluaciones[i].getDNI()
                indice = self.buscarAlByDNI(xDNI)

                if self.__federados[indice].getEdad() == edad:
                    self.__federados[indice].getInfo()

                    
    def modulo2(self):
        self.__evaluaciones.sort(key=lambda i: i.getProm(), reverse=True)
        xDNI = self.__evaluaciones[0].getDNI()
        indice = self.buscarAlByDNI(xDNI)
        print("El alumno con mayor promedio es ")
        print(self.__federados[indice].getInfo())
        print(self.__evaluaciones[0].getProm())
        
    def modulo3 (self):
        print("Alumnos que rindieron estilo libre")
        for i in range(len(self.__evaluaciones)):
            if (self.__evaluaciones[i].getEstilo() == 'L'):
                    xDNI = self.__evaluaciones[i].getDNI()
                    indice = self.buscarAlByDNI(xDNI)
                    print(self.__federados[indice].getInfo())
                    
    def modulo4(self):
        dni = input("Ingrese DNI > ")
        style = input("Ingrese Estilo > ")
        for i in range(len(self.__evaluaciones)):
            if (self.__evaluaciones[i].getEstilo().lower() == style):
                if(self.__evaluaciones[i].getDNI() == dni):
                    xDNI = self.__evaluaciones[i].getDNI()
                    indice = self.buscarAlByDNI(xDNI)
                    print(self.__federados[indice].getInfo())
                    print(self.__evaluaciones[i].notas())