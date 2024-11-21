import Peliculas
import Series


class Contenido:
    #prodriamos instanciar contenido en Plataforma en un metodo
    def __init__(self):
        self.peliculas=[]
        self.series=[]

    def agregar_pelicula(self):
        nombre=str(input("Ingrese nombre de pelicula:")) 
        genero=str(input("Ingrese genero:")) 
        popularidad=int(input("Ingrese Popularidad:")) 
        duracion=int(input("Ingrese Duracion:")) 

        npelicula=Peliculas(nombre,genero,popularidad,duracion)
        self.peliculas.append(npelicula)

    def agregar_series(self):

        nombre=str(input("Ingrese nombre de Serie:"))
        genero=str(input("Ingrese genero:"))
        popularidad=int(input("Ingrese Popularidad:"))
        duracion=int(input("Ingrese Duracion:"))

        #episodios=(input("Ingrese nombre de Serie")) #LISTAS DE TEMP, CON CAPS [] 
        
        nserie=Serie(nombre,genero,popularidad,duracion) # type: ignore
        self.peliculas.append(nserie)

    def busqueda_recursiva(self,preferencias,lista=None):

        if lista is None:
            lista = self.peliculas

        if not lista:  
            return []
        #si no verificaba 2 veces la lista 
        #vacia me decia index error out of range de [0]
        if len(self.peliculas)==0:
            return []

        pelicula_actual = lista[0]
        if pelicula_actual.genero == preferencias:
            return [pelicula_actual.nombre] + self.busqueda_recursiva(preferencias, lista[1:])
        else:
            return self.busqueda_recursiva(preferencias, lista[1:])