from classPersona import persona

class nodo:
    __dato = persona
    next = None
    
    def __init__(self, persona):
        self.__dato = persona
    
    def getDato(self):
        return self.__dato   
        