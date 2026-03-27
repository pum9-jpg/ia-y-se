import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

datos_animales = [
    {'nombre': 'paloma', 'tiene_plumas': 1, 'canta': 0, 'vuela_bien': 1, 'clase': 'pajaro'}, 
    {'nombre': 'canario', 'tiene_plumas': 1, 'canta': 1, 'vuela_bien': 1, 'clase': 'canario'},
    {'nombre': 'gallina', 'tiene_plumas': 1, 'canta': 0, 'vuela_bien': 0, 'clase': 'ave_no_voladora'},
    {'nombre': 'pez_dorado', 'tiene_plumas': 0, 'canta': 0, 'vuela_bien': 0, 'clase': 'pez'},
    {'nombre': 'salmon', 'tiene_plumas': 0, 'canta': 0, 'vuela_bien': 0, 'clase': 'pez'},
]

df = pd.DataFrame(datos_animales)
features = ['tiene_plumas', 'canta', 'vuela_bien']
X = df[features]
y = df['clase']

modelo_inductivo = DecisionTreeClassifier()
modelo_inductivo.fit(X, y)

reglas_aprendidas = export_text(modelo_inductivo, feature_names=features)
print("-    Sistema de Razonamiento Inductivo -")
print("\nReglas que el sistema INDUJO a partir de los ejemplos:")
print(reglas_aprendidas)

animal_nuevo = pd.DataFrame([[1,1,1]], columns=features)
prediccion = modelo_inductivo.predict(animal_nuevo)

print(f"\nClasificando un animal nuevos con caracteristicas [Plumas=Si, Canta=Si, Vuela=Si]. ")
print(f"Conclusion probable: El animal es un '{prediccion[0]}'")