"""reglas_produccion.py
Implementación simple de la Parte 1: Reglas de Producción (IF-THEN)
Basado en el ejercicio práctico de la Unidad 2: Representación del Conocimiento.
Ejecutar como script para una demo interactiva.
"""

from typing import List, Dict, Optional

# Base de conocimiento: reglas de diagnóstico
base_conocimiento_reglas = {
    "regla_1": {
        "si": ["llanta_blanda"],
        "entonces": "diagnostico_ponchadura"
    },
    "regla_2": {
        "si": ["chasquido_al_pedalear", "cadena_salta"],
        "entonces": "diagnostico_cadena_desgastada"
    }
    # Se pueden añadir más reglas aquí
}

# Reglas para soluciones basadas en diagnóstico
base_conocimiento_soluciones = {
    "regla_3": {
        "si": ["diagnostico_ponchadura"],
        "entonces": "solucion_parchar_o_cambiar_tubo"
    },
    "regla_4": {
        "si": ["diagnostico_cadena_desgastada"],
        "entonces": "solucion_reemplazar_cadena"
    }
}

def diagnosticar_con_reglas(hechos: List[str],
                            reglas_diagnostico: Dict[str, Dict],
                            reglas_solucion: Dict[str, Dict]) -> Dict[str, Optional[str]]:
    """Devuelve un dict con diagnóstico y solución sugerida (si aplica)."""
    diagnostico = None
    # Buscar diagnóstico
    for nombre_regla, contenido in reglas_diagnostico.items():
        condiciones = contenido["si"]
        if all(condicion in hechos for condicion in condiciones):
            diagnostico = contenido["entonces"]
            break

    solucion = None
    if diagnostico:
        for nombre_regla, contenido in reglas_solucion.items():
            condiciones = contenido["si"]
            if diagnostico in condiciones:
                solucion = contenido["entonces"]
                break

    return {"diagnostico": diagnostico, "solucion": solucion}

def main():
    print("- Usando Reglas de Producción -\n")
    print("Ejemplo: indique los síntomas separados por comas (ej: chasquido_al_pedalear,cadena_salta)")
    entrada = input("Sintomas: ").strip()
    hechos_usuario = [s.strip() for s in entrada.split(",") if s.strip()]
    if not hechos_usuario:
        print("No se ingresaron síntomas. Usando ejemplo por defecto: ['chasquido_al_pedalear','cadena_salta']")
        hechos_usuario = ['chasquido_al_pedalear', 'cadena_salta']

    resultado = diagnosticar_con_reglas(hechos_usuario, base_conocimiento_reglas, base_conocimiento_soluciones)
    if resultado['diagnostico']:
        print(f"Diagnóstico: {resultado['diagnostico']}")
        if resultado['solucion']:
            print(f"Solución sugerida: {resultado['solucion']}")
        else:
            print("No hay una solución automática en la base de conocimiento.")
    else:
        print("No se encontró un diagnóstico para los síntomas proporcionados.")

if __name__ == '__main__':
    main()
