# =====================================
# SISTEMA DE RAZONAMIENTO INDUCTIVO
# =====================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# ---- Datos de entrenamiento ----
# Cada fila es un ejemplo (animal) con sus características
# y la clase que queremos que aprenda (tipo de animal)
datos = pd.DataFrame([
    {"tiene_plumas": 1, "canta": 1, "pone_huevos": 1, "vive_en_agua": 0, "animal": "canario"},
    {"tiene_plumas": 1, "canta": 0, "pone_huevos": 1, "vive_en_agua": 0, "animal": "pajaro"},
    {"tiene_plumas": 0, "canta": 0, "pone_huevos": 1, "vive_en_agua": 1, "animal": "pez"},
    {"tiene_plumas": 0, "canta": 0, "pone_huevos": 0, "vive_en_agua": 1, "animal": "delfin"},
])

# ---- Separar características y etiquetas ----
X = datos.drop(columns=["animal"])
y = datos["animal"]

# ---- Crear y entrenar el modelo ----
modelo = DecisionTreeClassifier(criterion="entropy", random_state=0)
modelo.fit(X, y)

# ---- Visualizar el árbol aprendido ----
print("---- ÁRBOL DE DECISIÓN APRENDIDO ----")
print(export_text(modelo, feature_names=list(X.columns)))

# ---- Caso de uso: un animal nuevo ----
nuevo_animal = pd.DataFrame([{"tiene_plumas": 1, "canta": 1, "pone_huevos": 1, "vive_en_agua": 0}])
prediccion = modelo.predict(nuevo_animal)

print("\n---- PREDICCIÓN DEL SISTEMA INDUCTIVO ----")
print(f"Características del nuevo animal: {nuevo_animal.iloc[0].to_dict()}")
print(f"El modelo predice que es un: {prediccion[0]}")
