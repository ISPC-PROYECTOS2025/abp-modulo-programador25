from usuario import Usuario
from dispositivo import Dispositivo
from gestor_dispositivos import GestorDispositivos

def test_agregar_y_listar():
    u = Usuario(1, "Juan")
    g = GestorDispositivos(u)
    d = Dispositivo(1, "Luz", "Iluminación")

    g.agregar_dispositivo(d)
    assert g.listar_dispositivos() == [d]

def test_eliminar():
    u = Usuario(1, "Juan")
    g = GestorDispositivos(u)
    d = Dispositivo(1, "Luz", "Iluminación")
    g.agregar_dispositivo(d)

    g.eliminar_dispositivo("Luz")
    assert g.listar_dispositivos() == []