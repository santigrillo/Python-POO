from classbeca import beca
from manejadorBeneficiarios import manejadorBeneficiarios
mbs = manejadorBeneficiarios()

class manejadorBeca:
    __becas = []
    
    def __init__ (self):
        __becas = []
    
    def carga(self):
        with open("RPO/becas.csv", 'r') as filebecas:
            next (filebecas)
            for file in filebecas:
                file = file.split(';')
                unabeca= beca(int(file[0]), file[1], file[2])
                self.__becas.append(unabeca)
        print("Carga de becas.")
        
    def modulo1(self):
            
        tipobeca = input("Ingrese tipo de beca > ")
        
        i = 0
        becaid = 0
        
        while i < len(self.__becas) and (self.__becas[i].getnombre() != tipobeca):
            i += 1 
        
        if i < len(self.__becas):
                becaid = self.__becas[i].getid()
                
        return becaid
    

    def modulo2muestra(self, becaslista):
        contbecas = 0
        for i in range(len(becaslista)):
            contbecas += 1
            for n in range(len(self.__becas)):
                if(becaslista[i] == self.__becas[n].getid()):
                    print(self.__becas[n].getnombre())
                    
        print("El beneficario tiene ", contbecas, "beca/s")
        
    def modulo4(self):
        tipodebeca = input("Ingrese tipo de beca punto 4 > ")
        i = 0
        band = False
        idbeca = 0
        while i < len(self.__becas) and band == False:
            if (self.__becas[i].getnombre()== tipodebeca):
                idbeca = self.__becas[i].getid()
                return idbeca
            else:
                i += 1
        
    def calculartotal(self, cantidad, becaid):
        total = cantidad * self.__becas[becaid].gettotal()
        print("El total a pagar es", total)
        
    def retornalista(self):
        return self.__becas