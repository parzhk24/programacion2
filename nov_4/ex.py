
class Libro:

    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def data(self):
        return f"""
            {self.titulo}
            {self.autor}
            {self.genero}
        """
    
class Biblioteca:
    def __init__(self, direccion, libro: Libro):
        self.direccion = direccion
        self.libro = libro

    def info(self):
        print(f"""
            {self.direccion}
            {self.libro.data()}
        """)

mi_libro = Libro(
    "El Principito",
    "Antoine de Saint Exupery",
    "Fantasia"
)

mi_bilioteca = Biblioteca(
    "Pegado a CUCEA",
    libro = mi_libro
)

mi_bilioteca.info()