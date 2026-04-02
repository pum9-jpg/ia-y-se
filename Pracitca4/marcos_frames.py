"""marcos_frames.py
Implementación simple de la Parte 2: Marcos (Frames)
Basado en el ejercicio práctico de la Unidad 2: Representación del Conocimiento.
Ejecutar como script para una demo interactiva.
"""

from typing import List, Dict, Tuple, Optional

# Base de conocimiento usando frames (marcos)
base_conocimiento_frames = {
    "ponchadura": {
        "es_un": "problema_de_neumatico",
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
    # Se pueden añadir más frames aquí
}

def buscar_problema_por_sintoma(sintomas_usuario: List[str],
                                base_de_datos: Dict[str, Dict]) -> Tuple[Optional[str], Optional[Dict]]:
    """Busca un problema cuyo conjunto de sintomas contenga todos los sintomas_usuario."""
    for problema, detalles in base_de_datos.items():
        if all(sintoma in detalles.get("sintomas", []) for sintoma in sintomas_usuario):
            return problema, detalles
    return None, None

def main():
    print("\n- Usando Marcos (Frames) -\n")
    print("Ejemplo: indique los síntomas separados por comas (ej: chasquido_al_pedalear,cadena_salta)")
    entrada = input("Sintomas: ").strip()
    sintomas_usuario = [s.strip() for s in entrada.split(",") if s.strip()]
    if not sintomas_usuario:
        print("No se ingresaron síntomas. Usando ejemplo por defecto: ['chasquido_al_pedalear','cadena_salta']")
        sintomas_usuario = ['chasquido_al_pedalear', 'cadena_salta']

    problema_encontrado, detalles_problema = buscar_problema_por_sintoma(sintomas_usuario, base_conocimiento_frames)
    if problema_encontrado:
        print(f"Problema identificado: {problema_encontrado}")
        print(f"  ➔ Es un tipo de: {detalles_problema.get('es_un')}")
        print(f"  ➔ La solución es: {detalles_problema.get('solucion')}")
        herramientas = detalles_problema.get('herramientas_necesarias', [])
        if herramientas:
            print(f"  ➔ Necesitarás: {', '.join(herramientas)}")
    else:
        print("No se encontró un problema que coincida exactamente con todos los síntomas proporcionados.")

if __name__ == '__main__':
    main()
