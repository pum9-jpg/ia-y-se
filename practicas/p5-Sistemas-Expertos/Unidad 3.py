# ==============================================
#       PARTE 1: Definir la Base de Conocimiento
# ==============================================

base_de_conocimiento_coche = [
    {
        "nombre": "Regla 1: Problema de bateria o motor de arranque",
        "si": ["coche_no_gira_llave"],
        "entonces": "problema_bateria_o_arranque"
    },
    {
        "nombre": "Regla 2: Problema de combustible o encendido",
        "si": ["coche_gira_pero_no_enciende"],
        "entonces": "problema_combustible_o_encendido"
    },
    {
        "nombre": "Regla 3: Bateria descargada confirmada",
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


# =======================================================================================
#         PARTE 2: Construir el Motor de Inferencia y la Estructura del Sistema
# =======================================================================================
class SistemaExperto:
    def __init__(self, reglas):
        self.reglas = reglas
        self.hechos = set()
        self.historial_inferencia = {}
        self.hechos_iniciales = set()

    def razonar(self, hechos_iniciales):
        self.hechos_iniciales = set(hechos_iniciales)
        self.hechos = set(hechos_iniciales)
        nuevos_hechos_encontrados = True

        print("\n--  INICIANDO DIAGNÓSTICO CASO 1 -")
        print("- Proceso de Razonamiento -")

        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]

                if condiciones.issubset(self.hechos) and conclusion not in self.hechos:
                    self.hechos.add(conclusion)
                    self.historial_inferencia[conclusion] = regla["nombre"]
                    print(f"Hecho añadido: '{conclusion}' (Gracias a la regla:")
                    print(f"'{regla['nombre']}')")
                    nuevos_hechos_encontrados = True

        print("- Fin del Proceso de Razonamiento -")
        return self.hechos

    def obtener_diagnosticos_finales(self):
        return [hecho for hecho in self.hechos if hecho.startswith("diagnostico_")]

    def explicar_conclusion(self, conclusion):
        if conclusion in self.hechos_iniciales:
            return f"\nLa conclusión '{conclusion}' fue un hecho inicial."

        if conclusion in self.historial_inferencia:
            regla_que_lo_genero = self.historial_inferencia[conclusion]
            regla_completa = next((r for r in self.reglas if r["nombre"] == regla_que_lo_genero), None)
            condiciones = regla_completa["si"]

            explicacion = f"\nSe llegó a la conclusión '{conclusion}' por la '{regla_que_lo_genero}'."
            explicacion += f"\nEsta regla establece que SI se cumplen las siguientes condiciones: {condiciones}, "
            explicacion += f"ENTONCES se deduce '{conclusion}'."

            for condicion in condiciones:
                explicacion += self.explicar_conclusion(condicion)
            return explicacion
        else:
            return f"\nNo se pudo determinar el origen de la conclusión '{conclusion}'."


# ======================================================================
#              PARTE 3: Ejecutar el Sistema y Obtener un Diagnóstico
# ======================================================================
print("\n# - Caso de Uso 1 -")
print("# Hechos iniciales: El coche no gira la llave y las luces están muertas.\n")

hechos_del_usuario_1 = [
    "coche_no_gira_llave",
    "luces_debiles_o_muertas"
]

# Creamos una instancia del sistema experto con el conocimiento del mecánico
se_coche = SistemaExperto(base_de_conocimiento_coche)

# El motor de inferencia procesa los hechos
hechos_finales_1 = se_coche.razonar(hechos_del_usuario_1)
diagnosticos_1 = se_coche.obtener_diagnosticos_finales()

print(f"\nHechos Finales Deducidos: {hechos_finales_1}")
print(f"Diagnóstico(s) Final(es): {diagnosticos_1}")

# Pedimos una explicación para el diagnóstico final
if diagnosticos_1:
    print("\n- EXPLICACIÓN DEL DIAGNÓSTICO -")
    print(se_coche.explicar_conclusion(diagnosticos_1[0]))