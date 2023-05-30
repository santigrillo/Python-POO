from classBeneficiario import beneficiario

class manejadorBeneficiarios:
    
    __beneficiarios = []
    
    def __init__(self):
        self.__beneficiarios = []
        
    def carga(self):
        with open("RPO/beneficiarios.csv", 'r') as fileB:
            next (fileB)
            for file in fileB:
                file = file.split(';')
                unBeneficiario = beneficiario(file[0], file[1], file[2], file[3], file[4], file[5], int(file[6]), file[7])
                self.__beneficiarios.append(unBeneficiario)
                
        print("Beneficiarios cargados.")
        
    def muestramd1(self, becaid):
        print("ID a buscar ", becaid)
        cont = 0
        for i in range(len(self.__beneficiarios)):      
            if int(self.__beneficiarios[i].getBeca()) == int(becaid):
                print("Info ", self.__beneficiarios[i].getInfo())
        
    
    def muestraBeneficiarios(self):
        for i in range(len(self.__beneficiarios)):
            print(self.__beneficiarios[i].getInfo())
            
    def modulo2(self, becaslista):
        xDNI = input("Ingrese DNI > ")
        i = 0
        while i < len(self.__beneficiarios):
            if (self.__beneficiarios[i].getDNI() == xDNI):
                print(self.__beneficiarios[i].infomd2())
                becaslista.append(self.__beneficiarios[i].getBeca())
                i += 1
            else:
                i += 1
        return becaslista
    
    def ordenaxpromedio(self):
        # self.__beneficiarios.sort(key=lambda i: i.getPromedio(), reverse=True)
        self.__beneficiarios.sort()
        for i in range(len(self.__beneficiarios)):
            print(self.__beneficiarios[i].getinfomd3())
        
    
    def modulo42(self, idbecamd4):
        print("Id beca = ", idbecamd4)
        for i in range(len(self.__beneficiarios)):
            if self.__beneficiarios[i].getPromedio() > 8:
                if int(self.__beneficiarios[i].getBeca()) != int(idbecamd4): 
                    print("Beca beneficiario = ", self.__beneficiarios[i].getBeca(), " e id beca a buscar = ", idbecamd4)
                    print(self.__beneficiarios[i].getinfomd4())
                    
        print("No poseen la beca.")
    
    def getbeneficiarios(self):
        return self.__beneficiarios