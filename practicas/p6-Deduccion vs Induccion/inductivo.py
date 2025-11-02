import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Datos (Observaciones Específicas)
datos = [
    {"nombre": "paloma", "tiene_plumas": 1, "canta": 0, "vuela_bien": 1, "es_ave": 1},
    {"nombre": "canario", "tiene_plumas": 1, "canta": 1, "vuela_bien": 1, "es_ave": 1},
    {"nombre": "pez", "tiene_plumas": 0, "canta": 0, "vuela_bien": 0, "es_ave": 0},
    {"nombre": "pato", "tiene_plumas": 1, "canta": 0, "vuela_bien": 1, "es_ave": 1}
]

# Convertimos los datos en un formato que entienda sklearn
df = pd.DataFrame(datos)
caracteristicas = ["tiene_plumas", "canta", "vuela_bien"]
objetivo = "es_ave"

# Creamos y entrenamos el modelo (Árbol de Decisión)
modelo = DecisionTreeClassifier()
modelo.fit(df[caracteristicas], df[objetivo])

# Mostramos la regla inducida a partir de los ejemplos
reglas = export_text(modelo, feature_names=caracteristicas)
print("\n--- Sistema de Razonamiento Inductivo ---")
print("Regla(s) aprendida(s) a partir de los ejemplos:")
print(reglas)

# Prueba de predicción (nuevo caso)
nuevo_animal = pd.DataFrame([{"tiene_plumas": 1, "canta": 1, "vuela_bien": 1}])
prediccion = modelo.predict(nuevo_animal)

print("\nPredicción para un animal con esas características:")
print("¿Es un ave?:", "Sí" if prediccion[0] == 1 else "No")
