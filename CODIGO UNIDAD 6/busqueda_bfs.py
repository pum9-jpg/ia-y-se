# busqueda_bfs.py
from collections import deque

def busqueda_amplitud(grafo, inicio, meta):
    """Búsqueda en amplitud (BFS): explora por niveles y encuentra el camino más corto."""
    visitados = set()
    cola = deque([[inicio]])

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == meta:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None
