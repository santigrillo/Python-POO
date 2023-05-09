from class_manejadorEvaluacion import ManejadorEvaluaciones
from class_manejadorFederado import manejadorFederados


def menu():
    # Carga federados a lista
    federados = []
    manejadorFederados.carga(federados)
    
    # Carga evaluaciones al lista
    evaluaciones = []
    ManejadorEvaluaciones.carga(evaluaciones)

    # Modulo 1 = Leer un estilo y una edad y listar apellido, nombre, dni de cada participante.
    ManejadorEvaluaciones.option1(evaluaciones, federados)

    #Modulo 2 =  Mostrar apellido y nombre del patinador, estilo y club al que representa del patinador con mayor puntaje (promedio)
    manejadorFederados.option2(evaluaciones, federados)
    
    
if __name__ == "__main__":
    menu()