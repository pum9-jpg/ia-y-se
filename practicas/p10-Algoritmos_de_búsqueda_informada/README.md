# Unidad 7 — Ejercicio 1: Algoritmo de Búsqueda A*

## Descripción
El algoritmo **A\*** combina la búsqueda por costo uniforme y heurística para encontrar la ruta más eficiente entre dos puntos.  
Usa una función de evaluación `f(n) = g(n) + h(n)` donde:  
- `g(n)` es el costo real acumulado.  
- `h(n)` es una estimación heurística del costo restante.  
Es ampliamente utilizado en inteligencia artificial para resolución de problemas de rutas, planificación y juegos.

---

## Código (copiado del libro)
```python
from queue import PriorityQueue

def a_estrella(grafo, inicio, objetivo, heuristica):
    cola = PriorityQueue()
    cola.put((0, [inicio]))
    visitados = set()

    while not cola.empty():
        (costo, camino) = cola.get()
        nodo = camino[-1]
        if nodo == objetivo:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, peso in grafo.get(nodo, []):
                nuevo_costo = costo + peso + heuristica.get(vecino, 0)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.put((nuevo_costo, nuevo_camino))
    return None

# Grafo de ejemplo
grafo = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# Heurísticas estimadas
heuristica = {'A': 4, 'B': 2, 'C': 4, 'D': 4, 'E': 1, 'F': 0}

camino = a_estrella(grafo, 'A', 'F', heuristica)
print("Camino óptimo encontrado por A*:", camino)
```

# Ejemplo de salida esperada
Camino óptimo encontrado por A*: ['A', 'B', 'E', 'F']

# Observaciones
- A* combina exploración heurística y costo acumulado, priorizando rutas prometedoras.

- Si la heurística es admisible (nunca sobreestima), A* garantiza encontrar la ruta óptima.

- Se usa en sistemas de navegación, videojuegos y planeación autónoma.

# Conclusión
El algoritmo A* es un método eficiente y equilibrado para la búsqueda óptima en grafos y su uso de heurísticas lo hace más rápido y preciso que las búsquedas no informadas.