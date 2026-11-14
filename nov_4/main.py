class Motor:
    def __init__(self, caballos_fuerza: int, tipo: str):
        self.caballos_fuerza = caballos_fuerza
        self.tipo = tipo

    def encender(self) -> str:
        return f"Motor {self.tipo} de {self.caballos_fuerza} HP rugiendo."


class Rueda:
    def __init__(self, tamano: int):
        self.tamano = tamano

    def rodar(self) -> str:
        return f"Ruedas de {self.tamano} pulgadas girando."


class Coche:
    def __init__(self, marca: str, modelo: str, motor: Motor, tamano_rueda: int):
        self.marca = marca
        self.modelo = modelo
        # Composición: Coche contiene un objeto Motor
        self.motor = motor
        # Composición: Coche crea sus propios objetos Rueda internamente
        self.ruedas = [Rueda(tamano_rueda) for _ in range(4)]

    def arrancar(self):
        print(f"Arrancando el {self.marca} {self.modelo}:")
        print(f"- {self.motor.encender()}")
        print(f"- {self.ruedas[0].rodar()}")


# --- Uso ---
mi_motor = Motor(caballos_fuerza=300, tipo="V6")
mi_coche = Coche(marca="Toyota", modelo="Camry", motor=mi_motor, tamano_rueda=18)

mi_coche.arrancar()