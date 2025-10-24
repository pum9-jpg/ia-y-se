# ================================================
# UNIDAD 3 - SISTEMAS EXPERTOS
# SISTEMA EXPERTO DE DIAGNÓSTICO DE AUTOMÓVIL
# ================================================

# ---------------------------------------------
# 1. BASE DE CONOCIMIENTO
# ---------------------------------------------
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

# ---------------------------------------------
# 2. MOTOR DE INFERENCIA
# ---------------------------------------------
class SistemaExperto:
    def __init__(self, reglas):
        """
        Recibe la base de conocimiento (reglas).
        No contiene conocimiento del dominio, solo el motor lógico.
        """
        self.reglas = reglas
        self.hechos = set()
        self.historial_inferencia = {}  # Guarda qué regla generó cada conclusión

    def razonar(self, hechos_iniciales):
        """
        Encadenamiento hacia adelante:
        Aplica las reglas hasta que no haya nuevos hechos deducibles.
        """
        self.hechos = set(hechos_iniciales)
        nuevos_hechos_encontrados = True

        print("\n=== PROCESO DE RAZONAMIENTO ===\n")

        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]

                # Si todas las condiciones están cumplidas y la conclusión no está aún
                if condiciones.issubset(self.hechos) and conclusion not in self.hechos:
                    self.hechos.add(conclusion)
                    self.historial_inferencia[conclusion] = regla["nombre"]
                    print(f"✔ Hecho añadido: {conclusion} (por {regla['nombre']})")
                    nuevos_hechos_encontrados = True

        print("\n=== FIN DEL PROCESO DE RAZONAMIENTO ===\n")
        return self.hechos

    def obtener_diagnosticos_finales(self):
        """
        Devuelve los hechos que representan diagnósticos finales.
        """
        return [hecho for hecho in self.hechos if hecho.startswith("diagnostico_")]

    def explicar_conclusion(self, conclusion):
        """
        Muestra cómo se llegó a una conclusión (capacidad de explicación).
        """
        if conclusion not in self.historial_inferencia:
            if conclusion in self.hechos:
                return f"La conclusión '{conclusion}' fue un hecho inicial."
            else:
                return f"No se pudo determinar cómo se llegó a la conclusión '{conclusion}'."

        regla_que_lo_genero = self.historial_inferencia[conclusion]
        regla_completa = next((r for r in self.reglas if r["nombre"] == regla_que_lo_genero), None)

        if not regla_completa:
            return f"No se encontró información sobre la regla que generó '{conclusion}'."

        condiciones = regla_completa["si"]
        explicacion = f"Se llegó a la conclusión '{conclusion}' por la '{regla_que_lo_genero}'.\n"
        explicacion += f"Esta regla dice: SI se cumplen las condiciones {condiciones}, ENTONCES se deduce '{conclusion}'.\n"

        # Explicación recursiva
        for condicion in condiciones:
            explicacion += "\n" + self.explicar_conclusion(condicion)

        return explicacion


# ---------------------------------------------
# 3. EJEMPLO DE USO
# ---------------------------------------------
if __name__ == "__main__":
    # Hechos observados por el usuario (síntomas del auto)
    hechos_usuario = ["coche_no_gira_llave", "luces_funcionan_bien"]

    # Crear sistema experto
    sistema = SistemaExperto(base_de_conocimiento_coche)

    # Razonar con los hechos iniciales
    sistema.razonar(hechos_usuario)

    # Mostrar diagnósticos
    diagnosticos = sistema.obtener_diagnosticos_finales()
    print("Diagnósticos finales:", diagnosticos)

    # Mostrar explicación detallada del primer diagnóstico
    if diagnosticos:
        print("\n=== EXPLICACIÓN DEL DIAGNÓSTICO ===")
        print(sistema.explicar_conclusion(diagnosticos[0]))
