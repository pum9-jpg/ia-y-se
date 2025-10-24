# 1. BASE DE CONOCIMIENTO (Reglas de diagnóstico)
base_conocimiento_reglas = [
    {
        "regla_id": 1,
        "si": ["llanta_blanda"],
        "entonces": "diagnostico_pinchadura"
    },
    {
        "regla_id": 2,
        "si": ["chasquido_al_pedalear", "cadena_salta"],
        "entonces": "diagnostico_cadena_desgastada"
    }
]

# 2. BASE DE CONOCIMIENTO (Reglas de soluciones)
base_conocimiento_soluciones = [
    {
        "regla_id": 3,
        "si": ["diagnostico_pinchadura"],
        "entonces": "solucion_cambiar_o_parchar_tubo"
    },
    {
        "regla_id": 4,
        "si": ["diagnostico_cadena_desgastada"],
        "entonces": "solucion_reemplazar_cadena"
    }
]

# 3. MOTOR DE INFERENCIA
def diagnosticar_con_reglas(hechos, reglas_diagnostico, reglas_soluciones):
    diagnostico = None
    solucion = None

    # Buscar diagnóstico
    for regla in reglas_diagnostico:
        condiciones = regla["si"]
        if all(condicion in hechos for condicion in condiciones):
            diagnostico = regla["entonces"]
            print(f"Diagnóstico encontrado: {diagnostico}")
            break

    # Buscar solución si hay diagnóstico
    if diagnostico:
        for regla in reglas_soluciones:
            if regla["si"][0] == diagnostico:
                solucion = regla["entonces"]
                print(f"Solución encontrada: {solucion}")
                return

    print("No se pudo encontrar un diagnóstico con los síntomas proporcionados.")

# 4. EJEMPLO DE USO
hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]

diagnosticar_con_reglas(
    hechos_usuario,
    base_conocimiento_reglas,
    base_conocimiento_soluciones
)
