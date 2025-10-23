# sistema_deductivo.py
class SistemaExpertoDeductivo:
    def __init__(self, reglas):
        self.reglas = reglas

    def razonar(self, hechos):
        hechos_deducidos = set(hechos)
        nuevos_hechos_encontrados = True
        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]
                if condiciones.issubset(hechos_deducidos) and conclusion not in hechos_deducidos:
                    hechos_deducidos.add(conclusion)
                    nuevos_hechos_encontrados = True
        return hechos_deducidos


# Base de Conocimiento (Reglas Generales)
reglas_animales = [
    {"si": ["tiene_plumas"], "entonces": "es_ave"},
    {"si": ["es_ave", "canta"], "entonces": "es_canario"},
    {"si": ["pone_huevos", "vive_en_agua"], "entonces": "es_pez"},
    {"si": ["es_ave", "vuela_bien"], "entonces": "es_pajaro"}  # Nueva regla
]

# Caso de Uso
hechos_especificos = {"tiene_plumas", "canta"}

# Crear sistema y razonar
sistema_deductivo = SistemaExpertoDeductivo(reglas_animales)
conclusion_final = sistema_deductivo.razonar(hechos_especificos)

print("- Sistema de Razonamiento Deductivo -")
print(f"Hechos iniciales: {hechos_especificos}")
print(f"Hechos deducidos: {conclusion_final}")
print(f"Conclusión final: El animal es un '{next(c for c in conclusion_final if c.startswith('es_'))}'")
