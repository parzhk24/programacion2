
class Mensaje:
    def __init__(self, remitente, asunto):
        self.remitente = remitente
        self.asunto = asunto

    def resumen(self):
        return f"De {self.remitente}: {self.asunto}"