
class Persona:
    def __init__(self, nombre, edad, **kwargs):
        print("→ Entrando a Persona")
        super().__init__(**kwargs)
        self.nombre = nombre
        self.edad = edad
        print("← Saliendo de Persona")

class Estudiante(Persona):
    def __init__(self, universidad, semestre, **kwargs):
        print("→ Entrando a Estudiante")
        super().__init__(**kwargs)
        self.universidad = universidad
        self.semestre = semestre
        print("← Saliendo de Estudiante")

class Trabajador(Persona):
    def __init__(self, empresa, salario, **kwargs):
        print("→ Entrando a Trabajador")
        super().__init__(**kwargs)
        self.empresa = empresa
        self.salario = salario
        print("← Saliendo de Trabajador")

class Pasante(Estudiante, Trabajador):
    def __init__(self, nombre, edad, universidad, semestre, empresa, salario, horas_semana):
        print("→ Entrando a Pasante")
        self.horas_semana = horas_semana
        super().__init__(
            nombre=nombre,
            edad=edad,
            universidad=universidad,
            semestre=semestre,
            empresa=empresa,
            salario=salario
        )
        print("← Saliendo de Pasante")

# Creamos el objeto
ana = Pasante(
    nombre="Ana",
    edad=21,
    universidad="UNAM",
    semestre=6,
    empresa="Google",
    salario=15000,
    horas_semana=20
)
