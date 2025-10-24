# ================================================
# UNIDAD 2 - REPRESENTACIÓN DEL CONOCIMIENTO
# PARTE 1: Reglas de Producción (IF - THEN)
# ================================================

# ---- BASE DE CONOCIMIENTO: REGLAS DE DIAGNÓSTICO ----
base_conocimiento_reglas = {
    "regla_1": {
        "si": ["llanta_blanda"],
        "entonces": "diagnostico_ponchadura"
    },
    "regla_2": {
        "si": ["chasquido_al_pedalear", "cadena_salta"],
        "entonces": "diagnostico_cadena_desgastada"
    }
    # Puedes agregar más reglas según sea necesario
}

# ---- BASE DE CONOCIMIENTO: REGLAS DE SOLUCIÓN ----
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


# ---- MOTOR DE INFERENCIA ----
def diagnosticar_con_reglas(hechos, reglas_diagnostico, reglas_solucion):
    """
    Busca un diagnóstico a partir de los hechos y propone una solución.
    """
    diagnostico = None

    # Buscar un diagnóstico en las reglas
    for nombre_regla, contenido in reglas_diagnostico.items():
        condiciones = contenido["si"]
        # Verificar si todas las condiciones de la regla están presentes en los hechos
        if all(condicion in hechos for condicion in condiciones):
            diagnostico = contenido["entonces"]
            print(f"✅ Diagnóstico encontrado: {diagnostico}")
            break

    # Buscar la solución correspondiente
    if diagnostico:
        for nombre_regla, contenido in reglas_solucion.items():
            if diagnostico in contenido["si"]:
                solucion = contenido["entonces"]
                print(f"💡 Solución sugerida: {solucion}")
                return
        print("⚠️ No se encontró una solución asociada al diagnóstico.")
    else:
        print("❌ No se pudo encontrar un diagnóstico con los síntomas proporcionados.")


# ---- EJEMPLO DE USO ----
if __name__ == "__main__":
    # Hechos proporcionados por el usuario (síntomas observados)
    hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]

    print("\n=== SISTEMA EXPERTO: DIAGNÓSTICO DE BICICLETAS ===\n")
    diagnosticar_con_reglas(hechos_usuario, base_conocimiento_reglas, base_conocimiento_soluciones)
