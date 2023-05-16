class medico:
    __dni= int  
    __matricula= int
    ___apellido=str
    __nombre= str
    __prescripciones= []
    
    def __init__(self, dni, matricula, especialidad, apellido, nombre):
        self.__dni=dni
        self.__matricula=matricula
        self.__especialidad=especialidad
        self.__apellido=apellido
        self.__nombre=nombre    
    
    def addPrescipcion(self, prescripcion):
        self.__prescripciones.append(prescripcion)
        
    def muestraPrescripciones(self):
        print("\n")
        print("Prescripciones del medico ", self.__apellido, self.__nombre)
        for i in range(len(self.__prescripciones)):
            self.__prescripciones[i].getInfo(self.__nombre)
    
    def getNomb(self):
        return(self.__nombre)

class paciente:
    __dni= int
    __apellido= str
    __nombre= str
    __prescripciones = []
    
    def __init__(self, dni, apellido, nombre):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
    
    def addPrescripcion(self, prescripcion):
        self.__prescripciones.append(prescripcion)

    def muestraPrescripciones(self):
        print("Prescripciones de ", self.__apellido, self.__nombre)
        for i in range(len(self.__prescripciones)):
            self.__prescripciones[i].getInfoPac(self.__nombre)
            
    def getNomb(self):
        return(self.__nombre)

class Prescripcion:
    __fecha: str
    __diagnostico: str
    __medicacion: str
    __presentacion: str
    __dosis: str
    __paciente: object
    __medico: object
    
    def __init__(self, fecha, diagnostico, medicacion,
    presentacion, dosis, medico, paciente):
        self.__fecha=fecha
        self.__diagnostico=diagnostico
        self.__medicacion=medicacion
        self.__presentacion=presentacion
        self.__dosis=dosis
        self.__medico=medico
        self.__paciente=paciente
        self.__medico.addPrescipcion(self)
        self.__paciente.addPrescripcion(self)
        
    def getInfoPac(self, nombre):
        if self.__paciente.getNomb() == nombre:
            print("Fecha ", self.__fecha, "Parte médico ", self.__diagnostico)
            
    def getInfo(self, nombre):
        if self.__medico.getNomb() == nombre:
            print("Fecha ", self.__fecha, "Parte médico ", self.__diagnostico, " Paciente ", self.__paciente.getNomb())

def testClaseModelaAsociacion():
    pac = paciente(14555699, 'Vergara', 'Andrea')
    pac1 = paciente(14555699, 'Gomez', 'Mateo')
    
    med = medico(19327881, 1125, 'Clínica Médica','González', 'Jorge')
    
    prescripcion = Prescripcion('11/01/2020', 'Rinitis', 'Hexaler','10 comprimidos', '1 por día',med, pac)
    prescripcion2 = Prescripcion('29/01/2020', 'Otitis', 'Ciriax Gotas', 'envase 10 ml', '2 gotas cada 8h',med, pac1)
    prescripcion3 = Prescripcion('29/01/2022', 'Covid', 'Tafirol', 'Comprimido', '1 por dia',med, pac) 
    
    pac1.muestraPrescripciones()
    med.muestraPrescripciones()
    print("\n")

if __name__=='__main__':
    testClaseModelaAsociacion()