# Sistema de Búsqueda de Rutas Óptimas en Bolivia

Este proyecto implementa y compara dos algoritmos de búsqueda para determinar la ruta más corta entre ciudades principales de Bolivia, considerando las distancias en kilómetros. Los algoritmos utilizados son:

- **Búsqueda de Costo Uniforme (UCS)**: algoritmo de búsqueda no informada que expande los nodos en orden de menor costo acumulado.
- **Algoritmo A\***: algoritmo informada que utiliza una heurística (distancia en línea recta) para priorizar la expansión de nodos, acelerando la búsqueda.

---

## Datos y Recursos

- **Mapa de Bolivia**: estructura que contiene las conexiones entre ciudades y sus costos en kilómetros.
- **Coordenadas de ciudades**: puntos en un plano (x, y) que se usan para calcular la heurística de distancia en línea recta.
- **Funciones de búsqueda**: implementaciones en Python de UCS y A\*.

---

## Funcionalidad

El programa realiza los siguientes pasos:

1. **Configura las ciudades y sus conexiones**, incluyendo los costos en km.
2. **Define las coordenadas de cada ciudad** para calcular la heurística.
3. **Ejecuta la búsqueda con UCS y A\*** para una ruta específica (ejemplo: La Paz a Tarija).
4. **Muestra los resultados**:
   - La ruta encontrada.
   - El costo total del viaje.
   - El número de nodos expandidos en cada algoritmo.

Además, el programa realiza un análisis comparativo de la eficiencia de ambos algoritmos en base a la cantidad de nodos expandidos.



## Requisitos

- Python 3.x
- Librerías estándar (`math`, `heapq`)

---

## Resultados y Conclusiones

- La búsqueda A\* suele expandir menos nodos que UCS debido a la heurística informada, haciendo la búsqueda más eficiente.
- La heurística de distancia en línea recta es efectiva para guiar la búsqueda hacia la meta.
- La implementación permite modificar fácilmente el mapa, las coordenadas y las ciudades de inicio y fin para realizar diferentes pruebas.

Este sistema es útil para estudiar y comprender el comportamiento de algoritmos de búsqueda en grafos con costos y heurísticas.
