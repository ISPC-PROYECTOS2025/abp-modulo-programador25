from src.dispositivo import Dispositivo

class Usuario:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.dispositivos: list[Dispositivo] = []

    def registrar_dispositivo(self, dispositivo: Dispositivo):
        self.dispositivos.append(dispositivo)

    def eliminar_dispositivo(self, nombre: str):
        self.dispositivos = [d for d in self.dispositivos if d.nombre != nombre]

    def obtener_dispositivo(self, nombre: str):
        for d in self.dispositivos:
            if d.nombre == nombre:
                return d
        return None
