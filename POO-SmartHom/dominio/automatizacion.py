from dispositivo import Dispositivo
from usuario import Usuario

class Automatizacion:
    def __init__(self, id: int, nombre: str, dispositivos: list[Dispositivo], hora_activacion: str):
        self.id = id
        self.nombre = nombre
        self.dispositivos = dispositivos
        self.hora_activacion = hora_activacion

    def activar(self):
        for d in self.dispositivos:
            d.encender()

    def validar_dispositivos_registrados(self, usuario: Usuario) -> bool:
        nombres_usuario = [d.nombre for d in usuario.dispositivos]
        return all(d.nombre in nombres_usuario for d in self.dispositivos)

    def __str__(self):
        return f"Automatización(id={self.id}, nombre={self.nombre}, hora={self.hora_activacion})"