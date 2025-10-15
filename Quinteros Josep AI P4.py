# ----------------------------------------------------------
# BASE DE CONOCIMIENTO en formato *frames* (objetos con slots)
# ----------------------------------------------------------
base_conocimiento_frames = {
    "ponchadura": {
        "es_un": "problema_de_llanta",
        "sintomas": ["llanta_blanda"],
        "solucion": "parchar_o_cambiar_tubo",
        "herramientas_necesarias": ["bomba_de_aire", "parches", "pegamento"]
    },
    "cadena_desgastada": {
        "es_un": "problema_de_transmision",
        "sintomas": ["chasquido_al_pedalear", "cadena_salta"],
        "solucion": "reemplazar_cadena",
        "herramientas_necesarias": ["cortacadenas", "cadena_nueva"]
    }
    # Se podrían añadir más frames para otros componentes o problemas.
}

# ----------------------------------------------------------
# FUNCIÓN DE BÚSQUEDA POR SÍNTOMAS
# ----------------------------------------------------------
def buscar_problema_por_sintoma(sintomas_usuario, base_de_datos):
    for problema, detalles in base_de_datos.items():
        # Comprueba si todos los síntomas del usuario están en la
        # lista de síntomas del problema
        if all(sintoma in detalles["sintomas"] for sintoma in sintomas_usuario):
            return problema, detalles
    return None, None

# ----------------------------------------------------------
# EJECUCIÓN DE EJEMPLO
# ----------------------------------------------------------
print("\n- Usando Marcos (Frames) -")

hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]
problema_encontrado, detalles_problema = buscar_problema_por_sintoma(
    hechos_usuario, base_conocimiento_frames
)

if problema_encontrado:
    print(f"Problema identificado: {problema_encontrado}")
    print(f"  ➔ Es un tipo de: {detalles_problema['es_un']}")
    print(f"  ➔ La solución es: {detalles_problema['solucion']}")
    print(f"  ➔ Necesitarás: {', '.join(detalles_problema['herramientas_necesarias'])}")