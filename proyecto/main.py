
class Libro:

    def __init__(self, titulo, autor, fechapubli, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.fechapubli = fechapubli
        self.ejemplares = ejemplares

    def imprimir_titulo_y_autor(self):
        print(f'El libro elegido es {self.titulo} y fue escrito por {self.autor}')

    def imprimir_fecha_y_ejemplares(self):
        print(f'El libro elegido fue publicado en {self.fechapubli} y cuenta con {self.ejemplares} ejemplares.')

    def modificar_libro(self, ntitulo, nautor, nfecha, nejemplar):
        print(f'El titulo anterior del libro era {self.titulo}. Ahora es {ntitulo}')
        self.titulo = ntitulo
        print(f'El autor anterior del libro era {self.autor}. Ahora es {nautor}')
        self.autor = ntitulo
        print(f'La fecha de publicacion anterior del libro era {self.fechapubli}. Ahora es {nfecha}')
        self.fechapubli = nfecha
        print(f'El numero de ejemplares anterior del libro era {self.ejemplares}. Ahora es {nejemplar}')
        self.ejemplares = nejemplar

el_principito = Libro(
    'El principito',
    'Antoine',
    '1917',
    5
)
isla_misteriosa = Libro(
    'La isla misteriosa',
    'Julio Verne',
    '1887',
    3
)
ready_player = Libro(
    'Ready Player One',
    'Ernest Cline',
    '2010',
    4
)

el_principito.imprimir_titulo_y_autor()
isla_misteriosa.imprimir_fecha_y_ejemplares()

ntitulo = input('Nuevo titulo a asignar: ')
nautor = input('Nuevo autor a asignar: ')
nfecha = input('Nueva fecha de publicacion a asignar: ')
nejemplar = int(input('Nuevo numero de ejemplares a asignar: '))
ready_player.modificar_libro(ntitulo, nautor, nfecha, nejemplar)
