import Contenido

class Usuario:
    def __init__(self,nombre,contrasena,edad):
        self.nombre=nombre
        self.contrasena=contrasena
        self.edad=edad
        #self.preferencias=preferencias #pedimos preferencias al crear usuario
        #iniciamos una lista vacia para lo que va visualizando
        #para manejar lo que se le recomendaria
        self.hvisualizacion=[]
        self.preferencias=[]

    def agregar_usuario(self,usuario):
        pass

