# Sistema de Razonamiento: Deductivo vs Inductivo

## Descripción General

Este proyecto implementa y compara dos enfoques fundamentales de razonamiento en Inteligencia Artificial: el razonamiento deductivo y el razonamiento inductivo. El sistema demuestra cómo ambos métodos pueden aplicarse para clasificar animales basándose en sus características, pero utilizando filosofías completamente diferentes.

## Arquitectura del Sistema

### Componentes Principales

**1. Razonamiento Deductivo (razonamiento_deductivo.py)**
- Implementa un sistema experto basado en reglas predefinidas
- Utiliza encadenamiento hacia adelante para derivar conclusiones
- Parte de conocimiento general para aplicarlo a casos específicos

**2. Razonamiento Inductivo (razonamiento_inductivo.py)**
- Implementa un sistema de aprendizaje automático
- Utiliza un árbol de decisión para aprender patrones de datos
- Parte de ejemplos específicos para generalizar reglas

**3. Sistema Principal (main.py)**
- Orquesta la ejecución de ambos enfoques
- Presenta una comparativa side-by-side

## Instalación y Requisitos

### Prerrequisitos
- Python 3.6 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

Ejecuta los siguientes comandos en tu terminal:

```bash
# Instalar las librerías necesarias
pip install scikit-learn pandas

# Verificar la instalación
python -c "import pandas; from sklearn.tree import DecisionTreeClassifier; print('Dependencias instaladas correctamente')"
```

### Estructura de Archivos
```
proyecto/
│
├── razonamiento_deductivo.py
├── razonamiento_inductivo.py
├── main.py
└── README.md
```

## Ejecución del Sistema

### Opción 1: Ejecución completa
```bash
python main.py
```

### Opción 2: Ejecución individual
```bash
# Solo razonamiento deductivo
python razonamiento_deductivo.py

# Solo razonamiento inductivo
python razonamiento_inductivo.py
```

## Base de Conocimiento y Datos

### Razonamiento Deductivo
El sistema utiliza reglas expertas predefinidas:
```python
reglas_animales = [
    {"si": ["tiene_plumas"], "entonces": "es_ave"},
    {"si": ["es_ave", "canta"], "entonces": "es_canario"},
    {"si": ["pone_huevos", "vive_en_agua"], "entonces": "es_pez"},
    {"si": ["es_ave", "vuela_bien"], "entonces": "es_pajaro"}
]
```

### Razonamiento Inductivo
El sistema aprende de un conjunto de datos de ejemplos:
```python
datos_animales = [
    {'nombre': 'paloma', 'tiene_plumas': 1, 'canta': 0, 'vuela_bien': 1, 'clase': 'pajaro'},
    {'nombre': 'canario', 'tiene_plumas': 1, 'canta': 1, 'vuela_bien': 1, 'clase': 'canario'},
    # ... más ejemplos
]
```

## Flujo de Ejecución

### Proceso Deductivo
1. Recibe hechos específicos del usuario
2. Aplica reglas generales mediante matching
3. Deriva nuevas conclusiones iterativamente
4. Presenta la conclusión final garantizada

### Proceso Inductivo
1. Entrena un modelo con datos históricos
2. Aprende reglas de clasificación automáticamente
3. Visualiza el árbol de decisiones generado
4. Clasifica nuevos casos basándose en patrones aprendidos

## Casos de Uso

### Ejemplo Deductivo
**Entrada:** `{"tiene_plumas", "canta"}`
**Proceso:** Aplicación secuencial de reglas
**Salida:** `"es_canario"`

### Ejemplo Inductivo
**Entrada:** `[1, 1, 1]` (tiene_plumas=1, canta=1, vuela_bien=1)
**Proceso:** Clasificación por árbol de decisión
**Salida:** `"canario"`

## Características Técnicas

### Sistema Deductivo
- Motor de inferencia por encadenamiento hacia adelante
- Base de conocimiento explícita y modificable
- Conclusiones lógicamente garantizadas
- Transparencia en el proceso de razonamiento

### Sistema Inductivo
- Algoritmo de árbol de decisión (CART)
- Aprendizaje automático supervisado
- Capacidad de generalización
- Visualización de reglas aprendidas

## Conclusión

Este proyecto demuestra la complementariedad entre el razonamiento deductivo e inductivo en sistemas de inteligencia artificial. El enfoque deductivo resulta invaluable cuando contamos con conocimiento experto bien establecido y necesitamos transparencia en el proceso de toma de decisiones. Por otro lado, el enfoque inductivo brinda potencia cuando disponemos de grandes volúmenes de datos y necesitamos que el sistema descubra patrones por sí mismo.

La elección entre uno u otro enfoque depende fundamentalmente del problema a resolver: el deductivo para dominios con reglas claras y conocimiento explícito, el inductivo para problemas donde los patrones deben ser descubiertos a partir de datos observados. En la práctica, muchos sistemas modernos combinan ambos enfoques, utilizando deducción para el razonamiento de alto nivel e inducción para el aprendizaje de patrones específicos.
