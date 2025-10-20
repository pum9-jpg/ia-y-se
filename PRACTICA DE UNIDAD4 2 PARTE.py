# -----------------------------------------------
# Parte 2: Razonamiento Inductivo - Aprendiendo de Ejemplos
# -----------------------------------------------

# Instalar librerías necesarias (solo la primera vez)
# pip install scikit-learn pandas

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# -----------------------------------------------
# 1. Datos (Observaciones Específicas)
# -----------------------------------------------
# En lugar de reglas, tenemos ejemplos de animales observados

datos_animales = [
    {'nombre': 'paloma',  'tiene_plumas': 1, 'canta': 0, 'vuela_bien': 1, 'clase': 'pajaro'},
    {'nombre': 'canario', 'tiene_plumas': 1, 'canta': 1, 'vuela_bien': 1, 'clase': 'canario'},
    {'nombre': 'gallina', 'tiene_plumas': 1, 'canta': 0, 'vuela_bien': 0, 'clase': 'ave_no_voladora'},
    {'nombre': 'pez_dorado', 'tiene_plumas': 0, 'canta': 0, 'vuela_bien': 0, 'clase': 'pez'},
    {'nombre': 'salmon', 'tiene_plumas': 0, 'canta': 0, 'vuela_bien': 0, 'clase': 'pez'}
]

# Convertimos los datos a DataFrame para scikit-learn
df = pd.DataFrame(datos_animales)

# Las características (hechos observables)
features = ['tiene_plumas', 'canta', 'vuela_bien']

# Variable objetivo (lo que queremos predecir)
X = df[features]
y = df['clase']

# -----------------------------------------------
# 2. Proceso de Inducción (Aprendizaje)
# -----------------------------------------------
# Usamos un Árbol de Decisión: el algoritmo aprenderá reglas SI-ENTONCES
modelo_inductivo = DecisionTreeClassifier()
modelo_inductivo.fit(X, y)  # Aquí ocurre la "magia" del aprendizaje

# -----------------------------------------------
# 3. Resultados: Reglas "aprendidas"
# -----------------------------------------------
reglas_aprendidas = export_text(modelo_inductivo, feature_names=features)

print("\n--- Sistema de Razonamiento Inductivo ---")
print("\nReglas que el sistema INDUJO a partir de los ejemplos:")
print(reglas_aprendidas)

# -----------------------------------------------
# 4. Caso de uso: Clasificación de un nuevo animal
# -----------------------------------------------
# Ejemplo de entrada: un animal nuevo con plumas, que canta y vuela bien
animal_nuevo = pd.DataFrame([[1, 1, 1]], columns=features)

prediccion = modelo_inductivo.predict(animal_nuevo)

print(f"\nClasificando un animal nuevo con características [Plumas=Sí, Canta=Sí, Vuela=Sí]")
print(f"Conclusión probable: El animal es un '{prediccion[0]}'")
