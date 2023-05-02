class ventana:
    __titulo = ''
    __x1 = 0
    __x2 = 0
    __y1 = 0
    __y2 = 0
    
    def __init__(self, titulo, x1=0,y1=0, x2=500, y2=500):
            self.__titulo = titulo
            self.__x1 = max(0,x1)
            self.__y1 = max(0,y1)            
            self.__x2 = min(500, x2)
            self.__y2 = min(500, y2)
            
    def mostrar(self):
        print(self.__titulo)
    
    def getTitulo(self):
        return(self.__titulo)
    
    def alto(self):
       return self.__y2 - self.__y1
        
    def ancho(self):
        return self.__x2 - self.__x1
    
    def moverDerecha(self, unidad=1):
        self.__x1 += unidad
        self.__x2 += unidad

    def moverIzquierda(self, unidad=1):
        self.__x1 -= unidad
        self.__x2 -= unidad

    def bajar(self, unidad=1):
        self.__y1 += unidad
        self.__y2 += unidad
        
    def subir(self, unidad=1):
        self.__y1 -= unidad
        self.__y2 -= unidad