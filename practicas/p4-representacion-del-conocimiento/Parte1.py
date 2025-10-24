# La base de conocimiento se estructura como una lista de reglas de diagnóstico.
# Cada regla asocia un conjunto de síntomas con un problema.

base_conocimiento_reglas = {
    "regla_1": {
        "si": ["llanta_blanda"],
        "entonces": "diagnostico_ponchadura"
    },
    "regla_2": {
        "si": ["chasquido_al_pedalear", "cadena_salta"],
        "entonces": "diagnostico_cadena_desgastada"
    }
    # Se podrían añadir más reglas para otros problemas (frenos, cambios, etc.)
}

# También podemos tener reglas para las soluciones
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

# - Ejemplo de uso -
# Supongamos que un usuario nos da sus síntomas (hechos)
hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]

print("- Usando Reglas de Producción -")

def diagnosticar_con_reglas(hechos, reglas_diagnostico, reglas_solucion):
    diagnostico = None
    # Buscar un diagnóstico
    for nombre_regla, contenido in reglas_diagnostico.items():
        condiciones = contenido["si"]
        if all(condicion in hechos for condicion in condiciones):
            diagnostico = contenido["entonces"]
            print(f"Diagnóstico encontrado: {diagnostico}")
            break

    if diagnostico:
        for nombre_regla, conenido in reglas_solucion.items():
            if contenido["si"][0] == diagnostico:
                solucion = contenido["entonces"]
                print(f"Solución encontrada: {solucion}")
                return
    
    print("No se pudo encontrar un diagnóstico con los sintomas proporcionados.")
    
diagnosticar_con_reglas(hechos_usuario, base_conocimiento_reglas, base_conocimiento_soluciones)