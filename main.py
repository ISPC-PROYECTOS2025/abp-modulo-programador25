from gestion_dispositivos import listar_dispositivos, agregar_dispositivo, eliminar_dispositivo, ver_estado
from automatizacion import modo_despertar
from data import lista_de_dispositivos

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Listar dispositivos")
        print("2. Agregar dispositivo")
        print("3. Eliminar dispositivo")
        print("4. Ver estado de dispositivos")
        print("5. Activar Modo Despertar")
        print("6. Salir")

        seleccion_menu = input("Seleccioná una opción: ")

        if seleccion_menu == "1":
            listar_dispositivos()

        elif seleccion_menu  == "2":
            nombre_dispositivo = input("Nombre del dispositivo: ")

            print("Elija el tipo de dispositivo:")
            print("1. Luz")
            print("2. Tv")
            print("3. Música")
            print("4. Otro")
            opcion_tipo = input("Opción: ")
            tipo_dispositivo = "otro"  

            if  opcion_tipo == "1":
                tipo_dispositivo  = "luz"
            elif  opcion_tipo == "2":
                tipo_dispositivo = "tv"
            elif opcion_tipo == "3":
                tipo_dispositivo  = "música"
            elif  opcion_tipo == "4":
                tipo_dispositivo  = input("Ingrese el tipo de dispositivo personalizado: ")

            agregar_dispositivo(nombre_dispositivo, tipo_dispositivo )

        elif seleccion_menu == "3":
            if not lista_de_dispositivos:
                print("No hay dispositivos registrados para eliminar.")
            else:
                print("\nDispositivos registrados:")
                for i, dispositivo in enumerate(lista_de_dispositivos, start=1):
                    print(f"{i}. {dispositivo['nombre']} ({dispositivo['tipo']})")

                try:
                    seleccion_eliminar = int(input("Ingrese el número del dispositivo a eliminar: "))
                    if 1 <= seleccion_eliminar <= len(lista_de_dispositivos):
                        nombre_dispositivo = lista_de_dispositivos[seleccion_eliminar - 1]['nombre']
                        eliminar_dispositivo (nombre_dispositivo)
                    else:
                        print("El número ingresado no es correcto.")
                except ValueError:
                    print("Ingreso inválido. Por favor, ingrese un número.")

        elif seleccion_menu  == "4":
            ver_estado()

        elif seleccion_menu  == "5":
            hora_modo_despertar = input("Ingrese el horario para modo despertar(HH:MM): ")
            modo_despertar(hora_modo_despertar)
        elif seleccion_menu  == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intentá de nuevo.")


menu()

