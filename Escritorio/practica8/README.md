# Sistema de Razonamiento Inductivo (Árbol de Decisión) 🌳

Este script de Python simula un sistema de **Razonamiento Inductivo**, un pilar del aprendizaje automático (Machine Learning). A diferencia de los sistemas deductivos (basados en reglas fijas), el sistema inductivo **genera sus propias reglas** observando una serie de ejemplos y patrones en los datos.

## 💡 Conceptos Clave

1.  **DATOS (`datos_animales`)**: La base del conocimiento. Son **observaciones específicas** (ejemplos) de animales con sus características (`features`) y su clase final (`clase`).
2.  **INDUCCIÓN (Aprendizaje)**: El proceso central. El clasificador `DecisionTreeClassifier` analiza los datos y deduce **reglas generales** (un árbol) que relacionan las características con la clase.
3.  **REGLAS APRENDIDAS**: Son las reglas lógicas **SI... ENTONCES...** que el modelo infiere para segmentar los datos de la manera más eficiente posible.

---

## 🚀 ¿Cómo funciona el Razonamiento Inductivo?

El Árbol de Decisión utiliza los datos para encontrar la característica (o *feature*) que mejor divide los ejemplos en clases puras.

**Proceso Lógico:**

1.  **Observación**: El modelo ve que si `tiene_plumas = 0`, el animal siempre es un 'pez'.
2.  **División Principal**: Crea la primera regla: **SI** `tiene_plumas <= 0.50`, **ENTONCES** la clase es 'pez'.
3.  **Subdivisión**: Si `tiene_plumas = 1`, el modelo busca la siguiente mejor característica (en este caso, `canta` o `vuela_bien`) para refinar la clasificación.

El resultado es un conjunto de reglas jerárquicas que se utilizan para predecir la clase de un animal desconocido.

---

## ⚙️ Requisitos

Necesitas tener **Python** instalado, junto con las bibliotecas **pandas** y **scikit-learn** (sklearn).

Para instalar las dependencias, usa este comando en tu terminal:

```bash
pip install pandas scikit-learn

```
### Ejecución Rápida
Sigue estos pasos para ejecutar el script:

### 1. Guarda el Código
Copia todo el código Python y guárdalo en un archivo llamado, por ejemplo, razonamiento_inductivo.py.

### 2. Abre la Terminal
Abre tu Terminal, Símbolo del sistema o PowerShell.

### 3. Ejecuta el Script
Navega a la carpeta donde guardaste el archivo y usa el siguiente comando:

```bash

python razonamiento_inductivo.py
# O, si usas la versión 3:
python3 razonamiento_inductivo.py

```
### Resultado (Salida)
El script imprimirá las reglas generadas y la predicción para el nuevo animal:

- Sistema de Razonamiento Inductivo -
```bash
Reglas que el sistema INDUJO a partir de los ejemplos:
|--- tiene_plumas <= 0.50
|   |--- clase: pez
|--- tiene_plumas >  0.50
|   |--- canta <= 0.50
|   |   |--- vuela_bien <= 0.50
|   |   |   |--- clase: ave_no_voladora
|   |   |--- vuela_bien >  0.50
|   |   |   |--- clase: pajaro
|   |--- canta >  0.50
|   |   |--- clase: canario

```

Clasificando un animal nuevo con características [Plumas=Sí, Canta=Sí, Vuela=Sí]. 
Conclusión probable: El animal es un 'canario'
### Conclusión
El valor fundamental del razonamiento inductivo es su capacidad para descubrir conocimiento oculto o patrones complejos en grandes volúmenes de datos sin necesidad de un experto que codifique las reglas. Donde un sistema deductivo necesita que le digamos que "si canta y vuela, es canario", este modelo lo aprende por sí mismo a partir de los ejemplos. Esto lo hace indispensable para sistemas que deben adaptarse a datos nuevos o cambiantes, como la detección de fraude o el reconocimiento de imágenes.
