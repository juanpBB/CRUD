class Producto:
    def __init__(self, nombre, titulo, autor):
        self.nombre=nombre
        self.titulo=titulo
        self.autor=autor #esto es para declarar que aparecera en la app, como las cosas que se tomaran informacion
    def paraConexiondb(self):
        return{
            'nombre':self.nombre,
            'titulo':self.titulo,
            'autor':self.autor
            #esto funciona para poder mandar la informacion de los datos recojidos de la pagina, a la base de datos
        }
        


