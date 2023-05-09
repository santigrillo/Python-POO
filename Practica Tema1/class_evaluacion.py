class evaluacion: 
    __dni = ""
    __estilo = ""
    __nota1 = 0
    __nota2 = 0
    __nota3 = 0
    
    
    def __init__(self, dni, estilo, nota1, nota2, nota3):
        self.__dni = dni
        self.__estilo = estilo
        self.__nota1 = nota1 #Puntaje 1 
        self.__nota2 = nota2 #Puntaje 2
        self.__nota3 = nota3 #Puntaje 3
        
    def getEstilo(self):
        return(self.__estilo)
    
    def getDNI(self):
        return(self.__dni)
    
    def getPromedio(self):
        notas = (self.__nota1 + self.__nota2 + self.__nota3) 
        return notas / 3
    
    def getNota(self):
        print("Nota 1 ", self.__nota1, "\nNota 2", self.__nota2, "\nNota 3", self.__nota3)
        