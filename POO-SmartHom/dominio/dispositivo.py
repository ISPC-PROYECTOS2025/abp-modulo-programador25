from datetime import datetime

class Dispositivo:
    def __init__(self, id: int = None, nombre: str = "", tipo: str = "", estado: str = "apagado", id_usuario: int = None, fecha_registro=None):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__estado = estado
        self.__id_usuario = id_usuario
        self.__fecha_registro = fecha_registro or datetime.now()

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        if estado in ["encendido", "apagado"]:
            self.__estado = estado
        else:
            print("Estado inválido. Solo puede ser 'encendido' o 'apagado'.")

    def get_id_usuario(self):
        return self.__id_usuario

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def get_fecha_registro(self):
        return self.__fecha_registro

    def encender(self):
        self.__estado = "encendido"

    def apagar(self):
        self.__estado = "apagado"

    def __str__(self):
        return f"Dispositivo(id={self.__id}, nombre={self.__nombre}, tipo={self.__tipo}, estado={self.__estado}, usuario={self.__id_usuario}, fecha={self.__fecha_registro})"
