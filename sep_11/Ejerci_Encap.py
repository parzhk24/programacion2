
# Construye una clase UsuarioApp que contenga un atributo correo_inical
class UsuarioApp:
    def __init__(self, correo):
    # Guarda en self.correo el valor de correo_inicial (atributo debe ser privado)
        self.__correo = correo

    # 1. El GETTER (Lleva @property y el nombre que quieres usar)
    @property
    def correo(self):
        return self.__correo

    # 2. El SETTER (Lleva @nombre.setter y recibe el nuevo valor)
    @correo.setter
    def correo(self, nuevo_correo):
        self.__correo = nuevo_correo


# === Test descomenta ===
usuario = UsuarioApp("juan@mail.com")

print(usuario.correo)         # Llama al getter (muestra: juan@mail.com)

usuario.correo = "pedro@mail.com"  # Llama al setter (cambia el valor)
print(usuario.correo)         # Llama al getter (muestra: pedro@mail.com)
