
### Herencia Jerárquica

# 1. SUPERCLASE

class Persona:

    def __init__(self, nombre, edad, dni):

        self.nombre = nombre

        self.edad = edad

        self.dni = dni

    def presentarse(self):

        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

  
# 2. SUBCLASE TRABAJADOR (Hereda de Persona)

class Trabajador(Persona):

    def __init__(self, nombre, edad, dni, sueldo, cargo, empresa):

        super().__init__(nombre, edad, dni)

        self.sueldo = sueldo

        self.cargo = cargo

        self.empresa = empresa

    def calcular_sueldo_anual(self):

        return 12 * self.sueldo + 2000


# instance of Trabajador

trabajador = Trabajador("Juan", 35, "87654321B", 2000, "Ingeniero", "TechCorp")

trabajador.presentarse()

  

# 3. SUBCLASE ESTUDIANTE (Hereda de Persona)

class Estudiante(Persona):

    def __init__(self, nombre, edad, dni, universidad, curso, asignaturas):

        super().__init__(nombre, edad, dni)

        self.universidad = universidad

        self.curso = curso

        self.asignaturas = asignaturas

    def describirse(self):

        print(f"""Hola, soy {self.nombre}, tengo {self.edad} años y estudio en la {self.universidad}. Estoy en el curso {self.curso}.""")

 
# Instancia de Estudiante

estudiante = Estudiante(

    "María", 20,"87654321B","Universidad de Madrid",3,

    ["Programación", "Cálculo", "Álgebra"])

estudiante.describirse()


## Herencia múltiple

# ============================================================
# HERENCIA MÚLTIPLE EN PYTHON
# Conceptos clave: super() + **kwargs + MRO
# ============================================================

# SUPERCLASE 1

class Estudiante:

    def __init__(self, universidad, carrera, **kwargs):

        # **kwargs = "la bolsa" con los parámetros que esta clase NO necesita.

        # super() sigue el MRO y llama al SIGUIENTE constructor (Trabajador).

        # Le pasamos el resto de parámetros que todavía no se han usado.

        super().__init__(**kwargs)

        # Esta clase solo se queda con lo que le corresponde:

        self.universidad = universidad

        self.carrera = carrera

    def estudiar(self):

        print(f"Estudiando {self.carrera} en {self.universidad}.")

# ------------------------------------------------------------
# SUPERCLASE 2

class Trabajador:

    def __init__(self, empresa, puesto, **kwargs):

        # Vuelve a usar super() + **kwargs para continuar la cadena.

        # En este punto **kwargs ya casi está vacío (o vacío).

        # Al final la cadena llega a "object" y termina limpiamente.

        super().__init__(**kwargs)

        self.empresa = empresa

        self.puesto = puesto
        
    def trabajar(self):

        print(f"Trabajando como {self.puesto} en {self.empresa}.")

# ------------------------------------------------------------

# SUBCLASE CON HERENCIA MÚLTIPLE

# El orden (Estudiante, Trabajador) define el MRO:

#   1. EstudianteTrabajador

#   2. Estudiante

#   3. Trabajador

#   4. object

# ------------------------------------------------------------

class EstudianteTrabajador(Estudiante, Trabajador):

    def __init__(self, nombre, universidad, carrera, empresa, puesto):

        self.nombre = nombre

        # Aquí empieza la cadena cooperativa.

        # Se envían TODOS los parámetros. Cada clase tomará los suyos

        # y reenviará el resto con **kwargs.

        super().__init__(

            universidad=universidad,

            carrera=carrera,

            empresa=empresa,

            puesto=puesto )
            
    def presentarse(self):

        # Gracias a la herencia múltiple, podemos usar métodos

        # de ambas superclases sin problema.

        print(f"Hola, soy {self.nombre}.")

        self.estudiar()   # viene de Estudiante

        self.trabajar()   # viene de Trabajador
# ------------------------------------------------------------

# PRUEBA

persona = EstudianteTrabajador(

    nombre="Martín",

    universidad="UdeG",

    carrera="Ciberseguridad",

    empresa="Tech Solutions",

    puesto="Analista de Seguridad"

)
persona.presentarse()


# ------------------------------------------------------------

# VER EL MRO (Method Resolution Order)

# Muestra el orden exacto en el que Python busca métodos y constructores

# ------------------------------------------------------------

print("\n--- MRO de EstudianteTrabajador ---")

for i, cls in enumerate(EstudianteTrabajador.__mro__, 1):

    print(f"{i}. {cls.__name__}")


# Flujo real de la cadena:

# 1. EstudianteTrabajador llama a super()

# 2. Estudiante toma universidad y carrera → reenvía el resto

# 3. Trabajador toma empresa y puesto → reenvía el resto

# 4. object recibe la llamada final y la cadena termina
