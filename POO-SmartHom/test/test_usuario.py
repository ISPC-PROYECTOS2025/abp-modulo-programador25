from usuario import Usuario
from dispositivo import Dispositivo

def test_registrar_y_obtener_dispositivo():
    u = Usuario(1, "Juan")
    d = Dispositivo(1, "Luz", "Iluminación")
    u.registrar_dispositivo(d)

    assert u.obtener_dispositivo("Luz") == d

def test_eliminar_dispositivo():
    u = Usuario(1, "Juan")
    d1 = Dispositivo(1, "Luz", "Iluminación")
    d2 = Dispositivo(2, "Cafetera", "Electrodoméstico")
    u.registrar_dispositivo(d1)
    u.registrar_dispositivo(d2)

    u.eliminar_dispositivo("Luz")
    assert u.obtener_dispositivo("Luz") is None
    assert u.obtener_dispositivo("Cafetera") == d2
