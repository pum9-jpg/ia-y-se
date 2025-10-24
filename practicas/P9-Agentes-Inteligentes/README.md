# 🗺️ Búsqueda de Rutas en el Mapa de Bolivia (BFS y DFS)

Este proyecto implementa y compara dos algoritmos fundamentales de búsqueda en grafos: **Búsqueda en Amplitud (Breadth-First Search, BFS)** y **Búsqueda en Profundidad (Depth-First Search, DFS)**, aplicados a un grafo que representa un mapa simplificado de las principales ciudades de Bolivia.

## 📝 Descripción del Código

El código está escrito en Python y consta de los siguientes componentes:

1.  **`mapa_bolivia`**: Un diccionario que define el grafo no dirigido. Las claves son las ciudades y los valores son listas de ciudades directamente conectadas (vecinos).
2.  **`busqueda_amplitud(mapa, inicio, fin)`**: Implementa el algoritmo **BFS** usando una `deque` (cola) y un conjunto `visitados`. Su objetivo es encontrar la ruta con el **menor número de paradas**.
3.  **`busqueda_profundidad(mapa, inicio, fin)`**: Implementa el algoritmo **DFS** usando una lista como `pila` (stack) y un conjunto `visitados`. Su objetivo es encontrar **alguna ruta** entre los puntos.
4.  **Ejecución Principal**: Define una `ciudad_inicio` ('La Paz') y una `ciudad_destino` ('Tarija') y ejecuta ambos algoritmos para comparar sus resultados.

## 🚀 Cómo Ejecutar

### 📋 Requisitos

* **Python 3.x**
* No se requieren librerías externas aparte de la estándar `collections.deque`.

### 💻 Pasos

1.  **Guarda el código:** Copia el código Python completo en un archivo llamado, por ejemplo, `buscador_rutas.py`.

2.  **Ejecuta desde la terminal:** Abre tu terminal o línea de comandos, navega hasta donde guardaste el archivo y ejecuta:

    ```bash
    python buscador_rutas.py
    ```

3.  **Visualiza la Salida:** La terminal mostrará los resultados de la búsqueda para ambas rutas (BFS y DFS), junto con el número de paradas.

## 📊 Conclusiones y Comparación

La ejecución del código ilustra las diferencias clave entre BFS y DFS en el contexto de la búsqueda de caminos:

| Característica | Búsqueda en Amplitud (BFS) | Búsqueda en Profundidad (DFS) |
| :--- | :--- | :--- |
| **Estructura de Datos** | Cola (`deque`) | Pila (`list.pop()`) |
| **Tipo de Camino** | **Óptimo** (Garantiza el camino más corto en número de aristas/paradas). | **Válido** (Encuentra *un* camino, pero no necesariamente el más corto). |
| **Exploración** | Explora nivel por nivel, primero a todos los vecinos, luego a los vecinos de los vecinos, etc. | Explora tan profundamente como sea posible a lo largo de una rama antes de retroceder (backtracking). |
| **En este caso...** | El camino BFS será la ruta con el **mínimo número de ciudades** intermedias. | El camino DFS puede ser mucho más largo, ya que prioriza seguir una ruta aleatoria hasta un callejón sin salida o el destino. |

**Salida Esperada (Ejemplo):**