from datetime import datetime

class Usuario:
    def __init__(self, nombre: str, email: str, contrasena: str, fecha_registro=None, rol="estandar", id: int = None):
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__contrasena = contrasena
        self.__fecha_registro = fecha_registro or datetime.now()
        self.__rol = rol
        self.__dispositivos = []

 
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_contrasena(self):
        return self.__contrasena

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    def get_rol(self):
        return self.__rol

    def set_rol(self, rol):
        if rol in ["admin", "estandar"]:
            self.__rol = rol
        else:
            print("Rol inválido. Solo puede ser 'admin' o 'estandar'.")

    def get_fecha_registro(self):
        return self.__fecha_registro

    def get_dispositivos(self):
        return self.__dispositivos


    def registrar_dispositivo(self, dispositivo):
        self.__dispositivos.append(dispositivo)

    def eliminar_dispositivo(self, nombre: str):
        self.__dispositivos = [d for d in self.__dispositivos if d.get_nombre() != nombre]

    def obtener_dispositivo(self, nombre: str):
        for d in self.__dispositivos:
            if d.get_nombre() == nombre:
                return d
        return None

    def menu(self):
        """Este método será sobrescrito por las subclases"""
        raise NotImplementedError("El método menu debe ser implementado por la subclase")

    def __str__(self):
        return f"Usuario(id={self.__id}, nombre={self.__nombre}, email={self.__email}, rol={self.__rol})"
