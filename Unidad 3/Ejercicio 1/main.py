from manejadorFacultad import manejadorFacultad as mf

def test():
    facultades = []
    mf.carga(facultades)
    mf.modulo1(facultades)  #Ingresar codigo de facultad y mostrar nombre y sus carreras.
    mf.modulo2(facultades)  #Ingresar nombre de carrera y mostrar codigo e informacion de la facultad donde se dicta.
    
if __name__ == "__main__":
    test()