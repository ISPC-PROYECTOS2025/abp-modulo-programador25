from menu import menu_admin, menu_usuario_estandar, menu_gestion_dispositivos
from gestion_usuarios import iniciar_sesion, registrar_usuario, usuarios

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
                # Al volver de cerrar sesión, seguimos en el menú principal
            else:
                print("Usuario no encontrado o datos incorrectos.")
                respuesta = input("¿Desea registrarse? (s/n): ").strip().lower()
                if respuesta == "s":
                    usuario = registrar_usuario()
                    if usuario:
                        if usuario["rol"] == "admin":
                            menu_admin(usuario)
                        else:
                            menu_usuario_estandar(usuario)
                    # No se hace break, así vuelve al menú principal
                elif respuesta == "n":
                    print("Volviendo al menú principal...")
                else:
                    print("Opción inválida. Volviendo al menú principal...")

        elif opcion == "2":
            usuario = registrar_usuario()
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
