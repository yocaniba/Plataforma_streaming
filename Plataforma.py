#creamos clases en este caso creamos Clase Plataforma,
#Usuario,Contenido seguido de serie y pelicula.

class Plataforma:
    def __init__(self,nombre):
        #Instaciamos una lista contenido para poder manejar
        #la informacion. Tambien agregamos una lista de usuarios para
        #crear un login. Por el momento tenemos una lista de peliculas mas populares
        #por vistas
        self.nombre= nombre
        self.contenido=[]
        self.lista_usuarios=[]#lista de listas (datos del usuario)
        self.maspopulares=[]