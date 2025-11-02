# pip install scikit-learn pandas

# Código Python Inductivo:
from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd


# 1. Datos (Observaciones Específicas)
# A lo largo de reglas, tenemos unos list de ejemplos.
datos_animales = [
     {"nombre": "paloma", "tiene_plumas": 1, "canta": 1, "vuela_bien": 0, "clase": "pajaro" },
     {"nombre": "canario", "tiene_plumas": 1, "canta": 1, "vuela_bien": 1, "clase": "canario" },
     {"nombre": "gallina", "tiene_plumas": 1, "canta": 0, "vuela_bien": 0, "clase": "ave_no_voladora" },
     {"nombre": "pez_dorado", "tiene_plumas": 0, "canta": 0, "vuela_bien": 0, "clase": "pez" },
     {"nombre": "salmon", "tiene_plumas": 0, "canta": 0, "vuela_bien": 0, "clase": "pez" },
     
]

# Convertimos los datos a un formato que scikit-learn entienda
df = pd.DataFrame(datos_animales)
features = ["tiene_plumas", "canta", "vuela_bien"]
X = df[features]  # Las características (los “hechos”)
y = df["clase"]  # La etiqueta que queremos predecir (la “conclusión”)

# 2. Proceso de Inducción (Aprendizaje)
# Usamos un Árbol de Decisión, que aprende reglas tipo SI-ENTONCES
modelo_inductivo = DecisionTreeClassifier()
modelo_inductivo.fit(X, y)  # ¡Aquí ocurre la “magia”! el modelo aprende las reglas de los datos.

# 3. Resultados – Las Reglas “Aprendidas”
# Podemos visualizar las reglas que el árbol aprendió INDUCIDAS de los datos.
reglas_aprendidas = export_text(modelo_inductivo, feature_names=features)
print("=== Sistema de Razonamiento Inductivo ===")
print("Reglas aprendidas (sistema INDUCIDO a partir de los ejemplos):")
print(reglas_aprendidas)

# 4. Aplicación – Clasificar un nuevo caso
# Damos un nuevo animal y pedimos al modelo que lo clasifique.
animal_nuevo = pd.DataFrame([{"tiene_plumas": 1, "canta": 1, "vuela_bien": 1}])
prediccion = modelo_inductivo.predict(animal_nuevo)

print(f"\nClasificación de un animal nuevo con características {animal_nuevo.to_dict(orient='records')[0]}:")
print(f"El modelo inductivo predice que es un '{prediccion[0]}'")