import re

# -----------------------------
# VALIDACIONES BÁSICAS DE DATOS
# -----------------------------

def validar_email(email):
    """
    Verifica que el email tenga formato válido.
    Ejemplo válido: usuario@dominio.com
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None


def validar_contrasena(contrasena):
    """
    Valida que la contraseña tenga al menos 6 caracteres.
    (Podés agregar más condiciones si querés reforzar la seguridad)
    """
    return len(contrasena) >= 6


def validar_nombre(nombre):
    """
    Verifica que el nombre solo contenga letras y espacios.
    """
    return bool(re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', nombre))


def validar_opcion(opcion, opciones_validas):
    """
    Verifica que la opción elegida esté dentro de las opciones válidas.
    Ejemplo: validar_opcion('1', ['1', '2', '3'])
    """
    return opcion in opciones_validas


def validar_numero(valor):
    """
    Verifica que el valor ingresado sea un número entero positivo.
    """
    return valor.isdigit() and int(valor) >= 0
