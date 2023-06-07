from abc import ABC, abstractmethod

class collection(ABC):
    @abstractmethod
    def insertar_elemento(self, element, position):
        pass

    @abstractmethod
    def agregar_elemento(self, element):
        pass

    @abstractmethod
    def mostrar_elemento(self, posicion):
        pass

class manejadorCollection(collection):

    __elementos = []

    def __init__(self):
        self.__elementos = []

    def insertar_elemento(self, element, position):
        if (position < 0):
            raise ValueError("La posición dada es un numero negativo.")
        elif position > len(self.__elementos):
            raise ValueError("La posicion dada es mayor al rango de la lista.")
        self.__elementos.insert(position, element)

    def agregar_elemento(self, elemento):
        self.__elementos.append(elemento)

    def mostrar_elemento(self, posicion):
        if (posicion < 0) or (posicion > len(self.__elementos)):
            raise ValueError("La posición dada no es válida para mostrar el elemento")
        return self.__elementos[posicion]

def test():
    myCollection = manejadorCollection()
    elementoToPosition = int(input("Ingrese un elemento > "))
    positionToAddElement = int(input("Ingrese la posicion para agregar el elemento anterior > "))
    myCollection.insertar_elemento(elementoToPosition, positionToAddElement)
    elementoAppend = int(input("Ingrese un elemento que será agregado al final de la colección > "))
    myCollection.agregar_elemento(elementoAppend)
    positionToShowDates = int(input("Ingrese la posicion a buscar elementos > "))
    elemento = myCollection.mostrar_elemento(positionToShowDates)
    print(elemento)

if __name__ == "__main__":
    test()