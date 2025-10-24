# Sistema de Búsqueda de Rutas con A* vs UCS

## Descripción General

Este proyecto implementa y compara dos algoritmos de búsqueda en inteligencia artificial: **A*** (búsqueda informada) y **UCS** (Uniform Cost Search - búsqueda no informada). El sistema encuentra rutas óptimas entre ciudades bolivianas considerando distancias reales y utiliza una heurística para mejorar la eficiencia.

## Arquitectura del Sistema

### Componentes Principales

**1. Mapa Mejorado (mapa_mejorado.py)**
- Contiene distancias reales en kilómetros entre ciudades
- Incluye coordenadas geográficas para calcular heurísticas
- Define la función heurística de distancia en línea recta

**2. Búsqueda A* (busqueda_a_estrella.py)**
- Algoritmo de búsqueda informada
- Utiliza f(n) = g(n) + h(n) donde:
  - g(n): costo real desde el inicio
  - h(n): heurística (distancia estimada al destino)
- Garantiza optimalidad con heurística admisible

**3. Búsqueda UCS (busqueda_costo_uniforme.py)**
- Algoritmo de búsqueda no informada
- Similar a A* pero sin heurística (h(n) = 0)
- Expande nodos basándose solo en el costo acumulado

**4. Sistema Principal (main.py)**
- Ejecuta comparativas entre ambos algoritmos
- Analiza eficiencia en términos de nodos expandidos
- Presenta resultados detallados

## Instalación y Requisitos

### Prerrequisitos
- Python 3.6 o superior
- No se requieren librerías externas (solo math y heapq de la biblioteca estándar)

### Estructura de Archivos
```
proyecto_busqueda_informada/
│
├── mapa_mejorado.py
├── busqueda_a_estrella.py
├── busqueda_costo_uniforme.py
├── main.py
└── README.md
```

## Ejecución del Sistema

### Ejecución Completa
```bash
python main.py
```

## Conceptos Clave

### Búsqueda UCS (No Informada)
- Explora rutas basándose solo en costos reales
- Garantiza encontrar el camino óptimo
- Puede expandir muchos nodos innecesariamente

### Búsqueda A* (Informada)
- Combina costos reales con estimaciones heurísticas
- Dirige la búsqueda hacia el destino
- Expande menos nodos que UCS
- Mantiene optimalidad con heurísticas admisibles

### Heurística Utilizada
- Distancia en línea recta entre ciudades
- Siempre subestima la distancia real por carretera
- Esto la hace "admisible" (condición para optimalidad)

## Conclusión

**A* es más eficiente que UCS** porque utiliza información adicional (la heurística) para dirigir la búsqueda hacia el objetivo. Mientras UCS explora "a ciegas" expandiendo muchos nodos, A* prioriza los caminos más prometedores.

Ambos algoritmos encuentran la misma ruta óptima, pero **A* lo hace expandiendo menos nodos**, lo que lo hace más rápido y eficiente en uso de memoria. La heurística de distancia en línea recta funciona bien porque nunca sobreestima el costo real, garantizando que A* encuentre siempre el mejor camino.

En aplicaciones reales como GPS y sistemas de navegación, A* es preferible por su balance entre optimalidad y eficiencia.