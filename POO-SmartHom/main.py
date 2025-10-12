from modulos_main.funciones_usuario import registrar_usuario, iniciar_sesion
from dao.usuario_dao import UsuarioDAO
from dao.dispositivo_dao import DispositivoDAO

# Instancias de DAO
usuario_dao = UsuarioDAO()
dispositivo_dao = DispositivoDAO()

def menu_principal():
    while True:
        print("\n=== SmartHome ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        print("4. Consultas bd")  # NUEVO: opción para probar consultas multitabla/subconsulta
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()  # Tu menú interno según rol
        elif opcion == "3":
            print("Saliendo...")
            break
        elif opcion == "4":
            # -------- Consultas multitabla y subconsultas --------
            print("\n--- Dispositivos con usuario ---")
            for d in dispositivo_dao.obtener_dispositivos_con_usuario():
                print(f"{d['dispositivo']} ({d['tipo']}) - Usuario: {d['nombre_usuario']}")

            print("\n--- Usuarios con más de un dispositivo ---")
            for u in usuario_dao.usuarios_con_mas_de_un_dispositivo():
                print(f"Usuario: {u['nombre_usuario']}")

        else:
            print("Opción incorrecta.")

if __name__ == "__main__":
    menu_principal()
