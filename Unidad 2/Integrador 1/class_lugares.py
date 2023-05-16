class lugar: 
    __zona = ""
    __lugar = ""
    
    def __init__(self, zona, lugar):
        self.__zona = zona
        self.__lugar = lugar
    
    def getInfo(self):
        return (self.__zona, self.__lugar)