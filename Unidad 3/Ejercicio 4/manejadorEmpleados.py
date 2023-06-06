import numpy as np
from classEmpleado import empleado
from classExterno import externo
from classPlanta import planta
from classContratado import contratado


class manenajadorEmpleados:

    def __init__(self):
        self.__empleados = []
        
    def cargaPlanta(self):
        
        with open("Unidad 3/Ejercicio 4/archivos/planta.csv") as filePlanta:
            next(filePlanta)
            for file in filePlanta:
                file = file.split(';')
                unEmpleadoPlanta = planta(file[0], file[1], file[2], int(file[3]), int(file[4]))
                self.__empleados.append(unEmpleadoPlanta)
                

    def cargaContratados(self):

        with open("Unidad 3/Ejercicio 4/archivos/contratados.csv", 'r') as fileContrato:
            next(fileContrato)
            for file in fileContrato:
                file = file.split(';')
                unEmpleadoContratado = contratado(file[0], file[1], file[2], file[3], file[4])
                self.__empleados.append(unEmpleadoContratado)

    
    def cargaExternos(self):

        with open("Unidad 3/Ejercicio 4/archivos/externo.csv", 'r') as fileExt:
            next(fileExt)
            for file in fileExt:
                file = file.split(';')
                unEmpleadoExt = externo(file[0], file[1], file[2], file[3], file[4], file[5], int(file[6]), int(file[7]), int(file[8]), file[9])
                self.__empleados.append(unEmpleadoExt)
        
    def registrarHoras(self):
        contEncontrados = 0
        horasSumadas = False
        xDNI = input(("Ingrese DNI de un empleado externo para agregar horas > "))
        i = 0
        
        while i < len(self.__empleados) and not horasSumadas:
            if (self.__empleados[i].getDNI() == xDNI):
                self.__empleados[i].sumarHoras()
                horasSumadas = True
            else:
                i += 1
            if i == len(self.__empleados):
                print("Empleado no encontrado.")
                
    def totalTarea(self):
        self.mostrarTareas()
        total = 0
        xTarea = input("Ingrese tarea a consultar total > ")
        tareaEncontrada = False
        for i in range(len(self.__empleados)):
            if(self.__empleados[i].getTarea() == xTarea):
                print("Tarea encontrada.")
                total += int(self.__empleados[i].getCostoTarea())
                tareaEncontrada = True
        if tareaEncontrada == False:
            print("Tarea no encontrada.")
        print("El total para ", xTarea, "es", total)
        
    def mostrarTareas(self):
        for i in range(len(self.__empleados)):
            if (isinstance(self.__empleados[i], externo)):
                self.__empleados[i].getInformacionTarea()
                
    def ayudaEconomica(self):
        xSueldoMenorA = float(input("Ingrese el sueldo para buscar empleados que percibiran la ayuda economica > $"))
            
        for i in range(len(self.__empleados)):
            # self.__empleados[i].getInfoEmpleado()
            # print("Sueldo >", self.__empleados[i].calcularSueldo())
            if(int(self.__empleados[i].calcularSueldo()) < xSueldoMenorA):
                self.__empleados[i].getInfoEmpleado()
            
    def muestraSueldos(self):
        for i in range(len(self.__empleados)):
            self.__empleados[i].getInfoEmpleado()
            print("Sueldo >", self.__empleados[i].calcularSueldo())
            