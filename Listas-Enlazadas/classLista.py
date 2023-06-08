from classNodo import nodo

class lista:
    __head = None
    
    def addNodo(self, persona):
        newNodo = nodo(persona)
        
        if self.__head is None:
            self.__head = newNodo
        else:
            current_nodo = self.__head
            while current_nodo.next is not None:
                current_nodo = current_nodo.next
            current_nodo.next = newNodo
            
    def print_list(self):
        current_nodo = self.__head
        while current_nodo is not None:
            print(current_nodo.getDato().getNombre())
            current_nodo = current_nodo.next