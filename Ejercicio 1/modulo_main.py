from modulo_clase import email
import csv

def crearcorreo (correo):
     cadena = correo.split("@")
     nuevoid = cadena[0]
     cadena2 = cadena[1].split(".")
     nuevodominio = "@" + cadena2[0]
     tipodominio = "." + cadena2[1]
     passwordnueva = input("Ingrese clave: ")
     correonuevo = email(nuevoid, nuevodominio, tipodominio, passwordnueva)
     return correonuevo

def cargacorreo(listacorreos, long):
    for i in range(long):
     correo = input("Ingrese su correo electronico -> ")
     c = crearcorreo(correo)
     listacorreos.append(c)
     
def contdominio():
     cont = 0
     correos = open('correos.csv', 'r')
     dominioSearch = input("Ingrese dominio a buscar: ")
     for fila in correos:
          if(dominioSearch in fila):
               cont += 1
     print("Hay ", cont, " correos con ese dominio")

if __name__ == '__main__':
    
     nombre = input("Bienvenido, ingrese su nombre: ")
     xid = input("Ingrese ID: ")
     xdominio = input("Ingrese Dominio (gmail, yahoo, etc.): ")
     xtipo = input("Ingrese tipo (.com, .uk, .es): ")
     xpassword = input("Ingrese su contraseña: ")
    
     santiago=email(xid, xdominio, xtipo, xpassword)
     print ("El correo se ha creado con exito")    
    
     print ("Bienvenido ", nombre, " te enviaremos tus mensajes a la dirección ", santiago.returncorreo())
     
     santiago.changePassword()
     
     contdominio()
          

     
     