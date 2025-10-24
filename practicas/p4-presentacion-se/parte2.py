# 1. BASE DE CONOCIMIENTO (Frames simples)
base_conocimiento_frames = {
    "ponchadura": {
        "es_un": "problema_de_llanta",
    },
    "cadena_desgastada": {
        "es_un": "problema_de_transmision",
    }
}

# 2. BASE DE DATOS (Frames detallados por categoría de problema)
base_de_datos = {
    "problemas_de_llanta": {
        "sintomas": ["llanta_blanda"],
        "solucion": "parchar_o_cambiar_tubo",
        "herramientas_necesarias": ["bomba_de_aire", "parches", "pegamento"]
    },
    "problemas_de_transmision": {
        "sintomas": ["chasquido_al_pedalar", "cadena_salta"],
        "solucion": "reemplazar_cadena",
        "herramientas_necesarias": ["desarmador", "cadena_nueva"]
    }
}

# 3. FUNCIÓN DE BÚSQUEDA
def buscar_problema_por_sintoma(sintomas_usuario, base_de_datos):
    for nombre_problema, detalles in base_de_datos.items():
        if any(s in detalles["sintomas"] for s in sintomas_usuario):
            return nombre_problema, detalles
    return None, None

# 4. PROGRAMA PRINCIPAL
hechos_usuario = ["chasquido_al_pedalar", "cadena_salta"]

problema_encontrado, detalles_problema = buscar_problema_por_sintoma(hechos_usuario, base_de_datos)

if problema_encontrado:
    print(f"Problema identificado: {problema_encontrado}")
    print(f" => Es un tipo de: {base_conocimiento_frames.get(problema_encontrado.replace('problemas_de_', ''), {}).get('es_un', 'desconocido')}")
    print(f" => La solución es: {detalles_problema['solucion']}")
    print(f" => Necesitarás: {', '.join(detalles_problema['herramientas_necesarias'])}")
else:
    print("No se encontró un problema con los síntomas proporcionados.")
