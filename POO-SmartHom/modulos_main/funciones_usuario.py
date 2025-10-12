from datetime import datetime
from dominio.usuario import Usuario
from dao.usuario_dao import UsuarioDAO
from dominio.subclases_usuario import Admin, Estandar
from util.validaciones import validar_email, validar_contrasena, validar_nombre, validar_opcion

# --- Registro ---
def registrar_usuario():
    print("\n--- Registro de nuevo usuario ---")
    
    while True:
        nombre = input("Nombre: ")
        if validar_nombre(nombre):
            break
        print("Nombre inválido.")

    while True:
        email = input("Email: ")
        if validar_email(email):
            break
        print("Email inválido.")

    while True:
        contrasena = input("Contraseña (mínimo 6 caracteres): ")
        if validar_contrasena(contrasena):
            break
        print("Contraseña inválida.")

    while True:
        print("Seleccione el rol del usuario:")
        print("1. Admin")
        print("2. Estándar")
        opcion_rol = input("Opción: ")
        if validar_opcion(opcion_rol, ["1", "2"]):
            rol = "admin" if opcion_rol == "1" else "estandar"
            break
        print("Opción incorrecta.")

    if rol == "admin":
        usuario = Admin(nombre=nombre, email=email, contrasena=contrasena)
    else:
        usuario = Estandar(nombre=nombre, email=email, contrasena=contrasena)

    UsuarioDAO.registrar(usuario)
    print(f"Usuario '{usuario.get_nombre()}' registrado con rol '{usuario.get_rol()}'.")


# --- Inicio de sesión ---
def iniciar_sesion():
    print("\n--- Inicio de sesión ---")

    while True:
        email = input("Email: ")
        if validar_email(email):
            break
        print("Email inválido.")

    while True:
        contrasena = input("Contraseña: ")
        if validar_contrasena(contrasena):
            break
        print("Contraseña inválida.")

    usuario = UsuarioDAO.obtener_por_email(email)

    if usuario and usuario.get_contrasena() == contrasena:
        print(f"\nBienvenido {usuario.get_nombre()}!")
     
        if usuario.get_rol() == "admin":
            admin = Admin(
                nombre=usuario.get_nombre(),
                email=usuario.get_email(),
                contrasena=usuario.get_contrasena(),
                fecha_registro=usuario.get_fecha_registro(),
                id=usuario.get_id()
            )
            admin.mostrar_menu()
        else:
            estandar = Estandar(
                nombre=usuario.get_nombre(),
                email=usuario.get_email(),
                contrasena=usuario.get_contrasena(),
                fecha_registro=usuario.get_fecha_registro(),
                id=usuario.get_id()
            )
            estandar.mostrar_menu()
    else:
        print("Credenciales incorrectas.")
