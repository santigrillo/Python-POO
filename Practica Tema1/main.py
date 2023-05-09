from class_manejadorEvaluacion import ManejadorEvaluaciones
from class_manejadorFederado import manejadorFederados


def menu():
    # Carga federados a lista
    federados = []
    manejadorFederados.carga(federados)
    
    # Carga evaluaciones al lista
    evaluaciones = []
    ManejadorEvaluaciones.carga(evaluaciones)

    print("Menu")
    print("1 - Modulo 1 (Leer un estilo y una edad y listar apellido, nombre, dni de cada participante.)")
    print("2 - Modulo 2 (Mostrar apellido y nombre del patinador, estilo y club al que representa del patinador con mayor puntaje (promedio))")
    print("3 - Modulo 3 (Listar la información de los patinadores que hicieron estilo libre.)")
    print("4 - Modulo 4 (Dado un DNI y un estilo, mostrar las tres notas.)")
    print("0 - Salir")
    
    option = int(input("Ingrese opción > "))

    while option != 0:
        if option == 1:
            # Modulo 1 = Leer un estilo y una edad y listar apellido, nombre, dni de cada participante.
            ManejadorEvaluaciones.option1(evaluaciones, federados)
        elif option == 2:
            #Modulo 2 =  Mostrar apellido y nombre del patinador, estilo y club al que representa del patinador con mayor puntaje (promedio)
            manejadorFederados.option2(evaluaciones, federados)
        elif option == 3:
            #Modulo 3 = Listar la información de los patinadores que hicieron estilo libre.
            ManejadorEvaluaciones.option3(evaluaciones, federados)
        elif option == 4:
            #Modulo 4 = Dado un DNI y un estilo, mostrar las tres notas.
            ManejadorEvaluaciones.option4(evaluaciones)
        option = int(input("Ingrese opción > "))
    
    
if __name__ == "__main__":
    menu()