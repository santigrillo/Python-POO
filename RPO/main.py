from manejadorBecas import manejadorBeca
from manejadorBeneficiarios import manejadorBeneficiarios

def test():
    
    mB = manejadorBeca()
    mB.carga()
    
    mBs = manejadorBeneficiarios()
    mBs.carga()    
    
    # idbeca = mB.modulo1()
    # print(idbeca)
    # mBs.muestramd1(idbeca)
    
    # becaslista = []
    # mBs.modulo2(becaslista)
    # mB.modulo2muestra(becaslista)
    
    print("\n Lista ordenada")
    mBs.ordenaxpromedio() #Modulo3
    
    idbecamd = mB.modulo4()
    mBs.modulo42(idbecamd)
    
if __name__ =="__main__":
    test()