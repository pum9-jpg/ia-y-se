# 1. Instalación de librerías (Asumiendo que no están instaladas)
# pip install scikit-learn pandas

# Código Python Inductivo:
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Datos (Observaciones Específicas)
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
X = df[features] # Las características (los "hechos")
y = df['clase'] # La etiqueta que queremos predecir (la "conclusión")

# Proceso de Inducción (Aprendizaje)
# Usamos un Árbol de Decisión, que aprende reglas tipo SI-ENTONCES.
modelo_inductivo = DecisionTreeClassifier()
modelo_inductivo.fit(X, y) # Aquí ocurre la "magia": el modelo aprende las reglas de los datos.

# Resultados: Las Reglas "Aprendidas"
# Podemos visualizar las reglas que el algoritmo INDUJO de los datos.
reglas_aprendidas = export_text(modelo_inductivo, feature_names=features)

print("-\n- Sistema de Razonamiento Inductivo - ")
print("Reglas que el sistema INDUJO a partir de los ejemplos:")
print(reglas_aprendidas)

# Caso de Uso
# Ahora usamos el modelo aprendido para clasificar un animal nuevo y desconocido.
# Nuevo animal: tiene_plumas=1, canta=1, vuela_bien=1
animal_nuevo = pd.DataFrame([[1, 1, 1]], columns=features)
prediccion = modelo_inductivo.predict(animal_nuevo)

print("-" * 40)
print(f"Clasificando un animal nuevo con características [Plumas=Sí, Canta=Sí, Vuela=Sí].")
print(f"Conclusión probable: El animal es un '{prediccion[0]}'")

# Salida esperada (coincide con las imágenes):
"""
-
- Sistema de Razonamiento Inductivo -
Reglas que el sistema INDUJO a partir de los ejemplos:
|--- tiene_plumas <= 0.50
|   |--- class: pez
|--- tiene_plumas > 0.50
|   |--- canta <= 0.50
|   |   |--- vuela_bien <= 0.50
|   |   |   |--- class: ave_no_voladora
|   |   |--- vuela_bien > 0.50
|   |   |   |--- class: pajaro
|   |--- canta > 0.50
|   |   |--- class: canario
----------------------------------------
Clasificando un animal nuevo con características [Plumas=Sí, Canta=Sí, Vuela=Sí].
Conclusión probable: El animal es un 'canario'
"""