from gestion_dispositivos import listar_dispositivos, agregar_dispositivo, eliminar_dispositivo, ver_estado
from automatizacion import modo_despertar
from data import lista_de_dispositivos, usuarios_registrados
from gestion_usuarios import usuarios, modificar_rol

def menu_usuario_estandar(usuario):
    while True:
        print(f"\n--- MENÚ USUARIO - {usuario['nombre']} ---")
        print("1. Consultar datos personales")
        print("2. Activar automatización predefinida")
        print("3. Consultar dispositivos")
        print("4. Cerrar sesión")

        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            print(f"Nombre: {usuario['nombre']}")
            print(f"Email: {usuario['email']}")
            print(f"Rol: {usuario['rol']}")
        elif opcion == "2":
            horario = input("Ingrese el horario para modo despertar (HH:MM): ")
            modo_despertar(horario)
            usuario["automatizacion_activa"] = True
        elif opcion == "3":
            listar_dispositivos()
        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")
