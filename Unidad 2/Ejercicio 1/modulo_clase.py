class email:
    __idcuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __password = ''
    
    def __init__(self, xid=None, xdominio=None, xtipo=None, xpassword=None):
        self.__idcuenta = xid
        self.__dominio = xdominio
        self.__tipoDominio = xtipo
        self.__password = xpassword
        
    def __str__ (self):
        return(self.__idcuenta + "@" + self.__dominio + "." + self.__tipoDominio)
        
    
    def createAccount(self,correo,cont):
        if (correo.find('@')!= -1):
            auxCorreo= correo.split('@')
            user = auxCorreo[0]
            if (auxCorreo[1].find('.')!= -1):
                domCompleto= auxCorreo[1].split('.')
                auxDominio= domCompleto[0]
                auxTipoDominio= domCompleto[1]
                self.__init__(user,auxDominio,auxTipoDominio,cont)
                print('Correo creado con exito')
            else: print('Error: El dominio no contiene punto')
        else: print ('Error: El correo ingresado no contiene @') 
    
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
         
                    

    