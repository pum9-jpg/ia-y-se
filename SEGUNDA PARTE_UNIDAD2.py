# ================================================
# UNIDAD 2 - REPRESENTACIÓN DEL CONOCIMIENTO
# PARTE 2: Representación mediante MARCOS (FRAMES)
# ================================================

# La base de conocimiento es un diccionario donde cada clave es un "frame" u objeto.
# Cada frame tiene "slots" o atributos que lo describen.

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
    # Se pueden añadir más frames para describir otros componentes o problemas
}

# -------------------------------------------------------
# FUNCIÓN DE BÚSQUEDA (MOTOR DE CONSULTA)
# -------------------------------------------------------

def buscar_problema_por_sintoma(sintomas_usuario, base_de_datos):
    """
    Busca en la base de conocimiento un problema cuyos síntomas coincidan
    con los proporcionados por el usuario.
    """
    for problema, detalles in base_de_datos.items():
        # Verificar si todos los síntomas del usuario coinciden con los del problema
        if all(sintoma in detalles["sintomas"] for sintoma in sintomas_usuario):
            return problema, detalles
    return None, None


# -------------------------------------------------------
# EJEMPLO DE USO
# -------------------------------------------------------

print("\n=== Usando MARCOS (FRAMES) ===\n")

# Síntomas dados por el usuario
hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]

# Buscar el problema
problema_encontrado, detalles_problema = buscar_problema_por_sintoma(hechos_usuario, base_conocimiento_frames)

# Mostrar resultados
if problema_encontrado:
    print(f"✅ Problema identificado: {problema_encontrado}")
    print(f"🧩 Tipo: {detalles_problema['es_un']}")
    print(f"💡 Solución sugerida: {detalles_problema['solucion']}")
    print(f"🧰 Herramientas necesarias: {', '.join(detalles_problema['herramientas_necesarias'])}")
else:
    print("❌ No se pudo identificar el problema con los síntomas proporcionados.")
