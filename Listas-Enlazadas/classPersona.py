class persona:
    __nombre = str
    
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre