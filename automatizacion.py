from data import lista_de_dispositivos
  

def modo_despertar(horario):
    encontrado_tv = False

    for dispositivo in lista_de_dispositivos:
        nombre_minuscula = dispositivo["nombre"].lower()
        if "tv" in nombre_minuscula:
            encontrado_tv = True
            break 
        
    print("\nModo Despertar programado:")
    if encontrado_tv:
        print(f"- El televisor se encenderá y reproducirá música a las {horario}.")
    else:
        print("- No se encontró el televisor para programar el modo despertar.")
