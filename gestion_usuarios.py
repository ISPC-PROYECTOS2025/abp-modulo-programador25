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