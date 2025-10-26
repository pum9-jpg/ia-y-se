# sistema_inductivo.py
from sklearn import tree

# Datos de entrenamiento (Características de animales)
# [tiene_plumas, canta, vive_en_agua, pone_huevos]
X = [
    [1, 1, 0, 1],  # Canario
    [1, 0, 0, 1],  # Ave genérica
    [0, 0, 1, 1],  # Pez
    [1, 0, 0, 0],  # Murciélago (no pone huevos)
]

# Etiquetas correspondientes
Y = ["canario", "ave", "pez", "murcielago"]

# Crear el modelo (Árbol de Decisión)
modelo = tree.DecisionTreeClassifier()
modelo = modelo.fit(X, Y)

# Caso de uso: nuevo animal
nuevo_animal = [[1, 1, 0, 1]]  # Tiene plumas, canta, no vive en agua, pone huevos

prediccion = modelo.predict(nuevo_animal)

print("- Sistema de Razonamiento Inductivo -")
print("El modelo ha clasificado al animal como:", prediccion[0])
