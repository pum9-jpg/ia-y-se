# Unidad 4 — Razonamiento Deductivo e Inductivo

## Descripción
En esta unidad se presenta el otro enfoque de razonamiento:  
- **Inducción**, donde se infieren reglas generales a partir de ejemplos.

---

## Código 
```python
# Parte 2: Inducción — Aprendizaje a partir de ejemplos
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
```
## Ejemplo de salida esperada
Se ha deducido: es_ave
Se ha deducido: es_canario
Hechos finales deducidos: {'tiene_plumas', 'canta', 'es_ave', 'es_canario'}

## Reglas aprendidas por el modelo:
|--- tiene_plumas <= 0.50
|   |--- clase: pez
|--- tiene_plumas >  0.50
|   |--- canta <= 0.50
|   |   |--- clase: ave
|   |--- canta >  0.50
|   |   |--- clase: canario

Predicción para nuevo caso: canario

## Observaciones

- La deducción usa reglas existentes para llegar a conclusiones lógicas.

- La inducción genera reglas a partir de ejemplos concretos.

- Ambos procesos son fundamentales en la Inteligencia Artificial simbólica y el aprendizaje automático.

## Conclusión
La inducción permite a un sistema aprender patrones y reglas generales a partir de ejemplos específicos, que de forma refleja la capacidad de la inteligencia artificial para generar conocimiento a partir de la experiencia.