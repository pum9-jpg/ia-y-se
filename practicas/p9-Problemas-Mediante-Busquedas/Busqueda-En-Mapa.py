# ====== Representación del mapa (grafo) ======
mapa_bolivia = {
    'La Paz': ['Oruro', 'Beni'],
    'Oruro': ['La Paz', 'Cochabamba', 'Potosi'],
    'Cochabamba': ['Oruro', 'Santa Cruz', 'Chuquisaca', 'Beni'],
    'Potosi': ['Oruro', 'Chuquisaca', 'Tarija'],
    'Chuquisaca': ['Cochabamba', 'Potosi', 'Santa Cruz', 'Tarija'],
    'Santa Cruz': ['Cochabamba', 'Chuquisaca', 'Beni'],
    'Tarija': ['Potosi', 'Chuquisaca'],
    'Beni': ['La Paz', 'Cochabamba', 'Santa Cruz'],
    'Pando': []  # Pando está aislado en este mapa simplificado
}

# ====== Búsqueda en Amplitud (BFS) ======
from collections import deque

def busqueda_amplitud(grafo, inicio, meta):
    cola = deque([[inicio]])  # cola con el camino actual
    visitados = set()

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]
        if nodo == meta:
            return camino
        elif nodo not in visitados:
            for vecino in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
            visitados.add(nodo)
    return None

# ====== Búsqueda en Profundidad (DFS) ======
def busqueda_profundidad(grafo, inicio, meta, camino=None):
    if camino is None:
        camino = [inicio]
    if inicio == meta:
        return camino
    for vecino in grafo.get(inicio, []):
        if vecino not in camino:
            nuevo_camino = busqueda_profundidad(grafo, vecino, meta, camino + [vecino])
            if nuevo_camino:
                return nuevo_camino
    return None

# ====== Ejecución y comparación ======
ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'

print(f"Buscando ruta de '{ciudad_inicio}' a '{ciudad_destino}'.\n")

print("- Usando Búsqueda en Amplitud (BFS) -")
camino_bfs = busqueda_amplitud(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' ➔ '.join(camino_bfs)}")
print(f"Número de paradas: {len(camino_bfs) - 1}\n")

print("- Usando Búsqueda en Profundidad (DFS) -")
camino_dfs = busqueda_profundidad(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' ➔ '.join(camino_dfs)}")
print(f"Número de paradas: {len(camino_dfs) - 1}")
