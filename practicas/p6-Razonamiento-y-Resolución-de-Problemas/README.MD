# Documentación: Sistemas de Razonamiento Deductivo e Inductivo en Python

## 1. Introducción

Esta documentación explica el funcionamiento de dos sistemas de razonamiento aplicados al reconocimiento de animales:

* **Razonamiento Deductivo:** Utiliza reglas y hechos conocidos para deducir conclusiones.
* **Razonamiento Inductivo:** Aprende patrones a partir de ejemplos para generar reglas y predecir nuevas conclusiones.

Se incluyen detalles sobre cómo funciona cada código, los resultados esperados y los requisitos para ejecutar los scripts.

---

## Parte 1: Sistema de Razonamiento Deductivo

### Requisitos para ejecutar

* Python
* No se necesitan librerías externas.

### Código

```python
class SistemaExpertoDeductivo:
    def __init__(self, reglas):
        self.reglas = reglas

    def razonar(self, hechos):
        hechos_deducidos = set(hechos)
        nuevos_hechos_encontrados = True

        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]

                if condiciones.issubset(hechos_deducidos) and conclusion not in hechos_deducidos:
                    hechos_deducidos.add(conclusion)
                    nuevos_hechos_encontrados = True
        return hechos_deducidos

reglas_animales = [
    {"si": {"tiene_plumas"}, "entonces": "es_ave"},
    {"si": {"es_ave", "canta"}, "entonces": "es_canario"},
    {"si": {"pone_huevos", "vive_en_agua"}, "entonces": "es_pez"},
    {"si": {"es_ave", "vuela_bien"}, "entonces": "es_pajaro"}
]

hechos_especificos = {"tiene_plumas", "canta"}

sistema_deductivo = SistemaExpertoDeductivo(reglas_animales)
conclusion_final = sistema_deductivo.razonar(hechos_especificos)

print("\n--- Sistema de Razonamiento Deductivo ---")
print(f"Hechos Iniciales: {hechos_especificos}")
print(f"Hechos Deducidos: {conclusion_final}")
print(f"Conclusión Final: El animal es un '{next(f for f in conclusion_final if f.startswith('es_'))}'")
```

### Cómo funciona

1. Se define una clase que contiene las reglas del sistema.
2. Se reciben los hechos iniciales que describen al animal misterioso.
3. Se aplican todas las reglas de manera iterativa hasta que no se encuentren nuevos hechos.
4. Cada regla tiene condiciones (`si`) y una conclusión (`entonces`). Si todas las condiciones están en los hechos, la conclusión se agrega.

### Resultado esperado

* **Hechos Iniciales:** {"tiene_plumas", "canta"}
* **Hechos Deducidos:** {'tiene_plumas', 'canta', 'es_ave', 'es_canario'}
* **Conclusión Final:** El animal es un 'es_canario'

---

## Parte 2: Sistema de Razonamiento Inductivo

### Requisitos para ejecutar

* Python
* Librerías: `pandas`, `scikit-learn`

```bash
pip install pandas scikit-learn
```

### Código

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Datos de entrenamiento
datos_animales = [
    {"nombre": "paloma", "tiene_plumas": 1, "canta": 0, "vuela_bien": 1, "clase": "ave"},
    {"nombre": "canario", "tiene_plumas": 1, "canta": 1, "vuela_bien": 1, "clase": "ave"},
    {"nombre": "pez", "tiene_plumas": 0, "canta": 0, "vuela_bien": 0, "clase": "pez"},
    {"nombre": "pato", "tiene_plumas": 1, "canta": 0, "vuela_bien": 0, "clase": "ave"},
    {"nombre": "murciélago", "tiene_plumas": 0, "canta": 1, "vuela_bien": 1, "clase": "mamífero"},
    {"nombre": "león", "tiene_plumas": 0, "canta": 1, "vuela_bien": 0, "clase": "mamífero"},
    {"nombre": "pingüino", "tiene_plumas": 1, "canta": 0, "vuela_bien": 0, "clase": "ave"},
]

# Convertir datos a DataFrame
df = pd.DataFrame(datos_animales)
X = df[["tiene_plumas", "canta", "vuela_bien"]]
y = df["clase"]

# Entrenamiento
modelo_inductivo = DecisionTreeClassifier()
modelo_inductivo.fit(X, y)

# Visualización de reglas aprendidas
reglas_aprendidas = export_text(modelo_inductivo, feature_names=list(X.columns))
print("=== Sistema de Razonamiento Inductivo ===")
print(reglas_aprendidas)

# Clasificación de un nuevo animal
animal_nuevo = pd.DataFrame([{"tiene_plumas": 1, "canta": 1, "vuela_bien": 1}])
prediccion = modelo_inductivo.predict(animal_nuevo)
print(f"El modelo predice que es un '{prediccion[0]}'")
```

### Cómo funciona

1. Se define un conjunto de ejemplos con características y clases conocidas.
2. Se crea un DataFrame con las características predictoras (`X`) y la etiqueta (`y`).
3. Se entrena un árbol de decisión que genera reglas a partir de los datos.
4. `export_text` permite visualizar las reglas aprendidas.
5. Se puede predecir la clase de un animal desconocido usando estas reglas.

### Resultado esperado

* **Reglas aprendidas:** Varias reglas tipo SI-ENTONCES generadas automáticamente por el árbol.
* **Predicción de nuevo animal:** Por ejemplo, para un animal con `tiene_plumas=1`, `canta=1`, `vuela_bien=1`, el modelo predice que es un 'ave'.

---

## Conclusiones

* El sistema deductivo aplica reglas conocidas para deducir información específica.
* El sistema inductivo genera reglas a partir de ejemplos y predice nuevas conclusiones.
* Ambos códigos requieren Python , y el inductivo requiere librerías adicionales (`pandas`, `scikit-learn`).
