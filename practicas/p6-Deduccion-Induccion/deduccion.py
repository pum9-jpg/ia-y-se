reglas = [
    {"si": ["tiene_plumas"], "entonces": "es_ave"},
    {"si": ["es_ave", "canta"], "entonces": "es_canario"},
    {"si": ["pone_huevos", "vive_en_agua"], "entonces": "es_pez"},
    {"si": ["es_ave", "vuela_bien"], "entonces": "es_pajaro"}
]

hechos = {"tiene_plumas", "canta"}

nuevos = True
while nuevos:
    nuevos = False
    for regla in reglas:
        condiciones = set(regla["si"])
        conclusion = regla["entonces"]
        if condiciones.issubset(hechos) and conclusion not in hechos:
            hechos.add(conclusion)
            print(f"Se ha deducido: {conclusion}")
            nuevos = True

print("\nHechos finales deducidos:", hechos)