import Plataforma
import Usuario
import Peliculas
import Series
import Contenido

#ASKLÑDJASLÑD
#comentario2

#comentario3
    #METODOS 
def crear_usuario(usuario):
    plataforma_general.lista_usuarios.append(usuario)
    

def iniciarApp(self):
    print ("\n>>Bienvenidos a La Platafora de streaming<<\n")
    on=True
    while on==True:
        if self.validarUsuario():    
            on=self.mainMenu()



def validarUsuario():
    print("Bienvenido a la Plataforma de Streaming")
    def menu_interno():
        print("\n1-Crear Usuario")
        print("2-Iniciar Sesion\n")

    condicion=True
    while condicion:

        menu_interno()

        opcion = int(input())

        if opcion == 1:

            print ("Ingrese usuario")
            usuario = str(input())

            print ("Ingrese Contraseña")
            contrasena = str(input())

            print ("Ingrese Edad")
            edad = str(input())

            usuario_creado = Usuario.Usuario(usuario, contrasena, edad)
            crear_usuario(usuario_creado)

        elif opcion == 2:
           
           break
            
        else:

            print ("Opción invalida.")


#COLOCANDO UN CAMBIO

def menu_principal(validacion):
    #MOSTRAMOS UN MENU CON TODAS LAS OPCIONES DE BUSQUEDA
    print("Sesion Iniciada!\n---------------\n")

    def mostrar_opciones():

        print("\nMenú Principal")
        print("Seleccione Opciones:\n")
        print("1-Menu Admin")
        print("2-Buscar Peliculas")
        print("3-Buscar Series")
        print("4-Buscar Series")
        print("5-Buscar Series")
        print("6-Salir\n")
    
    
    condicion=True
    while condicion:
        mostrar_opciones()
        seleccion = int(input())

        if seleccion == 1:

            menuAdmin()

        elif seleccion == 2:
            
            pelispref()

        elif seleccion == 3:

            pelispref()

        elif seleccion == 4:

            pelispref()

        elif seleccion == 5:

            pelispref()

        elif seleccion == 6:
           
           break

        else:

            print ("Opción invalida.")

    

def menuAdmin():
    #MOSTRAMOS UN MENU CON TODAS LAS OPCIONES DE BUSQUEDA
        
    def mostrar_opciones_admin():

        print("\nMenú Admin")
        print("Seleccione Opciones:\n")
        print("1-Cargar Peliculas")
        print("2-Eliminar Peliculas")
        print("3-Buscar Series")
        print("4-Buscar Series")
        print("5-Buscar Series")
        print("6-Volver al Menu Principal\n")

    condicion=True
    while condicion:

        mostrar_opciones_admin()

        seleccion = int(input())

        if seleccion == 1:

            menuAdmin()

        elif seleccion == 2:
            
            pelispref()

        elif seleccion == 3:

            pelispref()

        elif seleccion == 4:

            pelispref()

        elif seleccion == 5:

            pelispref()

        elif seleccion == 6:
           
           break

        else:

            print ("Opción invalida.")

def pelispref(self,contenido):

    preferencia=str(input("\nIngrese Genero preferido:\n"))
    lista=contenido.busqueda_recursiva(preferencia)
    print("Estas son las peliculas con tus preferencias!\n")
    print("Seleccione Opcion para Visualizar:\n")

    for peliculas in lista:
        print ("\nOpcion:",peliculas,"\n")


plataforma_general=Plataforma.Plataforma("Disney Plus")

validacion=validarUsuario()
menu_principal(validacion)