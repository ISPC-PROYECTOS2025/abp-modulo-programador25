def modo_despertar(dispositivos, horario):
    encontrado_tv = False

    for d in dispositivos:
        nombre_minuscula = d["nombre"].lower()
        if "tv" in nombre_minuscula or "televisor" in nombre_minuscula:
            encontrado_tv = True
            break  # sale del ciclo si encontró el TV

    print("\nModo Despertar programado:")
    if encontrado_tv:
        print(f"- El televisor se encenderá y reproducirá música a las {horario}.")
    else:
        print("- No se encontró el televisor para programar el modo despertar.")
