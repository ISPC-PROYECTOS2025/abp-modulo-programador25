# test_registro.py

from gestion_usuarios import registrar_usuario_interactivo
from data import usuarios_registrados

print("Usuarios antes:", usuarios_registrados)

usuario = registrar_usuario_interactivo()

print("Usuario registrado:", usuario)
print("Usuarios después:", usuarios_registrados)
