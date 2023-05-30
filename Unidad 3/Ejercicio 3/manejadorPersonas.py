from class_persona import persona

class manejadorPersonas: 
        
    def __init__ (self):
        self.__personas = []
        
    def addPersona (self, nombre, direccion, dni):
        unapersona = persona(nombre, direccion, dni)
        self.__personas.append(unapersona)
        return unapersona
            
        