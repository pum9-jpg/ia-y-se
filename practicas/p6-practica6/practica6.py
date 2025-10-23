# Reutilizamos la estructura de nuestro SistemaExperto de la Unidad 3
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

# - Base de Conocimiento (Reglas Generales) -
reglas_animales = [
    {"si": ["tiene_plumas"], "entonces": "es_ave"},
    {"si": ["es_ave", "canta"], "entonces": "es_canario"},
    {"si": ["pone_huevos", "vive_en_agua"], "entonces": "es_pez"},
    {"si": ["es_ave", "vuela_bien"], "entonces": "es_pajaro"}  # Nueva regla
]

# - Caso de Uso -
# Hechos específicos de un animal misterioso
hechos_especificos = {"tiene_plumas", "canta"}

# Creamos el sistema y razonamos
sistema_deductivo = SistemaExpertoDeductivo(reglas_animales)
conclusion_final = sistema_deductivo.razonar(hechos_especificos)

print("- Sistema de Razonamiento Deductivo - ")
print(f"Hechos iniciales: {hechos_especificos}")
print(f"Hechos deducidos: {conclusion_final}")

# Encontrar la conclusión principal
conclusion_principal = next((c for c in conclusion_final if c.startswith('es_')), "desconocido")
print(f"Conclusión final: El animal es un '{conclusion_principal}'")

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# - Datos (Observaciones Específicas) -
# En lugar de reglas, tenemos una lista de ejemplos.
datos_animales = [
    {'nombre': 'paloma', 'tiene_plumas': 1, 'canta': 0, 'vuela_bien': 1, 'clase': 'pajaro'},
    {'nombre': 'canario', 'tiene_plumas': 1, 'canta': 1, 'vuela_bien': 1, 'clase': 'canario'},
    {'nombre': 'gallina', 'tiene_plumas': 1, 'canta': 0, 'vuela_bien': 0, 'clase': 'ave_no_voladora'},
    {'nombre': 'pez_dorado', 'tiene_plumas': 0, 'canta': 0, 'vuela_bien': 0, 'clase': 'pez'},
    {'nombre': 'salmon', 'tiene_plumas': 0, 'canta': 0, 'vuela_bien': 0, 'clase': 'pez'}
]

# Convertimos los datos a un formato que scikit-learn entiende (DataFrame de pandas)
df = pd.DataFrame(datos_animales)
features = ['tiene_plumas', 'canta', 'vuela_bien']
X = df[features]  # Las características (los "hechos")
y = df['clase']   # La etiqueta que queremos predecir (la "conclusión")

# - Proceso de Inducción (Aprendizaje) -
# Usamos un Árbol de Decisión, que aprende reglas tipo SI-ENTONCES.
modelo_inductivo = DecisionTreeClassifier()
modelo_inductivo.fit(X, y)  # Aquí ocurre la "magia": el modelo aprende las reglas de los datos.

# - Resultados: Las Reglas "Aprendidas" -
# Podemos visualizar las reglas que el algoritmo INDUJO de los datos.
reglas_aprendidas = export_text(modelo_inductivo, feature_names=features)
print("- Sistema de Razonamiento Inductivo - ")
print("\nReglas que el sistema INDUJO a partir de los ejemplos:")
print(reglas_aprendidas)

# - Caso de Uso -
# Ahora usamos el modelo aprendido para clasificar un animal nuevo y desconocido.
animal_nuevo = pd.DataFrame([[1, 1, 1]], columns=features)  # tiene_plumas=1, canta=1, vuela_bien=1
prediccion = modelo_inductivo.predict(animal_nuevo)

print(f"\nClasificando un animal nuevo con características [Plumas=Si, Canta=Si, Vuela=Si]: ")
print(f"Conclusión probable: El animal es un '{prediccion[0]}'")
