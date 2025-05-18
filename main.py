from gestion_dispositivos import listar_dispositivos, agregar_dispositivo, eliminar_dispositivo, ver_estado
from automatizacion import modo_despertar
from data import dispositivos


def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Listar dispositivos")
        print("2. Agregar dispositivo")
        print("3. Eliminar dispositivo")
        print("4. Ver estado de dispositivos")
        print("5. Activar Modo Despertar")
        print("6. Salir")

        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            listar_dispositivos(dispositivos)

        elif opcion == "2":
            nombre = input("Nombre del dispositivo: ")

            print("Elija el tipo de dispositivo:")
            print("1. Luz")
            print("2. Televisor")
            print("3. Música")
            print("4. Otro")

            opcion_tipo = input("Opción: ")

            if opcion_tipo == "1":
                tipo = "luz"
            elif opcion_tipo == "2":
                tipo = "tv"
            elif opcion_tipo == "3":
                tipo = "música"
            elif opcion_tipo == "4":
                tipo = input("Ingrese el tipo de dispositivo personalizado: ")
            else:
                print("Opción inválida. Se asignará tipo 'otro'.")
                tipo = "otro"

            agregar_dispositivo(dispositivos, nombre, tipo)

        elif opcion == "3":
            if not dispositivos:
                print("No hay dispositivos registrados para eliminar.")
            else:
                print("\nDispositivos registrados:")
                for i, dispositivo in enumerate(dispositivos, start=1):
                    print(f"{i}. {dispositivo['nombre']} ({dispositivo['tipo']})")

                try:
                    seleccion = int(input("Ingrese el número del dispositivo a eliminar: "))
                    if 1 <= seleccion <= len(dispositivos):
                        nombre = dispositivos[seleccion - 1]['nombre']
                        eliminar_dispositivo(dispositivos, nombre)
                    else:
                        print("El número ingresado no es correcto.")
                except ValueError:
                    print("Ingreso inválido. Por favor, ingrese un número.")

        elif opcion == "4":
            ver_estado(dispositivos)

        elif opcion == "5":
            horario = input("Ingrese el horario para modo despertar(HH:MM): ")
            print(f"El modo despertar será a las {horario}")
            modo_despertar(dispositivos, horario)

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intentá de nuevo.")


menu()
