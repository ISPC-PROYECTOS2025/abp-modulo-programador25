from data import usuarios_registrados

def validar_usuario(usuario: str) -> bool:
    """
    Valida que el nombre de usuario contenga solo letras y números, y tenga al menos 5 caracteres.
    """
    if not usuario.isalnum():
        print("Error: El usuario solo puede contener letras y números.")
        return False
    if len(usuario) < 5:
        print("Error: El usuario debe tener al menos 5 caracteres.")
        return False
    return True

def validar_correo(correo_electronico: str) -> bool:
    """
    Valida que el correo electrónico contenga '@' y '.', y tenga al menos 5 caracteres.
    """
    if "@" not in correo_electronico or "." not in correo_electronico:
        print("Error: El correo debe contener '@' y un punto para el dominio.")
        return False
    if len(correo_electronico) < 5:
        print("Error: El correo electrónico debe tener al menos 5 caracteres.")
        return False
    return True

def validar_contraseña(contraseña: str) -> bool:
    """
    Valida que la contraseña tenga al menos 8 caracteres, una mayúscula y un carácter especial.
    """
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"

    if len(contraseña) < 8:
        print("Error: La contraseña debe tener al menos 8 caracteres.")
        return False
    if not any(c.isupper() for c in contraseña):
        print("Error: La contraseña debe contener al menos una letra mayúscula.")
        return False
    if not any(c in caracteres_especiales for c in contraseña):
        print("Error: La contraseña debe contener al menos un carácter especial.")
        return False
    return True

def registrar_usuario(usuario: str, correo_electronico: str, contraseña: str) -> bool:
    """
    Registra un nuevo usuario validando el nombre de usuario, correo electrónico y la fortaleza de la contraseña.
    """
    print(f"\n--- Intentando registrar usuario '{usuario}' ---")

    if not validar_usuario(usuario):
        return False
    if not validar_correo(correo_electronico):
        return False
    if not validar_contraseña(contraseña):
        return False

    print("¡Usuario registrado con éxito!")
    return True


def iniciar_registro():

    print("\n--- INICIO DEL REGISTRO DE USUARIO ---")
    print("Por favor, ingresa los siguientes datos:")

    while True:
        nombre_usuario = input("Nombre de usuario (solo letras/números, min 5 caracteres): ")
        if validar_usuario(nombre_usuario):
            break
        print("Inténtalo de nuevo.")

    while True:
        email = input("Correo electrónico: ")
        if validar_correo(email):
            break
        print("Inténtalo de nuevo.")

    while True:
        password = input("Contraseña (min 8 caracteres, 1 mayúscula, 1 carácter especial): ")
        if validar_contraseña(password):
            break
        print("Inténtalo de nuevo.")

    registrar_usuario(nombre_usuario, email, password)

if __name__ == "__main__":
    iniciar_registro()
    
def modificar_rol(email, lista_usuarios):
    for usuario in lista_usuarios:
        if usuario["email"] == email:
            print("Ingrese el nuevo rol:")
            print("1 - usuario")
            print("2 - admin")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                usuario["rol"] = "usuario"
            elif opcion == "2":
                usuario["rol"] = "admin"
            else:
                print("Opción inválida. No se modificó el rol.")
                return
            print("Se cambió correctamente el rol.")
            return
    print("No se encontró un usuario con ese email.")

def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    email = input("Correo electrónico: ").strip()
    contraseña = input("Contraseña: ").strip()

    for usuario in usuarios_registrados:
        if usuario["email"] == email and usuario["contraseña"] == contraseña:
            print(f"Bienvenido, {usuario['nombre']}!")
            return usuario

    print("Correo o contraseña incorrectos.")
    respuesta = input("¿Desea registrarse? (s/n): ").strip().lower()

    if respuesta == "s":
        print("\n--- REGISTRO DE NUEVO USUARIO ---")

        while True:
            nombre = input("Nombre de usuario (letras/números, min 5 caracteres): ").strip()
            if validar_usuario(nombre):
                break
            print("Nombre inválido. Intenta de nuevo.")

        while True:
            nuevo_email = input("Correo electrónico: ").strip()
            if validar_correo(nuevo_email):
                break
            print("Correo inválido. Intenta de nuevo.")

        while True:
            nueva_contraseña = input("Contraseña (min 8 caracteres, 1 mayúscula, 1 carácter especial): ").strip()
            if validar_contraseña(nueva_contraseña):
                break
            print("Contraseña inválida. Intenta de nuevo.")

        nuevo_usuario = {
            "nombre": nombre,
            "email": nuevo_email,
            "contraseña": nueva_contraseña,
            "rol": "usuario"
        }
        usuarios_registrados.append(nuevo_usuario)
        print("¡Usuario registrado con éxito!")
        return nuevo_usuario

    return None
