import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# -  Datos (Observaciones Específicas) -
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

# Definimos las características
features = ['tiene_plumas', 'canta', 'vuela_bien']
X = df[features]  # Las características (los "hechos")
y = df['clase']   # La variable objetivo (la clase o tipo de animal)

# Entrenamos el modelo de árbol de decisión
modelo = DecisionTreeClassifier()
modelo.fit(X, y)

# Mostramos el árbol aprendido en texto
arbol_texto = export_text(modelo, feature_names=features)
print("Árbol de decisión aprendido:\n")
print(arbol_texto)

# Probamos con un nuevo animal misterioso
nuevo_animal = pd.DataFrame([{'tiene_plumas': 1, 'canta': 1, 'vuela_bien': 1}])
prediccion = modelo.predict(nuevo_animal)

print("\nAnimal misterioso:")
print(nuevo_animal)
print(f"\nPredicción: El animal pertenece a la clase '{prediccion[0]}'")
y = df['clase']  # La etiqueta que queremos predecir (la "conclusión")


# -  Proceso de Inducción (Aprendizaje) -
# Usamos un Árbol de Decisión, que aprende reglas tipo SI-ENTONCES.
modelo_inductivo = DecisionTreeClassifier()
modelo_inductivo.fit(X, y) # Aquí ocurre la "magia": el modelo aprende las reglas de los datos.

# -  Resultados: Las Reglas "Aprendidas" -
# Podemos visualizar las reglas que el algoritmo INDUJO de los datos.
reglas_aprendidas = export_text(modelo_inductivo, feature_names=features)
print("-  Sistema de Razonamiento Inductivo -  ")
print("\nReglas que el sistema INDUJO a partir de los ejemplos:")
print(reglas_aprendidas)

# -  Caso de Uso -
# Ahora usamos el modelo aprendido para clasificar un animal nuevo y desconocido.
animal_nuevo = pd.DataFrame([[1, 1, 1]], columns=features) # tiene_plumas=1, canta=1, vuela_bien=1
prediccion = modelo_inductivo.predict(animal_nuevo)

print(f"\nClasificando un animal nuevo con características [Plumas=Sí, Canta=Sí, Vuela=Sí]. ")
print(f"Conclusión probable: El animal es un '{prediccion[0]}'")