#La base de conocimiento es un diccionario donde cada clave es un "frame" u objeto
#Cada frame tiene "slots" o atributos que lo describen

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
    #Se podrian añadir mas frames para describir otros componentes o problemas
}

#- Ejemplo de uso -
# Este tipo de representacion facilita la consulta de inforammacion sobre los objetos

print("\n- Usando Marcos (Frames) -")
def buscar_problemas_por_sintomas(sintomas_usuario, base_de_datos):
    for problema, detalles in base_de_datos.items():
        if all(sintoma in detalles["sintomas"] for sintoma in sintomas_usuario):
            return problema, detalles
    return None, None

hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]
problema_encontrado, detalles_problema = buscar_problemas_por_sintomas(hechos_usuario, base_conocimiento_frames)

if problema_encontrado:
    print(f"Problema identificado: {problema_encontrado}")
    print(f"-->  Es un tipo de: {detalles_problema['es_un']}")
    print(f"-->  La solucion es: {detalles_problema['solucion']}")
    print(f"-->  Necesitarias {', '.join(detalles_problema['herramientas_necesarias'])}")