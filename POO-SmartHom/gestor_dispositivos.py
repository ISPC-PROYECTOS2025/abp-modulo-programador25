from dispositivo import Dispositivo
from usuario import Usuario

class GestorDispositivos:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario

    def listar_dispositivos(self):
        return self.usuario.dispositivos

    def agregar_dispositivo(self, dispositivo: Dispositivo):
        self.usuario.registrar_dispositivo(dispositivo)

    def eliminar_dispositivo(self, nombre: str):
        self.usuario.eliminar_dispositivo(nombre)