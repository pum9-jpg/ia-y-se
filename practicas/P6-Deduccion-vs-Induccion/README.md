
# 📘 Explicación de los Sistemas Expertos: Deductivo e Inductivo

Este documento describe el funcionamiento de dos tipos de **sistemas expertos** implementados en Python:  
uno **deductivo** y otro **inductivo**. Ambos buscan llegar a conclusiones sobre animales, pero emplean métodos diferentes.

---

## 🧠 1. Sistema Experto Deductivo

### 🔹 Código Completo

```python
class SistemaExpertoDeductivo:
    def __init__(self, reglas):
        self.reglas = reglas
        self.hechos = set()

    def razonar(self, hechos):
        self.hechos = set(hechos)
        nuevos_hechos = True
        while nuevos_hechos:
            nuevos_hechos = False
            for condiciones, resultado in self.reglas:
                if all(cond in self.hechos for cond in condiciones) and resultado not in self.hechos:
                    self.hechos.add(resultado)
                    nuevos_hechos = True
        return self.hechos

# - Base de Conocimiento (Reglas Generales) -
reglas_animales = [
    (["tiene_plumas"], "es_ave"),
    (["es_ave", "canta"], "es_cantor"),
    (["es_ave", "vuela_bien"], "es_pajaro"),
    (["tiene_pelo", "vive_en_agua"], "es_nutria"),
    (["es_pez", "vuela_bien"], "es_pez_volador")
]

# - Hechos de Uso -
hechos_especificos = ["tiene_plumas", "vuela_bien"]

# Creamos el sistema y razonamos
sistema = SistemaExpertoDeductivo(reglas_animales)
conclusion_final = sistema.razonar(hechos_especificos)

# Imprimimos el Sistema de Razonamiento Deductivo -
print("** Sistema de Razonamiento Deductivo - **")
print("Hechos iniciales: ", hechos_especificos)
print("Hechos deducidos: ", conclusion_final)
print("** Conclusión final: El animal es un ", [c for c in conclusion_final if c.startswith("es_")])
```

### ⚙️ Explicación

1. **Base de conocimiento:** contiene reglas lógicas como “si tiene plumas → es ave”.
2. **Motor de inferencia:** evalúa las reglas hasta no encontrar nuevas conclusiones.
3. **Resultado:** deduce que el animal con plumas y que vuela es un **pájaro**.

**Salida esperada:**
```
Hechos deducidos: {'es_pajaro', 'es_ave', 'vuela_bien', 'tiene_plumas'}
Conclusión final: El animal es un ['es_pajaro', 'es_ave']
```

---

## 🤖 2. Sistema Experto Inductivo

### 🔹 Código Completo

```python
# pip install scikit-learn pandas

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Datos de entrenamiento
# ['tiene_plumas', 'canta', 'vuela_bien']
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
```

### ⚙️ Explicación

1. **Datos de entrenamiento:** representan ejemplos previos de animales y sus características.
2. **Árbol de decisión:** el modelo aprende patrones a partir de esos ejemplos.
3. **Predicción:** al ingresar un nuevo conjunto de características, el modelo predice que el animal es un **pájaro**.

**Salida esperada:**
```
|--- tiene_plumas <= 0.50
|   |--- class: gato
|--- tiene_plumas > 0.50
|   |--- class: pajaro

Clasificando un animal nuevo con características [Plumas=SÍ, Canta=SÍ, Vuela=SÍ].
Conclusión probable: El animal es un «pajaro»
```

---

## 🧾 Comparación entre Deductivo e Inductivo

| Aspecto | Sistema Deductivo | Sistema Inductivo |
|----------|-------------------|-------------------|
| Enfoque | Basado en reglas | Basado en datos y aprendizaje |
| Fuente de conocimiento | Reglas predefinidas por expertos | Ejemplos o datos de entrenamiento |
| Tipo de razonamiento | Lógico (de lo general a lo particular) | Estadístico (de lo particular a lo general) |
| Ejemplo | "Si tiene plumas y vuela, es un ave." | Aprende que tener plumas → suele ser un pájaro |
| Flexibilidad | Limitada a las reglas definidas | Se adapta con nuevos datos |

---

## 🧩 Conclusión General

Ambos sistemas muestran dos formas distintas de razonar y llegar a conclusiones.
El sistema deductivo parte de reglas claras establecidas por una persona y aplica la lógica para deducir nuevos hechos, mientras que el sistema inductivo aprende por experiencia, analizando ejemplos hasta reconocer patrones.
En conjunto, permiten entender cómo una máquina puede razonar o aprender dependiendo de la información que se le proporcione.
En este caso, ambos sistemas llegan a la misma conclusión: —que el animal es un pájaro—, pero lo hacen siguiendo caminos diferentes: uno por lógica y el otro por aprendizaj

