from conn.db_conn import obtener_conexion
from dominio.dispositivo import Dispositivo
from dao.interfaces.i_dispositivo_dao import IDispositivoDAO

class DispositivoDAO(IDispositivoDAO):

    @staticmethod
    def registrar(dispositivo: Dispositivo):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO dispositivo (nombre, tipo, id_usuario, fecha_registro) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (
                dispositivo.get_nombre(),
                dispositivo.get_tipo(),
                dispositivo.get_id_usuario(),
                dispositivo.get_fecha_registro()
            ))
            conexion.commit()
        conexion.close()

    @staticmethod
    def listar_todos():
        conexion = obtener_conexion()
        dispositivos = []
        with conexion.cursor() as cursor:
            sql = "SELECT id_dispositivo, nombre, tipo, id_usuario, fecha_registro FROM dispositivo"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for fila in resultados:
                d = Dispositivo(
                    id=fila[0],
                    nombre=fila[1],
                    tipo=fila[2],
                    id_usuario=fila[3],
                    fecha_registro=fila[4]
                )
                dispositivos.append(d)
        conexion.close()
        return dispositivos

    @staticmethod
    def listar_por_usuario(id_usuario):
        conexion = obtener_conexion()
        dispositivos = []
        with conexion.cursor() as cursor:
            sql = "SELECT id_dispositivo, nombre, tipo, id_usuario, fecha_registro FROM dispositivo WHERE id_usuario = %s"
            cursor.execute(sql, (id_usuario,))
            resultados = cursor.fetchall()
            for fila in resultados:
                d = Dispositivo(
                    id=fila[0],
                    nombre=fila[1],
                    tipo=fila[2],
                    id_usuario=fila[3],
                    fecha_registro=fila[4]
                )
                dispositivos.append(d)
        conexion.close()
        return dispositivos

    @staticmethod
    def obtener_por_id(id_dispositivo):
        conexion = obtener_conexion()
        dispositivo = None
        with conexion.cursor() as cursor:
            sql = "SELECT id_dispositivo, nombre, tipo, id_usuario, fecha_registro FROM dispositivo WHERE id_dispositivo = %s"
            cursor.execute(sql, (id_dispositivo,))
            resultado = cursor.fetchone()
            if resultado:
                dispositivo = Dispositivo(
                    id=resultado[0],
                    nombre=resultado[1],
                    tipo=resultado[2],
                    id_usuario=resultado[3],
                    fecha_registro=resultado[4]
                )
        conexion.close()
        return dispositivo

    @staticmethod
    def actualizar(dispositivo: Dispositivo):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "UPDATE dispositivo SET nombre=%s, tipo=%s, id_usuario=%s WHERE id_dispositivo=%s"
            cursor.execute(sql, (
                dispositivo.get_nombre(),
                dispositivo.get_tipo(),
                dispositivo.get_id_usuario(),
                dispositivo.get_id()
            ))
            conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id_dispositivo):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "DELETE FROM dispositivo WHERE id_dispositivo=%s"
            cursor.execute(sql, (id_dispositivo,))
            conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_dispositivos_con_usuario():
        """Devuelve todos los dispositivos con el nombre del usuario dueño"""
        conexion = obtener_conexion()
        dispositivos = []
        with conexion.cursor(dictionary=True) as cursor:
            sql = """
            SELECT d.nombre AS dispositivo, d.tipo, u.nombre_usuario
            FROM dispositivo d
            JOIN usuario u ON d.id_usuario = u.id_usuario
            """
            cursor.execute(sql)
            dispositivos = cursor.fetchall()
        conexion.close()
        return dispositivos

    
