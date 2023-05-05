class conjunto:
    __elementos = ""
    
    def __init__(self, elementos=""):
        self.__elementos = set(elementos)
    
    def __str__(self):
        return self.__elementos
    
    def __add__(self, segundoconjunto):
        union = self.__elementos | segundoconjunto.__elementos
        return union

    def __sub__ (self, segundoconjunto):
        dif = self.__elementos - segundoconjunto.__elementos
        return dif

    def __eq__ (self, segundoconjunto):
        return self.__elementos == segundoconjunto.__elementos
    