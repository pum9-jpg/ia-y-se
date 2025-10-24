from collections import deque

def bfs(grafo, inicio, objetivo):
    visitados = set()
    cola = deque([[inicio]])

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == objetivo:
            return camino

        if nodo not in visitados:
            for vecino in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
            visitados.add(nodo)
    return None

# Ejemplo de grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Camino más corto de A a F:", bfs(grafo, 'A', 'F'))