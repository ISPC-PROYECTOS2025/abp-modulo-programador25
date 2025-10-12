from dominio.dispositivo import Dispositivo
from dao.dispositivo_dao import DispositivoDAO

class GestorDispositivo:
    def __init__(self, id_usuario: int):
        self.__id_usuario = id_usuario
        self.__dispositivos = DispositivoDAO.listar_por_usuario(id_usuario)

    def agregar_dispositivo(self, nombre: str, tipo: str, estado: str):
        dispositivo = Dispositivo(
            nombre=nombre,
            tipo=tipo,
            estado=estado,
            id_usuario=self.__id_usuario
        )
        DispositivoDAO.registrar(dispositivo)
        self.__dispositivos = DispositivoDAO.listar_por_usuario(self.__id_usuario)
        print("Dispositivo agregado correctamente.")

    def eliminar_dispositivo(self, id_dispositivo: int):
        disp = self.obtener_dispositivo(id_dispositivo)
        if disp:
            DispositivoDAO.eliminar(id_dispositivo)
            self.__dispositivos = DispositivoDAO.listar_por_usuario(self.__id_usuario)
            print("Dispositivo eliminado correctamente.")
        else:
            print("Dispositivo no encontrado.")

    def actualizar_dispositivo(self, id_dispositivo: int, nuevo_nombre: str = None, nuevo_tipo: str = None, nuevo_estado: str = None):
        disp = self.obtener_dispositivo(id_dispositivo)
        if disp:
            if nuevo_nombre:
                disp.set_nombre(nuevo_nombre)
            if nuevo_tipo:
                disp.set_tipo(nuevo_tipo)
            if nuevo_estado:
                disp.set_estado(nuevo_estado)
            DispositivoDAO.actualizar(disp)
            self.__dispositivos = DispositivoDAO.listar_por_usuario(self.__id_usuario)
            print("Dispositivo actualizado correctamente.")
        else:
            print("Dispositivo no encontrado.")


    def listar_dispositivos(self):
        if not self.__dispositivos:
            print("No hay dispositivos cargados.")
        else:
            print("\n--- Mis dispositivos ---")
            for d in self.__dispositivos:
                print(f"- {d.get_id()} | {d.get_nombre()} | {d.get_tipo()} | {d.get_estado()}")

    def obtener_dispositivo(self, id_dispositivo: int):
        for d in self.__dispositivos:
            if d.get_id() == id_dispositivo:
                return d
        return None
