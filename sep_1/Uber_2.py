# ============================================
# ACTIVIDAD: Construyendo la clase VehiculoUber
# Completa los espacios marcados con # TODO
# ============================================

class VehiculoUber:
    
    # 1. CONSTRUCTOR (se ejecuta al crear cada objeto)
    def __init__(self, placas, conductor, modelo_auto, ubicacion_gps, calificacion):
        # TODO: Asigna cada parámetro a su atributo
        # Ejemplo: self.placas = placas
        self.placas = placas
        self.conductor = conductor
        self.modelo_auto = modelo_auto
        self.ubicacion_gps = ubicacion_gps
        self.calificacion = calificacion
        self.disponible = True          # Todos empiezan disponibles
        self.bloqueado = False          # Por seguridad

    # 2. MÉTODOS
    def actualizar_gps(self, nuevas_coordenadas):
        # TODO: Cambia la ubicación y muestra un mensaje
        self.ubicacion_gps = nuevas_coordenadas
        print(f"{self.conductor} ahora está en: {self.ubicacion_gps}")

    def aceptar_viaje(self):
        # TODO: Cambia disponible a False y muestra mensaje
        self.disponible = False
        print(f"{self.conductor} aceptó un viaje. Ya no está disponible.")

    def finalizar_viaje(self):
        # TODO: Cambia disponible a True y muestra mensaje
        self.disponible = True
        print(f"{self.conductor} finalizó un viaje. Ya está disponible nuevamente.")

    def bloquear_por_seguridad(self):
        # TODO: Pon bloqueado = True, disponible = False y muestra alerta
        self.bloqueado = True
        self.disponible = False
        print(f"{self.conductor} ha sido bloqueado. No estará disponible hasta nuevo aviso.")


# ============================================
# 3. CREACIÓN DE OBJETOS (Instanciación)
# ============================================

# TODO: Completa la creación de los 3 objetos
auto_juan = VehiculoUber(
    "JAL-9876",
    "Juan Pérez",
    "Chevrolet Aveo",
    "Av. Vallarta y Américas",
    4.9
)

auto_maria = VehiculoUber(
    # TODO: Completa los datos de María
    "JMX-4321", 
    "María Torres", 
    "Toyota Yaris", 
    "Centro de Tlaquepaque", 
    4.75
)

auto_alerta = VehiculoUber(
    # TODO: Completa los datos de Carlos (el reportado)
    "LMN-5555", 
    "Carlos R.", 
    "Nissan Sentra", 
    "Anillo Periférico Sur", 
    3.2
)


# ============================================
# 4. PRUEBAS (descomenta para probar)
# ============================================

auto_juan.actualizar_gps("Av. Vallarta 1500")
auto_juan.aceptar_viaje()
auto_alerta.bloquear_por_seguridad()

print("Estado de Juan:", auto_juan.disponible)
print("Estado de María:", auto_maria.disponible)
print("¿Está bloqueado Carlos?", auto_alerta.bloqueado)