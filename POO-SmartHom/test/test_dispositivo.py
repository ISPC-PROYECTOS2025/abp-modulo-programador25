import pytest
from src.dispositivo import Dispositivo

def test_encender_apagar():
    d = Dispositivo(1, "Luz", "Iluminación")
    assert d.estado is False

    d.encender()
    assert d.estado is True

    d.apagar()
    assert d.estado is False

def test_str_representation():
    d = Dispositivo(2, "Cafetera", "Electrodoméstico")
    assert "Cafetera" in str(d)
    assert "Apagado" in str(d)
