# ============================================================
# ACTIVIDAD PRÁCTICA: La clase BandejaCorreo
# Completa únicamente los espacios marcados con # TODO
# ============================================================

# 1. DECLARACIÓN DE LA CLASE (El molde)
class BandejaCorreo:

    # 2. CONSTRUCTOR (Se ejecuta al crear la bandeja de entrada)
    # TODO: Define el constructor con los parámetros: self, usuario, capacidad_maxima
    def __init__(self, usuario, capacidad_maxima):
        # TODO: Guarda los datos recibidos en la libreta del objeto ('self')
        self.usuario = usuario
        self.capacidad_maxima = capacidad_maxima
        
        # Atributos de estado inicial
        self.correos_recibidos = 0  # Inicia sin correos


    # 3. MÉTODOS DE ACCIÓN

    # ACCIÓN 1: Recibir un nuevo correo
    def recibir_correo(self, remitente):
        # Validamos si todavía hay espacio en la bandeja
        if self.correos_recibidos < self.capacidad_maxima:
            # TODO: Suma 1 al contador de correos recibidos
            self.correos_recibidos += 1
            
            # TODO: Muestra un mensaje impreso usando un f-string
            # Ejemplo: "📧 [usuario] recibió un correo de [remitente]."
            print(f"📧 {self.usuario} recibió un correo de {remitente}.")
        else:
            print(f"⚠️ ¡Bandeja llena! No se pudo recibir el correo de {remitente}.")


    # ACCIÓN 2: Consultar cuántos correos hay guardados
    def ver_estado(self):
        # TODO: Muestra en pantalla el usuario, los correos recibidos y su capacidad máxima
        print(f"📥 Usuario: {self.usuario}")
        print(f"📊 Correos en bandeja: {self.correos_recibidos} / {self.capacidad_maxima}")


# ============================================================
# 4. PRUEBA DEL CÓDIGO (Instanciación)
# ============================================================

# TODO: Crea un objeto llamado 'mi_bandeja' con tu nombre y capacidad máxima de 2 correos
mi_bandeja = BandejaCorreo("Santi", 2)

# TODO: Prueba recibir 3 correos seguidos para ver si funciona el límite
mi_bandeja.recibir_correo("carlos@gmail.com")
mi_bandeja.recibir_correo("ana@gmail.com")
mi_bandeja.recibir_correo("promociones@uber.com")  # Este debería rebotar por bandeja llena

# TODO: Llama al método para ver el estado final de tu bandeja
mi_bandeja.ver_estado()