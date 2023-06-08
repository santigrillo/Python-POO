from classLista import lista
from classPersona import persona


def test():
    list = lista()
    unaPersona = persona("Juan")
    list.addNodo(unaPersona)
    unaPersona = persona("Mateo")
    list.addNodo(unaPersona)
    list.print_list()
    
if __name__ == "__main__":
    test()