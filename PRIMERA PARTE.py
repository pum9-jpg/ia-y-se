# ================================================
# UNIDAD 3 - SISTEMAS EXPERTOS
# PARTE 1: Definir la Base de Conocimiento
# ================================================

# BASE DE CONOCIMIENTO
# Contiene el conocimiento de un mecánico experto.
# Cada regla tiene condiciones ("si"), una conclusión ("entonces") y un nombre identificador.

base_de_conocimiento_coche = [
    {
        "nombre": "Regla 1: Problema de batería o motor de arranque",
        "si": ["coche_no_gira_llave"],
        "entonces": "problema_bateria_o_arranque"
    },
    {
        "nombre": "Regla 2: Problema de combustible o encendido",
        "si": ["coche_gira_pero_no_enciende"],
        "entonces": "problema_combustible_o_encendido"
    },
    {
        "nombre": "Regla 3: Batería descargada confirmada",
        "si": ["problema_bateria_o_arranque", "luces_debiles_o_muertas"],
        "entonces": "diagnostico_bateria_descargada"
    },
    {
        "nombre": "Regla 4: Posible problema del motor de arranque",
        "si": ["problema_bateria_o_arranque", "luces_funcionan_bien"],
        "entonces": "diagnostico_motor_arranque_defectuoso"
    },
    {
        "nombre": "Regla 5: Posible problema de combustible",
        "si": ["problema_combustible_o_encendido", "huele_a_gasolina"],
        "entonces": "diagnostico_sistema_combustible"
    },
    {
        "nombre": "Regla 6: Posible problema de encendido",
        "si": ["problema_combustible_o_encendido", "no_huele_a_gasolina"],
        "entonces": "diagnostico_sistema_encendido"
    }
]

# -------------------------------------------------------
# Verificación básica: mostrar reglas cargadas
# -------------------------------------------------------
if __name__ == "__main__":
    print("\n=== BASE DE CONOCIMIENTO - SISTEMA EXPERTO DE COCHE ===\n")
    for regla in base_de_conocimiento_coche:
        print(f"{regla['nombre']}")
        print(f"  Si: {', '.join(regla['si'])}")
        print(f"  Entonces: {regla['entonces']}\n")
