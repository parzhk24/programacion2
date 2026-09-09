# ============================================================
# ACTIVIDAD EXPRÉS: Construyendo la clase CuentaCorreo
# Escribe la línea de código correspondiente debajo de cada # TODO
# ============================================================

# TODO 1: Declara la clase llamada CuentaCorreo
class CuentaCorreo:

    # TODO 2: Define el constructor __init__
    # Debe recibir: self, usuario y password
    def __init__(self, usuario, password):

        # TODO 3: Guarda 'usuario' en el atributo permanente del objeto usando self
        self.usuario = usuario
        # TODO 4: Guarda 'password' en el atributo permanente del objeto usando self
        self.password = password


    # TODO 5: Define el método 'mostrar_info' (recibe únicamente self)
    def mostrar_info(self):

        # TODO 6: Imprime en pantalla usando un f-string:
        # "Cuenta: [usuario] | Password: [password]"
        print(f'Cuenta: {self.usuario} | Password: {self.password}')

# ============================================================
# PRUEBA TU CÓDIGO
# ============================================================

# TODO 7: Crea un objeto llamado 'mi_cuenta' pasando tu usuario y una contraseña de prueba
# Ejemplo: "erica@gmail.com", "1234"
mi_cuenta = CuentaCorreo('sam@gmail.com', '1234')

# TODO 8: Llama al método 'mostrar_info' de tu objeto 'mi_cuenta'
mi_cuenta.mostrar_info()