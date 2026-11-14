
from modelos import Bilioteca, Libro, Comic

# Instanciacion de clase principal
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

# Instanciacion de subclase
af15 = Comic(
    'Amazing Fantasy No. 15',
    'Stan Lee',
    '1962',
    5,
    'Marvel',
    '616',
    'primera'
)

mi_biblio = Bilioteca(
    ready_player,
    af15
)

print(mi_biblio.info_libro())
print(mi_biblio.info_comic())
