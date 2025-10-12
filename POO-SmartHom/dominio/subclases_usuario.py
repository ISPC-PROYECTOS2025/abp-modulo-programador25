
from dominio.usuario import Usuario
from modulos_main import funciones_admin, funciones_usuario

class Admin(Usuario):
    def mostrar_menu(self):
        while True:
            opcion = self._seleccionar_opcion(
                "Elige una opción:",
                ["Gestionar usuarios", "Gestionar dispositivos", "Salir"]
            )
            if opcion == "1":
                self.crud_usuarios()
            elif opcion == "2":
                self.crud_dispositivos()
            else:
                break

    def _seleccionar_opcion(self, mensaje, opciones):
        print(f"\n{mensaje}")
        for i, texto in enumerate(opciones, start=1):
            print(f"{i}. {texto}")
        return input("Seleccione una opción: ")

    def crud_usuarios(self):
        while True:
            opcion = self._seleccionar_opcion(
                "CRUD Usuarios:",
                ["Listar usuarios", "Actualizar usuario", "Eliminar usuario", "Cambiar rol de usuario", "Volver"]
            )
            if opcion == "1":
                funciones_admin.listar_usuarios()
            elif opcion == "2":
                funciones_admin.actualizar_usuario()
            elif opcion == "3":
                funciones_admin.eliminar_usuario()
            elif opcion == "4":
                funciones_admin.cambiar_rol_usuario()
            else:
                break

    def crud_dispositivos(self):
        while True:
            opcion = self._seleccionar_opcion(
                "CRUD Dispositivos:",
                ["Listar dispositivos", "Registrar dispositivo", "Actualizar dispositivo", "Eliminar dispositivo", "Volver"]
            )
            if opcion == "1":
                funciones_admin.listar_dispositivos_todos()
            elif opcion == "2":
                funciones_admin.registrar_dispositivo()
            elif opcion == "3":
                funciones_admin.actualizar_dispositivo()
            elif opcion == "4":
                funciones_admin.eliminar_dispositivo()
            else:
                break


class Estandar(Usuario):
    def mostrar_menu(self):
        while True:
            opcion = self._seleccionar_opcion(
                "Elige una opción:",
                ["Ver mis datos personales", "Ver mis dispositivos", "Salir"]
            )
            if opcion == "1":
                funciones_usuario.ver_datos_personales(self)
            elif opcion == "2":
                from dominio.gestor_dispositivo import GestorDispositivo
                gestor = GestorDispositivo(self.get_id())
                gestor.listar_dispositivos()
            else:
                break

    def _seleccionar_opcion(self, mensaje, opciones):
        print(f"\n{mensaje}")
        for i, texto in enumerate(opciones, start=1):
            print(f"{i}. {texto}")
        return input("Seleccione una opción: ")
