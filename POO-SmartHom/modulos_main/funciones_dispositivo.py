from dominio.dispositivo import Dispositivo
from dao.dispositivo_dao import DispositivoDAO

def crud_dispositivos():
    while True:
        print("\n--- CRUD Dispositivos ---")
        print("1. Listar dispositivos")
        print("2. Registrar dispositivo")
        print("3. Actualizar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_dispositivos_todos()
        elif opcion == "2":
            registrar_dispositivo()
        elif opcion == "3":
            actualizar_dispositivo()
        elif opcion == "4":
            eliminar_dispositivo()
        elif opcion == "5":
            break
        else:
            print("Opción incorrecta.")


def listar_dispositivos_todos():
    dispositivos = DispositivoDAO.listar_todos()
    for d in dispositivos:
        print(f"- {d.id_dispositivo} | {d.nombre} | {d.tipo} | {d.fecha_registro} | Usuario: {d.id_usuarios}")


def listar_dispositivos_usuario(id_usuario):
    dispositivos = DispositivoDAO.listar_por_usuario(id_usuario)
    for d in dispositivos:
        print(f"- {d.id_dispositivo} | {d.nombre} | {d.tipo} | {d.fecha_registro}")


def registrar_dispositivo():
    nombre = input("Nombre dispositivo: ")
    tipo = input("Tipo: ")
    estado = input("Estado (encendido/apagado): ")
    id_usuario = int(input("ID usuario asignado: "))

    dispositivo = Dispositivo(nombre=nombre, tipo=tipo, estado=estado, id_usuarios=id_usuario)
    DispositivoDAO.registrar(dispositivo)
    print("Dispositivo registrado.")


def actualizar_dispositivo():
    id_disp = int(input("Ingrese ID del dispositivo a actualizar: "))
    disp = DispositivoDAO.obtener_por_id(id_disp)
    if disp:
        disp.nombre = input(f"Nuevo nombre ({disp.nombre}): ") or disp.nombre
        disp.tipo = input(f"Nuevo tipo ({disp.tipo}): ") or disp.tipo
        disp.estado = input(f"Nuevo estado ({disp.estado}): ") or disp.estado
        DispositivoDAO.actualizar(disp)
        print("Dispositivo actualizado.")
    else:
        print("Dispositivo no encontrado.")


def eliminar_dispositivo():
    id_disp = int(input("Ingrese ID del dispositivo a eliminar: "))
    disp = DispositivoDAO.obtener_por_id(id_disp)
    if disp:
        confirmar = input(f"¿Seguro que desea eliminar {disp.nombre}? (s/n): ")
        if confirmar.lower() == "s":
            DispositivoDAO.eliminar(id_disp)
            print("Dispositivo eliminado.")
    else:
        print("Dispositivo no encontrado.")
