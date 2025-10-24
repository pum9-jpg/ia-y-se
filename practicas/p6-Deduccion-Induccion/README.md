# Unidad 4 — Razonamiento Deductivo e Inductivo

## Descripción
En esta unidad se presentan el enfoque de razonamiento:  
- **Deducción**, donde las conclusiones se derivan lógicamente de reglas existentes.  
---

## Código 
```python
# Parte 1: Deducción — Motor lógico de inferencia
reglas = [
    {"si": ["tiene_plumas"], "entonces": "es_ave"},
    {"si": ["es_ave", "canta"], "entonces": "es_canario"},
    {"si": ["pone_huevos", "vive_en_agua"], "entonces": "es_pez"},
    {"si": ["es_ave", "vuela_bien"], "entonces": "es_pajaro"}
]

hechos = {"tiene_plumas", "canta"}

nuevos = True
while nuevos:
    nuevos = False
    for regla in reglas:
        condiciones = set(regla["si"])
        conclusion = regla["entonces"]
        if condiciones.issubset(hechos) and conclusion not in hechos:
            hechos.add(conclusion)
            print(f"Se ha deducido: {conclusion}")
            nuevos = True

print("\nHechos finales deducidos:", hechos)

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
La deducción usa reglas existentes para llegar a conclusiones lógicas.


## Conclusión
La deducción permite obtener conclusiones lógicas a partir de hechos y reglas existentes, demostrando cómo un sistema puede razonar de manera estructurada siguiendo una base de conocimiento predefinida.