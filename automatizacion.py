def modo_despertar(dispositivos):
    encontrado_tv = False

    for d in dispositivos:
        nombre_minuscula = d["nombre"].lower()
        if "tv" in nombre_minuscula or "televisor" in nombre_minuscula:
            d["estado"] = "encendido y reproduciendo música"
            encontrado_tv = True
            break  # sale del ciclo si encontró el TV

    print("\nModo Despertar activado:")
    if encontrado_tv:
        print("- El televisor está encendido y reproduciendo música.")
    else:
        print("- No se encontró el televisor.")
