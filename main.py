from gestion_usuarios import iniciar_sesion, registrar_usuario_interactivo
from data import usuarios_registrados as usuarios
from menu import menu_admin, menu_usuario_estandar

def main():
    print("Bienvenido al sistema")
    while True:
        print("\n1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = iniciar_sesion()
            if usuario:
                if usuario["rol"] == "admin":
                    menu_admin(usuario)
                else:
                    menu_usuario_estandar(usuario)
            else:
                print("Usuario no encontrado o datos incorrectos.")

        elif opcion == "2":
            es_primer_usuario = len(usuarios) == 0
            rol = "admin" if es_primer_usuario else "usuario"
            usuario = registrar_usuario_interactivo(rol=rol)

            if usuario:
                if usuario["rol"] == "admin":
                    menu_admin(usuario)
                else:
                    menu_usuario_estandar(usuario)

        elif opcion == "3":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
