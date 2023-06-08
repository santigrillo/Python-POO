import json

class persona:
    __nombre = str
    __apellido = str
    
    def __init__ (self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        
    def muestraInfo(self):
        print(self.__nombre, self.__apellido)
        
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.__nombre,
                apellido = self.__apellido,
            )
        )
        return d