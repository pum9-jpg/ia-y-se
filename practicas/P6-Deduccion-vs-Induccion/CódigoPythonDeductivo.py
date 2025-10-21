class SistemaExpertoDeductivo:
    def __init__(self, reglas):
        self.reglas = reglas
        self.hechos = set()

    def razonar(self, hechos):
        self.hechos = set(hechos)
        nuevos_hechos = True
        while nuevos_hechos:
            nuevos_hechos = False
            for condiciones, resultado in self.reglas:
                if all(cond in self.hechos for cond in condiciones) and resultado not in self.hechos:
                    self.hechos.add(resultado)
                    nuevos_hechos = True
        return self.hechos

# - Base de Conocimiento (Reglas Generales) -
reglas_animales = [
    (["tiene_plumas"], "es_ave"),
    (["es_ave", "canta"], "es_cantor"),
    (["es_ave", "vuela_bien"], "es_pajaro"),
    (["tiene_pelo", "vive_en_agua"], "es_nutria"),
    (["es_pez", "vuela_bien"], "es_pez_volador")
]

# - Hechos de Uso -
hechos_especificos = ["tiene_plumas", "vuela_bien"]

# Creamos el sistema y razonamos
sistema = SistemaExpertoDeductivo(reglas_animales)
conclusion_final = sistema.razonar(hechos_especificos)

# Imprimimos el Sistema de Razonamiento Deductivo -
print("** Sistema de Razonamiento Deductivo - **")
print("Hechos iniciales: ", hechos_especificos)
print("Hechos deducidos: ", conclusion_final)
print("** Conclusión final: El animal es un ", [c for c in conclusion_final if c.startswith("es_")])
