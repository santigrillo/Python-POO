from objectEncoder import ObjectEncoder
from manejadorPersonas import manejador
from classPersona import persona

def menu():
    print("1 - Agregar persona.")
    print("2 - Subir a JSON.")
    print("3 - Leer JSON.")
    print("4 - Mostrar personas.")

def test():
    jsonF = ObjectEncoder()
    personas = manejador()

    menu()
    option = int(input("Ingrese opcion > "))
    
    while option != -1:
        if option == 1:
            nombre = input("Ingrese nombre > ")
            apellido = input("Ingrese apellido > ")
            unaPersona = persona(nombre, apellido)
            personas.addPersona(unaPersona)

        if option == 2:
            d = personas.toJSON()
            jsonF.guardarJSONArchivo(d)
            
        if option == 3:
            diccionario = jsonF.leerJSONArchivo()
            personas = jsonF.decodificarDiccionario(diccionario)
            
        if option == 4: 
            personas.mostrar()

        menu()
        option = int(input("Ingrese opcion > "))

if __name__ == "__main__":
    test()