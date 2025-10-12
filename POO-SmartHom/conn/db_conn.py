import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="4204136Jesi*",
        database="bd_gestion"
    )
    return conexion