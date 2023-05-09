class evaluacion: 
    __dni = ""
    __estilo = ""
    __puntaje = [0, 0, 0] #3 Puntajes
    
    def __init__(self, dni, estilo, nota1, nota2, nota3):
        self.__dni = dni
        self.__estilo = estilo
        self.__puntaje[0] = nota1 #Puntaje 1 
        self.__puntaje[1] = nota2 #Puntaje 2
        self.__puntaje[2] = nota3 #Puntaje 3
        
    def getEstilo(self):
        return(self.__estilo)
    
    def getDNI(self):
        return(self.__dni)