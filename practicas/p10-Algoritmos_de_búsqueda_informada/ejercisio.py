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
