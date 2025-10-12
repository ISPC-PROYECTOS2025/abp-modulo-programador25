class Dispositivo:
    def __init__(self, id: int, nombre: str, tipo: str):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.estado = False  # apagado por defecto

    def encender(self):
        self.estado = True

    def apagar(self):
        self.estado = False

    def __str__(self):
        estado_str = "Encendido" if self.estado else "Apagado"
        return f"Dispositivo(id={self.id}, nombre={self.nombre}, tipo={self.tipo}, estado={estado_str})"
