from class_carrera import carrera

class facultad:
    __codigo = str
    __nombre = str
    __direccion  = str
    __localidad = str
    __telefono = str
    
    def __init__(self, cod, nom, dire, loc, tel):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = dire
        self.__localidad = loc
        self.__telefono = tel
        self.__carreras = []
    
    def getNomb(self):
        return(self.__nombre)
            
    def addCarrera(self, unacarrera):
        self.__carreras.append(unacarrera)
        
    def getCod(self):
        return(self.__codigo)
    
    def infoModulo1(self):
        print(self.__nombre)
        for i in range(len(self.__carreras)):
            self.__carreras[i].infomd1()
        
    def getCeI(self):
        return(self.__nombre, "cod", self.__codigo)
    
    def infomd2(self, carreraFind):
        for i in range(len(self.__carreras)):
            if(self.__carreras[i].getnomb().lower() == carreraFind):
                self.__carreras[i].infomd1()
                print("Codigo",self.__carreras[i].getCod())
                print("= Informacion de la facultad =")
                print(self.__nombre, "Localidad", self.__localidad)
    