from class_helado import helado

class manejadorHelados:
    
    def ventaHelado(helados, sabores):
                i = 0
                grs = int(input("Ingrese cantidad de gramos que va a vender = "))
                cant = int(input("Cuantos sabores va a agregar? 1/4 = "))   
                print("Cantidad de sabores = ", cant)
                h = helado(grs)
                helados.append(h)     
                while i < cant:
                    for n in range(len(sabores)):
                        print(sabores[n].getSabor())  
                    xid = int(input("Ingrese id del sabor = "))
                    sb = sabores[xid-1]
                    sabores[xid-1].sumapedido()
                    helados[len(helados)-1].addSabor(sb)
                    i+=1
                print("\n = Ticket =")
                helados[len(helados)-1].getTicket()
                
    def muestraSaboresPorHelado(helados):
        for i in range(len(helados)):
            print("Helado ", i, " sabores = ")
            helados[i].getSabores()
                

