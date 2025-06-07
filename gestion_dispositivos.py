from data import lista_de_dispositivos
def listar_dispositivos():
    if not lista_de_dispositivos:
        print("No hay dispositivos registrados.")
    else:
        print("\nDispositivos registrados:")
        for dispositivo in lista_de_dispositivos:
            print(f"- {dispositivo['nombre']} ({dispositivo['tipo']}) - Estado: {dispositivo['estado']}")

def agregar_dispositivo(nombre, tipo):
    nuevo_dispositivo = {
        "nombre": nombre,
        "tipo": tipo,
        "estado": "apagado"
    }
    lista_de_dispositivos.append(nuevo_dispositivo)
    print(f"Dispositivo '{nombre}' ha sido agregado correctamente.")

def eliminar_dispositivo(nombre):
    for dispositivo in lista_de_dispositivos:
        if dispositivo["nombre"].lower() == nombre.lower():
            lista_de_dispositivos.remove(dispositivo)
            print(f"El dispositivo '{nombre}' ha sido eliminado correctamente.")
            return
    print("Dispositivo no encontrado.")

def ver_estado():
    if not lista_de_dispositivos:
        print("No hay dispositivos para mostrar.")
        return
    print("\nEstado de los dispositivos:")
    for dispositivo in lista_de_dispositivos:
        print(f"- {dispositivo['nombre']} ({dispositivo['tipo']}): {dispositivo['estado']}")

