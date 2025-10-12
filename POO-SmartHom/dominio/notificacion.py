# dominio/notificacion.py

from datetime import datetime

class Notificacion:
    def __init__(self, mensaje: str, usuario_id: int, leida: bool = False, id: int = None):
        self.__id = id
        self.__mensaje = mensaje
        self.__fecha = datetime.now()
        self.__leida = leida
        self.__usuario_id = usuario_id

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def mensaje(self):
        return self.__mensaje

    @property
    def fecha(self):
        return self.__fecha

    @property
    def leida(self):
        return self.__leida

    @property
    def usuario_id(self):
        return self.__usuario_id

    # Setters (solo donde tiene sentido)
    @leida.setter
    def leida(self, valor: bool):
        self.__leida = valor

    def marcar_como_leida(self):
        """Marca la notificación como leída"""
        self.__leida = True

    def __str__(self):
        estado = "Leída" if self.__leida else "No leída"
        return f"[{self.__fecha.strftime('%Y-%m-%d %H:%M:%S')}] {self.__mensaje} ({estado})"
