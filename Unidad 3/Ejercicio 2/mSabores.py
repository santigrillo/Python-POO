from class_sabor import sabor

class manejadorSabores:
    def carga(sabores):
        with open("Unidad 3/Ejercicio 2/archivos/sabores.csv", 'r') as filehelados:
            next (filehelados)
            for file in filehelados:
                file = file.split(';')
                unSabor = sabor(file[0], file[1], file[2])
                sabores.append(unSabor)
    
    def muestraSabores(sabores):
        for i in range(len(sabores)):
            print(sabores[i].getNombre())
            
    def modulo2(sabores):
        sabores.sort(key=lambda i: i.getVecesPedido(), reverse = True) 
        for i in range(len(sabores)):
            print(sabores[i].getNombre(), "fue pedido ", sabores[i].getVecesPedido())