# Sistema de Diagnóstico - Enfoque Basado en Marcos (Frames)

## Descripción
Este enfoque utiliza una **representación basada en marcos (frames)** para modelar conocimiento sobre fallas mecánicas.  
Cada frame describe un tipo de problema con sus atributos (síntomas, solución y herramientas necesarias).  
Esto permite acceder y razonar sobre los datos de manera más estructurada y semántica.

## Código
```python
# Base de conocimiento en formato de Frames
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
}

print("\n--- Usando Marcos (Frames) ---\n")

def buscar_problema_por_sintomas(sintomas_usuario, base_de_datos):
    for problema, detalles in base_de_datos.items():
        if all(sintoma in detalles["sintomas"] for sintoma in sintomas_usuario):
            return problema, detalles
    return None, None

# Hechos del usuario
hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]

# Buscar problema en la base de conocimiento
problema_encontrado, detalles_problema = buscar_problema_por_sintomas(hechos_usuario, base_conocimiento_frames)

if problema_encontrado:
    print(f" Problema identificado: {problema_encontrado}")
    print(f"   - Es un tipo de: {detalles_problema['es_un']}")
    print(f"   - La solución es: {detalles_problema['solucion']}")
    print(f"   - Herramientas necesarias: {', '.join(detalles_problema['herramientas_necesarias'])}")
else:
    print("No se encontró un problema que coincida con los síntomas dados.")
```

## Ejemplo de uso
El usuario reporta los síntomas:  
- **chasquido al pedalear**  
- **cadena salta**  

**Resultado esperado:**  
> Problema identificado: cadena_desgastada  
> Es un tipo de: problema_de_transmision  
> La solución es: reemplazar_cadena  
> Herramientas necesarias: cortacadenas, cadena_nueva

## Observaciones
Los marcos permiten organizar la información de forma jerárquica y reutilizable.  
Son ideales cuando los objetos comparten características o atributos similares.

## Conclusión
Ofrece una representación **más flexible y semántica** del conocimiento, diferenciandose de las reglas, los frames permiten ampliar el sistema fácilmente al agregar nuevos objetos o atributos, lo que lo hace más escalable y mantenible en sistemas complejos.
