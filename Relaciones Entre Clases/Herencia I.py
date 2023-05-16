#La herencia es un mecanismo que permite compartir automáticamente métodos y datos entre clases y subclases. Este mecanismo permite crear nuevas clases existentes programando solamente las diferencias.

class persona(object):
    __dni = str
    __nombre = str
    __apellido = str
    
    def __init__(self, dni, nombre,apellido):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        
    def getData(self):
        return self.__nombre, self.__apellido, self.__dni
    
       
class alumnoUNSJ(persona):
    __carrera = str
    
    def __init__(self, carrera, dni, nombre, apellido):
        self.__carrera = carrera
        super().__init__(dni, nombre, apellido)
        
    def muestraDatos(self):
        print(super().getData())
        print(self.__carrera)
        
class profesorUNSJ(persona):
    __departamento = str
    __titulo = str
    
    def __init__(self, depa, tit, dni, nombre, apellido):
        self.__departamento = depa
        self.__titulo = tit
        super().__init__(dni, nombre, apellido)
        
    def muestraDatos(self):
        print(super().getData())
        print("Departamento ",self.__departamento, "- Titulo " , self.__titulo)
        
def test():
    
    alumno = alumnoUNSJ("TUPW", 43013821, "Fede", "Lauria")
    alumno.muestraDatos()
    
    profesor = profesorUNSJ("Informatica", "Licenciado en sistemas", 24181210, "Juan", "Gimenez")
    profesor.muestraDatos()
    
if __name__ == "__main__":
    test()
        