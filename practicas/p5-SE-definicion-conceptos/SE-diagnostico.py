# BASE DE CONOCIMIENTO
# Cada regla representa una relación causa-efecto entre síntomas y diagnóstico.

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

class SistemaExpertoCoche:
    def __init__(self, reglas):
        # 1. Separación: el conocimiento se pasa al sistema, no está dentro de él.
        self.reglas = reglas
        self.hechos = set()
        # Para la explicación, guardamos qué regla generó cada hecho.
        self.historial_inferencia = {}

    def razonar(self, hechos_iniciales):
        """
        MOTOR DE INFERENCIA
        Utiliza un algoritmo de encadenamiento hacia adelante.
        """
        self.hechos = set(hechos_iniciales)
        nuevos_hechos_encontrados = True

        print("- Proceso de Razonamiento -")
        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]

                # Si las condiciones se cumplen y la conclusión aún no existe
                if condiciones.issubset(self.hechos) and conclusion not in self.hechos:
                    self.hechos.add(conclusion)
                    self.historial_inferencia[conclusion] = regla["nombre"]
                    print(f"Hecho añadido: '{conclusion}' (Gracias a la regla: '{regla['nombre']}')")
                    nuevos_hechos_encontrados = True

        print("- Fin del Proceso de Razonamiento -")
        return self.hechos

    def obtener_diagnosticos_finales(self):
        """Filtra los hechos para mostrar solo los diagnósticos finales."""
        return [hecho for hecho in self.hechos if hecho.startswith('diagnostico_')]

    def explicar_conclusion(self, conclusion):
        """
        Capacidad de Explicación:
        Muestra cómo se llegó a una conclusión específica.
        """
        if conclusion not in self.historial_inferencia:
            if conclusion in self.hechos:
                return f"La conclusión '{conclusion}' fue un hecho inicial."
            else:
                return f"No se pudo determinar cómo se llegó a la conclusión '{conclusion}'."

        regla_que_lo_genero = self.historial_inferencia[conclusion]

        # Buscar la regla completa para mostrar sus condiciones
        regla_completa = next((r for r in self.reglas if r["nombre"] == regla_que_lo_genero), None)
        condiciones = regla_completa["si"]

        explicacion = f"\nSe llegó a la conclusión '{conclusion}' por la '{regla_que_lo_genero}'.\n"
        explicacion += f"Esta regla establece que SI se cumplen las siguientes condiciones: {condiciones}, "
        explicacion += f"ENTONCES se deduce '{conclusion}'.\n"

        # Explicar recursivamente las condiciones previas
        for condicion in condiciones:
            explicacion += self.explicar_conclusion(condicion)

        return explicacion


# - Caso de Uso 1 -
print("\nINICIANDO DIAGNÓSTICO CASO 1 -")

hechos_iniciales = ["coche_no_gira_llave", "luces_debiles_o_muertas"]

sistema = SistemaExpertoCoche(base_de_conocimiento_coche)
hechos_finales = sistema.razonar(hechos_iniciales)

print("\nHechos Finales Deducidos:", hechos_finales)
diagnosticos = sistema.obtener_diagnosticos_finales()
print("Diagnóstico(s) Final(es):", diagnosticos)

# Mostrar explicación del diagnóstico
if diagnosticos:
    print("\n- EXPLICACIÓN DEL DIAGNÓSTICO -")
    print(sistema.explicar_conclusion(diagnosticos[0]))

