from abc import ABC, abstractmethod
from dominio.dispositivo import Dispositivo

class IDispositivoDAO(ABC):

    @abstractmethod
    def registrar(self, dispositivo: Dispositivo):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def listar_por_usuario(self, id_usuario: int):
        pass

    @abstractmethod
    def obtener_por_id(self, id_dispositivo: int):
        pass

    @abstractmethod
    def actualizar(self, dispositivo: Dispositivo):
        pass

    @abstractmethod
    def eliminar(self, id_dispositivo: int):
        pass
