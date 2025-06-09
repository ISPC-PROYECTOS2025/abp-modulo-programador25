from data import usuarios_registrados as usuarios

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

def registrar_usuario(usuario: str, correo_electronico: str, contraseña: str):
    """
    Registra un nuevo usuario validando datos y agregándolo a la lista usuarios.
    Devuelve el dict del usuario registrado o None si falla.
    """
    print(f"\n--- Intentando registrar usuario '{usuario}' ---")

    if not validar_usuario(usuario):
        return None
    if not validar_correo(correo_electronico):
        return None
    if not validar_contraseña(contraseña):
        return None

    nuevo_usuario = {
        "nombre": usuario,
        "email": correo_electronico,
        "contraseña": contraseña,
        "rol": "usuario"  # por defecto usuario normal, o podrías parametrizarlo
    }
    usuarios.append(nuevo_usuario)
    print("¡Usuario registrado con éxito!")
    return nuevo_usuario

def registrar_usuario_interactivo(rol=None):
    print("\n--- REGISTRO DE NUEVO USUARIO ---")

    # Determinar rol según parámetro o si hay usuarios
    if rol is None:
        if len(usuarios) == 0:
            rol = "admin"
            print("¡Primera cuenta creada, se asignará rol de admin!")
        else:
            rol = "usuario"
    else:
        if rol == "admin":
            print("Se asignará rol de admin (por parámetro).")
        else:
            print("Se asignará rol de usuario (por parámetro).")

    # Validaciones como antes
    while True:
        nombre = input("Nombre de usuario (letras/números, min 5 caracteres): ").strip()
        if validar_usuario(nombre):
            break
        print("Nombre inválido. Intenta de nuevo.")

    while True:
        email = input("Correo electrónico: ").strip()
        if validar_correo(email):
            break
        print("Correo inválido. Intenta de nuevo.")

    while True:
        contraseña = input("Contraseña (min 8 caracteres, 1 mayúscula, 1 carácter especial): ").strip()
        if validar_contraseña(contraseña):
            break
        print("Contraseña inválida. Intenta de nuevo.")

    nuevo_usuario = {
        "nombre": nombre,
        "email": email,
        "contraseña": contraseña,
        "rol": rol
    }
    usuarios.append(nuevo_usuario)
    print(f"¡Usuario registrado con éxito con rol '{rol}'!")
    return nuevo_usuario
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

    for usuario in usuarios:
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
        usuarios.append(nuevo_usuario)
        print("¡Usuario registrado con éxito!")
        return nuevo_usuario

    return None