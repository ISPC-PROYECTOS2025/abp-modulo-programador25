from abc import ABC, abstractmethod
from dominio.usuario import Usuario

class IUsuarioDAO(ABC):

    @abstractmethod
    def registrar(self, usuario: Usuario):
        pass

    @abstractmethod
    def obtener_por_email(self, email: str):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def actualizar(self, usuario: Usuario):
        pass

    @abstractmethod
    def eliminar(self, email: str):
        pass
