# Algoritmo de Búsqueda en Amplitud (BFS) en el Mapa de Bolivia 🇧🇴

Este script de Python implementa el algoritmo de **Búsqueda en Amplitud (Breadth-First Search o BFS)** para encontrar el camino más corto, en términos de número de saltos entre departamentos, en un mapa simplificado de Bolivia.

## 💡 Conceptos Clave

1.  **Representación del Mapa (`mapa_bolivia`)**: El conocimiento del mundo (el mapa) se modela como un **grafo no dirigido** usando un diccionario.
    * **Nodos (Estados)**: Los departamentos (ej. 'La Paz', 'Oruro').
    * **Aristas (Conexiones)**: La lista de departamentos vecinos que comparten frontera.
2.  **BFS (`busqueda_amplitud`)**: Es un **algoritmo de búsqueda no informado** (ciego) que explora el grafo nivel por nivel.
    * **Cola (`deque`)**: Estructura **FIFO (First-In, First-Out)** que asegura que se expandan primero los caminos más cortos (por eso siempre encuentra el camino mínimo).
    * **Conjunto `visitados`**: Mecanismo para **evitar ciclos** y no procesar un departamento más de una vez, optimizando la búsqueda.

---

## 🚀 ¿Cómo funciona el Algoritmo BFS?

La función `busqueda_amplitud` simula un viaje de exploración:

1.  **Inicio**: Comienza en el departamento de `inicio` y lo pone en la cola como el primer camino `['inicio']`.
2.  **Exploración por Nivel**: En cada paso, saca el camino más antiguo de la izquierda de la cola (`cola.popleft()`).
3.  **Expansión**: Revisa todos los **vecinos** del último departamento en ese camino.
4.  **Generación de Nuevos Caminos**: Por cada vecino **no visitado**, crea un *nuevo* camino más largo (ej. `['La Paz', 'Oruro']`) y lo añade al **final de la cola**.
5.  **Meta**: El proceso se repite. Como los caminos más cortos se procesan primero, **el primer camino que llega al destino (`fin`) es garantizado como el más corto**.

---

## ⚙️ Estructura del Código

```python
# BASE DE CONOCIMIENTO (El Grafo)
mapa_bolivia = {
    'La Paz': ['Oruro', 'Beni'],
    # ...
    'Pando': []
}
# ...
# FUNCIÓN DE BÚSQUEDA (El Motor de Búsqueda)
def busqueda_amplitud(mapa, inicio, fin):
    # ... Lógica BFS usando deque y set ...
```
### Ejecución Rápida
Para ejecutar la búsqueda, necesitas copiar el código del mapa y la función, y luego hacer una llamada al final.

### 1. Guarda el Código
Copia el diccionario mapa_bolivia y la función busqueda_amplitud en un archivo llamado, por ejemplo, bfs_bolivia.py.

### 2. Añade la Prueba
Añade las siguientes líneas al final del archivo para ejecutar una prueba:

``` bash
Python

# --- PRUEBA DE USO ---
inicio_ruta = 'La Paz'
fin_ruta = 'Tarija'
camino_mas_corto = busqueda_amplitud(mapa_bolivia, inicio_ruta, fin_ruta)

print(f"Ruta desde {inicio_ruta} hasta {fin_ruta}:")
print(camino_mas_corto)

```

### 3. Ejecuta el Script
Abre tu Terminal y ejecuta:

```bash

python bfs_bolivia.py
# O, si usas la versión 3:
python3 bfs_bolivia.py

```
### 4. Salida Esperada
Para la ruta 'La Paz' a 'Tarija', el camino más corto (en 3 saltos) se mostrará así:

Ruta desde La Paz hasta Tarija:
['La Paz', 'Oruro', 'Potosi', 'Tarija']

``` 
### Conclusión 
El algoritmo de Búsqueda en Amplitud (BFS) es fundamental en la Inteligencia Artificial y la informática porque ofrece una solución óptima para problemas de camino más corto donde todas las aristas tienen el mismo "costo" (en este caso, un salto de un departamento a otro). Su uso de la cola FIFO garantiza que explore todas las opciones a un nivel N antes de pasar al nivel N+1. Esto asegura que el primer camino encontrado hacia el objetivo sea, por definición, el que tiene la menor cantidad de pasos.
