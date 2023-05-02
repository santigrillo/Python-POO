from modulo_clase import email
import csv

if __name__ == '__main__':
     listaCorreos = []
     mail=email()
     nombre = input("Bienvenido, ingrese su nombre: ")
     xcorreo = input("Ingrese su correo: ")
     xpassword = input("Ingrese su contraseña: ")
     mail.createAccount(xcorreo, xpassword)
     
     print ("El correo se ha creado con exito")
         
     print ("Bienvenido ", nombre, " te enviaremos tus mensajes a la dirección ", mail)
     
     mail.changePassword()    
          
     with open('correos.csv', 'r') as file:
          file_reader = csv.reader(file, delimiter=';')
          cont = 0
          dominiox = input("Dominio a buscar > ")
          for i in file_reader:
               if (dominiox in i[0]):
                    cont += 1
          print("Hay ", cont, " correos con ese dominio")