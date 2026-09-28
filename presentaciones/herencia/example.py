# 1. ¿Cómo indicamos que Perro hereda de Animal?
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro( Animal ):
    def __init__(self, nombre, raza):
        # 2. ¿Cómo llamamos al constructor del Padre?
        super().__init__(nombre)
        self.raza = raza

    # 3. Sobrescribir el método hablar
    def hablar(self):
        return "¡Guau, guau!"