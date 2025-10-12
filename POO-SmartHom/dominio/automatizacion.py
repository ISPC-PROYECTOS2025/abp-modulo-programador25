from dominio.dispositivo import Dispositivo
from dominio.usuario import Usuario

class Automatizacion:
    def __init__(self, id: int = None, nombre: str = "", dispositivos: list[Dispositivo] = None, hora_activacion: str = ""):
        self.__id = id
        self.__nombre = nombre
        self.__dispositivos = dispositivos if dispositivos else []
        self.__hora_activacion = hora_activacion

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_dispositivos(self):
        return self.__dispositivos

    def get_hora_activacion(self):
        return self.__hora_activacion


    def set_nombre(self, nombre: str):
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre
        else:
            print("Nombre inválido. Debe ser un texto no vacío.")

    def set_hora_activacion(self, hora: str):
        # podrías agregar validaciones de formato (ejemplo: HH:MM)
        if isinstance(hora, str):
            self.__hora_activacion = hora
        else:
            print("La hora de activación debe ser una cadena de texto.")

    def agregar_dispositivo(self, dispositivo: Dispositivo):
        if isinstance(dispositivo, Dispositivo):
            self.__dispositivos.append(dispositivo)
        else:
            print("Solo se pueden agregar objetos de tipo Dispositivo.")

    def eliminar_dispositivo(self, nombre: str):
        self.__dispositivos = [d for d in self.__dispositivos if d.get_nombre() != nombre]

    # === MÉTODOS FUNCIONALES ===
    def activar(self):
        for d in self.__dispositivos:
            d.encender()

    def validar_dispositivos_registrados(self, usuario: Usuario) -> bool:
        nombres_usuario = [d.get_nombre() for d in usuario.dispositivos]
        return all(d.get_nombre() in nombres_usuario for d in self.__dispositivos)

    def __str__(self):
        return f"Automatizacion(id={self.__id}, nombre={self.__nombre}, hora={self.__hora_activacion})"
