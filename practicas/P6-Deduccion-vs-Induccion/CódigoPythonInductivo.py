# pip install scikit-learn pandas

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Datos de entrenamiento
# [‘tiene_plumas’, ‘canta’, ‘vuela_bien’]
datos_animales = [
    ['pajaro', True, True, True],
    ['pajaro', True, False, True],
    ['pajaro', True, True, False],
    ['gato', False, True, False],
    ['gato', False, False, False],
    ['gato', False, False, True],  # si aplica
]

# Crear un DataFrame
df = pd.DataFrame(datos_animales, columns=['animal', 'tiene_plumas', 'canta', 'vuela_bien'])

# Separar las características (los “hechos”) y la clase
X = df[['tiene_plumas', 'canta', 'vuela_bien']]
y = df['animal']

# Crear el modelo
modelo = DecisionTreeClassifier()

# Proceso de Inducción (Aprendizaje)
modelo.fit(X, y)

# Visualizar el árbol de decisión
arbol_texto = export_text(modelo, feature_names=['tiene_plumas', 'canta', 'vuela_bien'])
print(arbol_texto)

# Proceso de Predicción
# Clasificar un nuevo animal con los hechos de los ejemplos:
# [True, True, True]
animal_nuevo = pd.DataFrame([[True, True, True]], columns=['tiene_plumas', 'canta', 'vuela_bien'])
prediccion = modelo.predict(animal_nuevo)

print(f"\nClasificando un animal nuevo con características [Plumas=SÍ, Canta=SÍ, Vuela=SÍ]. ")
print(f"Conclusión probable: El animal es un «{prediccion[0]}»")
