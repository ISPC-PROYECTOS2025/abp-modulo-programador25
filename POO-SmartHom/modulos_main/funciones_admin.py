from dao.usuario_dao import UsuarioDAO
from dao.dispositivo_dao import DispositivoDAO
from dominio.gestor_dispositivo import GestorDispositivo
from util.validaciones import validar_nombre, validar_numero, validar_opcion
from datetime import datetime

def menu_admin(usuario):
    while True:
        print(f"\nHola {usuario.get_nombre()} (Administrador)")
        print("1. Gestionar usuarios")
        print("2. Gestionar dispositivos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crud_usuarios()
        elif opcion == "2":
            crud_dispositivos()
        elif opcion == "3":
            break
        else:
            print("Opción incorrecta.")

# --- CRUD Usuarios ---
def crud_usuarios():
    while True:
        print("\n--- CRUD Usuarios ---")
        print("1. Listar usuarios")
        print("2. Actualizar usuario")
        print("3. Eliminar usuario")
        print("4. Cambiar rol de usuario")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_usuarios()
        elif opcion == "2":
            actualizar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            cambiar_rol_usuario()
        elif opcion == "5":
            break
        else:
            print("Opción incorrecta.")

def listar_usuarios():
    usuarios = UsuarioDAO.listar_todos()
    if usuarios:
        for u in usuarios:
            print(f"- {u.get_id()} | {u.get_nombre()} | {u.get_email()} | {u.get_rol()} | {u.get_fecha_registro()}")
    else:
        print("No hay usuarios registrados.")

def actualizar_usuario():
    email = input("Ingrese el email del usuario: ")
    usuario = UsuarioDAO.obtener_por_email(email)
    if usuario:
        nuevo_nombre = input(f"Nuevo nombre ({usuario.get_nombre()}): ") or usuario.get_nombre()
        nueva_contrasena = input(f"Nueva contraseña: ") or usuario.get_contrasena()
        usuario.set_nombre(nuevo_nombre)
        usuario.set_contrasena(nueva_contrasena)
        UsuarioDAO.actualizar(usuario)
        print("Usuario actualizado.")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario():
    email = input("Ingrese el email del usuario: ")
    usuario = UsuarioDAO.obtener_por_email(email)
    if usuario:
        confirmar = input(f"¿Seguro que desea eliminar a {usuario.get_nombre()}? (s/n): ")
        if confirmar.lower() == "s":
            try:
                UsuarioDAO.eliminar(email)
            except Exception as e:
                print("No se puede eliminar el usuario. Primero elimine todos los dispositivos asociados.")
    else:
        print("Usuario no encontrado.")

def cambiar_rol_usuario():
    email = input("Ingrese el email del usuario: ")
    usuario = UsuarioDAO.obtener_por_email(email)
    if usuario:
        nuevo_rol = input(f"Nuevo rol ({usuario.get_rol()}): ").lower()
        usuario.set_rol(nuevo_rol)
        UsuarioDAO.actualizar(usuario)
        print("Rol actualizado.")
    else:
        print("Usuario no encontrado.")

# --- CRUD Dispositivos ---
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
    if dispositivos:
        for d in dispositivos:
            print(f"- {d.get_id()} | {d.get_nombre()} | {d.get_tipo()} | {d.get_estado()} | Usuario: {d.get_id_usuario()} | {d.get_fecha_registro()}")
    else:
        print("No hay dispositivos registrados.")

def registrar_dispositivo():
    id_usuario = int(input("ID usuario asignado: "))
    gestor = GestorDispositivo(id_usuario)

    nombre = input("Nombre dispositivo: ")
    tipo = input("Tipo: ")
    estado = input("Estado (encendido/apagado): ")

    gestor.agregar_dispositivo(nombre, tipo, estado)

def actualizar_dispositivo():
    id_usuario = int(input("ID usuario del dispositivo: "))
    gestor = GestorDispositivo(id_usuario)


    id_disp = int(input("ID del dispositivo a actualizar: "))
    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_tipo = input("Nuevo tipo: ")
    nuevo_estado = input("Nuevo estado (encendido/apagado): ")

    gestor.actualizar_dispositivo(id_disp, nuevo_nombre, nuevo_tipo, nuevo_estado)

def eliminar_dispositivo():
    id_usuario = int(input("ID usuario del dispositivo: "))
    gestor = GestorDispositivo(id_usuario)

    id_disp = int(input("ID del dispositivo a eliminar: "))
    gestor.eliminar_dispositivo(id_disp)
