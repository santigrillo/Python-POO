import json
from classPersona import persona

class manejador:
    
    def __init__(self):
        self.__personas = []
        
    def addPersona(self, unaPersona):
        self.__personas.append(unaPersona)
        
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            personas = [persona.toJSON() for persona in self.__personas]
        )
        return d
    
    def mostrar(self):
        for i in range(len(self.__personas)):
            self.__personas[i].muestraInfo()