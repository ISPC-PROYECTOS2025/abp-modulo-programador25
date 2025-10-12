from conn.db_conn import obtener_conexion
from dominio.usuario import Usuario
from dao.interfaces.i_usuario_dao import IUsuarioDAO

class UsuarioDAO(IUsuarioDAO):

    @staticmethod
    def registrar(usuario: Usuario):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = """
        INSERT INTO usuario (nombre_usuario, correo_electronico, contrasena, fecha_registro, rol)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            usuario.get_nombre(),
            usuario.get_email(),
            usuario.get_contrasena(),
            usuario.get_fecha_registro(),
            usuario.get_rol()
        ))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def obtener_por_email(email: str):
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        sql = """
        SELECT id_usuario, nombre_usuario, correo_electronico, contrasena, fecha_registro, rol
        FROM usuario
        WHERE correo_electronico = %s
        """
        cursor.execute(sql, (email,))
        fila = cursor.fetchone()
        cursor.close()
        conexion.close()
        if fila:
            return Usuario(
                id=fila['id_usuario'],
                nombre=fila['nombre_usuario'],
                email=fila['correo_electronico'],
                contrasena=fila['contrasena'],
                fecha_registro=fila['fecha_registro'],
                rol=fila['rol']
            )
        return None

    @staticmethod
    def listar_todos():
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("""
        SELECT id_usuario, nombre_usuario, correo_electronico, contrasena, fecha_registro, rol
        FROM usuario
        """)
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return [Usuario(
                id=fila['id_usuario'],
                nombre=fila['nombre_usuario'],
                email=fila['correo_electronico'],
                contrasena=fila['contrasena'],
                fecha_registro=fila['fecha_registro'],
                rol=fila['rol']
            ) for fila in filas]

    @staticmethod
    def actualizar(usuario: Usuario):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = """
        UPDATE usuario
        SET nombre_usuario=%s, contrasena=%s, rol=%s
        WHERE correo_electronico=%s
        """
        cursor.execute(sql, (
            usuario.get_nombre(),
            usuario.get_contrasena(),
            usuario.get_rol(),
            usuario.get_email()
        ))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar(email: str):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM usuario WHERE correo_electronico=%s"
        try:
            cursor.execute(sql, (email,))
            conexion.commit()
            print("Usuario eliminado.")
        except Exception as e:
            if e.errno == 1451:  # Foreign key constraint fails
                print("No se puede eliminar el usuario. Primero elimine todos los dispositivos asociados.")
            else:
                print(f"Error al eliminar el usuario: {e}")
        finally:
            cursor.close()
            conexion.close()


    @staticmethod
    def usuarios_con_mas_de_un_dispositivo():
        """Devuelve los usuarios que tienen más de un dispositivo (subconsulta)"""
        conexion = obtener_conexion()
        with conexion.cursor(dictionary=True) as cursor:
            sql = """
            SELECT nombre_usuario
            FROM usuario
            WHERE id_usuario IN (
                SELECT id_usuario
                FROM dispositivo
                GROUP BY id_usuario
                HAVING COUNT(*) > 1
            )
            """
            cursor.execute(sql)
            usuarios = cursor.fetchall()
        conexion.close()

        if not usuarios:
            return [{"nombre_usuario": "No hay usuarios con más de un dispositivo"}]
        
        return usuarios
