# ============================================================
# ACTIVIDAD 3: Construcción de la clase VehiculoUber
# Lee detenidamente cada comentario # y escribe el código abajo.
# ============================================================

# 1. DECLARACIÓN DE LA CLASE
# TODO: Define la clase llamada VehiculoUber
class VehiculoUber:

    # 2. CONSTRUCTOR (__init__)
    # TODO: Define el método constructor. 
    # Debe recibir: self, placas, conductor, modelo y saldo_conductor
    def __init__(self, placas, conductor, modelo, saldo_conductor):
        # TODO: Asigna cada parámetro recibido a su atributo usando 'self'
        
        self.placas = placas
        self.conductor = conductor
        self.modelo = modelo
        self.saldo_conductor = saldo_conductor

    # 3. MÉTODOS DE LA CLASE/Crea 3 métodos públicos (reciben self) que hagan lo siguiente:
    # TODO:1. Método 'iniciar_viaje' (recibe self y el nombre_pasajero)
    # Debe imprimir: "Iniciando viaje con [nombre_pasajero]..."
    def iniciar_viaje(self, nombre_pasajero):
        print(f'Iniciando viaje con {nombre_pasajero}')

    # TODO:2. Método 'completar_viaje' (recibe self y costo_final)
    # Debe:
    # 1. Sumar costo_final a self.saldo_conductor
    # 2. Imprimir un mensaje de viaje finalizado y el nuevo saldo del conductor
    def completar_viaje(self, costo_final):
        self.saldo_conductor = self.saldo_conductor + costo_final
        print(f'Viaje finalizado. Nuevo saldo neto de {self.saldo_conductor}')


    # TODO: 3.Método 'mostrar_resumen' (recibe self)
    # Debe imprimir el nombre del conductor, el modelo, las placas y su saldo actual 
    def mostrar_resumen(self):
        print(f'El conductor {self.conductor} cuenta con el carro modelo {self.modelo}, sus placas son {self.placas} y con un saldo de {self.saldo_conductor}')




# ============================================================
# 4. PRUEBA DE TU CÓDIGO (INSTANCIACIÓN Y USO)
# ============================================================

# TODO: Crea un objeto llamado 'uber_1' con tus propios datos de prueba
# (placas, conductor, modelo, saldo_inicial)
uber_1 = VehiculoUber(
    'LWYR-UP',
    'Saul Goodman',
    'Cadillac Deville',
    1000
)

# TODO: Llama al método 'iniciar_viaje' pasándole el nombre de un pasajero
uber_1.iniciar_viaje('Adrian')

# TODO: Llama al método 'completar_viaje' pasándole el monto cobrado (ej. 95.50)
uber_1.completar_viaje(100)

# TODO: Llama al método 'mostrar_resumen' para verificar sus datos finales
uber_1.mostrar_resumen()