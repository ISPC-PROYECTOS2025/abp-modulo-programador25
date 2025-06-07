from data import dispositivos

def listar_dispositivos():
    if not dispositivos:
        print("No hay dispositivos registrados.")
    else:
        print("\nDispositivos registrados:")
        for d in dispositivos:
            print(f"- {d['nombre']} ({d['tipo']}) - Estado: {d['estado']}")

def agregar_dispositivo(nombre, tipo):
    dispositivo = {
        "nombre": nombre,
        "tipo": tipo,
        "estado": "apagado"
    }
    dispositivos.append(dispositivo)
    print(f"Dispositivo '{nombre}' ha sido agregado correctamente.")

def eliminar_dispositivo(nombre):
    for d in dispositivos:
        if d["nombre"].lower() == nombre.lower():
            dispositivos.remove(d)
            print(f"El dispositivo '{nombre}' ha sido eliminado correctamente.")
            return
    print("Dispositivo no encontrado.")

def ver_estado():
    if not dispositivos:
        print("No hay dispositivos para mostrar.")
        return
    print("\nEstado de los dispositivos:")
    for d in dispositivos:
        print(f"- {d['nombre']} ({d['tipo']}): {d['estado']}")

