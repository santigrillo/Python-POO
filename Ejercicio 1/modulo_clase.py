class email:
    __idcuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __password = ''
    
    def __init__(self, xid, xdominio, xtipo, xpassword):
        self.__idcuenta = xid
        self.__dominio = xdominio
        self.__tipoDominio = xtipo
        self.__password = xpassword 
        
    def returncorreo(self):
       print(self.__idcuenta+self.__dominio+self.__tipoDominio) 
   
    def getDominio(self):
        return("El dominio es "+self.__dominio)      
        
    def changePassword(self):
        print ("Modulo cambio contraseña")
        indice = 0
        while indice < 3:
            claveanterior = input("Ingrese clave anterior: ")
            if (claveanterior == self.__password):
                clavenueva = input("Ingrese nueva clave: ")
                self.__password = clavenueva
                indice = 3
                print ("Clave cambiada con éxito")
            else:
                print("Clave mal ingresada")
                indice += 1 
            if (indice > 3):
             print("La contaseña se ingresó mal demasiadas veces, pruebe mas tarde")
         
                    

    