#Un objeto de una clase contiene como partes a objetos de otras clases y estas partes están fisicamente contenidas por el agregado.
#Los tiempos de vida de los objetos continente y contenido están estrechamente acoplados.
#La destrucción del objeto continente implica la destrucción de sus partes.

#Profesor contiene cuenta de campus.

#Contexto = Cuando se crea un nuevo Profesor, se crea automaticamente la cuenta en el campus, que será su nombre y apellido en minusculas, seguido por el dominio. La clave por defecto será su numero de documento. El idUsuario es un número consecutivo que comienza desde el cero, y se incrementa cada nuevo usuario.

class cuentaCampus:
    __dominio = "@unsj-cuim.edu.ar"
    __idCuenta = 0
    __idUsuario = int
    __nombreUsuario = str
    __clave = str
    
    @classmethod
    def getDominio(cls):
        return cls.__dominio
    
    @classmethod
    def getidCuenta(cls):
        cls.__idCuenta += 1
        return cls.__idCuenta
    
    def __init__(self, idUsuario, nombreUsuario, clave):
        self.__idUsuario = idUsuario
        self.__nombreUsuario = nombreUsuario
        self.__clave = clave
        
    def __str__(self):
        cadena = "Usuario {}\nClave {}".format(self.__nombreUsuario, self.__clave)
        return cadena
        
    def cambiarClave(self):
        newPass = input("Ingrese nueva clave: ")
        self.__clave = newPass  
        
class profesor:
    __dni = str
    __apellido = str
    __nombre = str
    __cuentaCampus: object
    
    def __init__(self, dni, apellido, nombre):
        self.__dni = dni 
        self.__nombre = nombre
        self.__apellido = apellido
        idCuenta = cuentaCampus.getidCuenta()
        dominio = cuentaCampus.getDominio()
        user = nombre.lower()+apellido.lower()+dominio
        self.__cuentaCampus = cuentaCampus(idCuenta, user, dni)
        
    def __del__(self):
        print("Borrando profesor..")
        del self.__cuentaCampus
    
    def getInfo(self):
        print("Profesor: ")
        print("Apellido y nombre: {},{}".format(self.__apellido, self.__nombre))
        print(self.__cuentaCampus)
        
    
def test():
    dni = input("DNI: ")
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    
    prof1 = profesor(dni, apellido, nombre)
    print("\n")
    prof1.getInfo()
    
    del prof1
    
if __name__ == "__main__":
    test()
    