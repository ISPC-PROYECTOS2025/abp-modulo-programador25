from usuario import Usuario
from dispositivo import Dispositivo
from automatizacion import Automatizacion

def test_activar_automatizacion():
    d1 = Dispositivo(1, "Luz", "Iluminación")
    d2 = Dispositivo(2, "Cafetera", "Electrodoméstico")
    auto = Automatizacion(1, "Mañana", [d1, d2], "07:00")

    auto.activar()
    assert d1.estado is True
    assert d2.estado is True

def test_validar_dispositivos_registrados():
    u = Usuario(1, "Francisco")
    d1 = Dispositivo(1, "Luz", "Iluminación")
    d2 = Dispositivo(2, "Cafetera", "Electrodoméstico")
    u.registrar_dispositivo(d1)
    u.registrar_dispositivo(d2)

    auto = Automatizacion(1, "Mañana", [d1, d2], "07:00")
    assert auto.validar_dispositivos_registrados(u) is True

    d3 = Dispositivo(3, "Televisor", "Electrodoméstico")
    auto2 = Automatizacion(2, "Noche", [d3], "21:00")
    assert auto2.validar_dispositivos_registrados(u) is False