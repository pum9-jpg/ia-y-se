from collections import deque

# --- BÚSQUEDA EN AMPLITUD (BFS) ---
def busqueda_amplitud(grafo, inicio, fin):
    visitados = set()
    cola = deque([[inicio]])

    while cola:
        camino = cola.popleft()
        ciudad_actual = camino[-1]

        if ciudad_actual == fin:
            return camino

        if ciudad_actual not in visitados:
            visitados.add(ciudad_actual)
            for vecino in grafo[ciudad_actual]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None


# --- BÚSQUEDA EN PROFUNDIDAD (DFS) ---
def busqueda_profundidad(grafo, inicio, fin):
    visitados = set()
    pila = [[inicio]]

    while pila:
        camino = pila.pop()
        ciudad_actual = camino[-1]

        if ciudad_actual == fin:
            return camino

        if ciudad_actual not in visitados:
            visitados.add(ciudad_actual)
            for vecino in grafo[ciudad_actual]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                pila.append(nuevo_camino)

    return None
