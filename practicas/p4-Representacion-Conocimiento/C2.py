# La base de conocimiento es un diccionario donde cada clave es un "frame" u objeto.
# Cada frame tiene "slots" o atributos que lo describen.

base_conocimiento_frames = {
    "pinchadura": {
        "es_un": "problema_de_llanta",
        "síntomas": ["llanta_blanda"],
        "solución": "parchar_o_cambiar_tubo",
        "herramientas_necesarias": ["bombas_de_aire", "parches", "pegamento"]
    },
    "cadena_desgastada": {
        "es_un": "problema_de_transmisión",
        "síntomas": ["chasquido_al_pedaleer", "cadena_salta"],
        "solución": "reemplazar_cadena",
        "herramientas_necesarias": ["cortacadenas", "cadena_nueva"]
    }
}

# Se podrían añadir más frames para describir otros componentes o problemas.


# Ejemplo de uso
# Este tipo de representación facilita la consulta de información sobre los objetos.

print("\n Usando Marcos (Frames): \n")

def buscar_problema_por_síntoma(síntomas_usuario, base_de_datos):
    for problema, detalles in base_de_datos.items():
        # Compara si todos los síntomas del usuario están en la lista de síntomas del problema
        if all(síntoma in detalles["síntomas"] for síntoma in síntomas_usuario):
            return problema, detalles
    return None, None


# Datos del usuario
hechos_usuario = ["chasquido_al_pedaleer", "cadena_salta"]

# Buscar el problema en la base de conocimiento
problema_encontrado, detalles_problema = buscar_problema_por_síntoma(hechos_usuario, base_conocimiento_frames)

# Mostrar resultado
if problema_encontrado:
    print(f"Problema identificado: {problema_encontrado}")
    print(f"➡ Es un tipo de: {detalles_problema['es_un']}")
    print(f"➡ Solución: {detalles_problema['solución']}")
    print(f"➡ Herramientas necesarias: {', '.join(detalles_problema['herramientas_necesarias'])}")
else:
    print("No se encontró un problema que coincida con los síntomas.")
