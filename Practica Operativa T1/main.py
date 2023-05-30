from manejador import manejador

def test():
    m = manejador()
    m.cargaFederados()
    m.cargaEvaluaciones()
    
    m.modulo1()
    m.modulo2()
    m.modulo3()
    m.modulo4()
if __name__ == "__main__":
    test()