from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd

data = [
    {"tiene_plumas":1, "canta":1, "vive_en_agua":0, "pone_huevos":1, "clase":"canario"},
    {"tiene_plumas":1, "canta":0, "vive_en_agua":0, "pone_huevos":1, "clase":"ave"},
    {"tiene_plumas":0, "canta":0, "vive_en_agua":1, "pone_huevos":1, "clase":"pez"},
    {"tiene_plumas":0, "canta":0, "vive_en_agua":0, "pone_huevos":0, "clase":"mamifero"}
]

df = pd.DataFrame(data)
X = df[["tiene_plumas", "canta", "vive_en_agua", "pone_huevos"]]
y = df["clase"]

modelo = DecisionTreeClassifier(max_depth=3)
modelo.fit(X, y)

print("\nReglas aprendidas por el modelo:\n")
print(export_text(modelo, feature_names=list(X.columns)))

nuevo = pd.DataFrame([{"tiene_plumas":1, "canta":1, "vive_en_agua":0, "pone_huevos":1}])
print("Predicción para nuevo caso:", modelo.predict(nuevo)[0])