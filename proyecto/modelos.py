class Libro:

    def __init__(self, titulo, autor, fechapubli, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.fechapubli = fechapubli
        # Atributo privado
        self.__ejemplares = ejemplares

    # Getter para atributo privado
    def get_ejemplares(self):
        return self.__ejemplares

    def imprimir_titulo_y_autor(self):
        return f'El libro elegido es {self.titulo} y fue escrito por {self.autor}'

    def imprimir_fecha_y_ejemplares(self):
        return f'El libro elegido fue publicado en {self.fechapubli} y cuenta con {self.get_ejemplares()} ejemplares.'

#Creacion de subclase
class Comic(Libro):
    def __init__(self, titulo, autor, fechapubli, ejemplares, franquicia, universo, generacion):
        super().__init__(titulo, autor, fechapubli, ejemplares)
        self.franquicia = franquicia
        self.universo = universo
        self.generacion = generacion
        
    # Metodo propio
    def info_comic(self):
        return f'Este comic pertenece a la franquicia {self.franquicia} al universo {self.universo} y a la {self.generacion} generacion'
    
    # Polimorfismo
    def imprimir_titulo_y_autor(self):
        return f'El comic elegido es {self.titulo} y fue escrito por {self.autor}'

class Bilioteca:
    def __init__(self, libro, comic):
        self.libro = libro
        self.comic = comic

    def info_libro(self):
        return f"""
{self.libro.imprimir_titulo_y_autor()}
{self.libro.imprimir_fecha_y_ejemplares()}
{self.libro.imprimir_titulo_y_autor()}
"""  
    
    def info_comic(self):
        return f"""
{self.comic.imprimir_titulo_y_autor()}
{self.comic.info_comic()}
"""  