mapa_bolivia = {
    'La Paz': ['Oruro', 'Beni'],
    'Oruro': ['La Paz', 'Cochabamba', 'Potosi'],
    'Cochabamba': ['Oruro', 'Santa Cruz', 'Chuquisaca', 'Beni'],
    'Potosi': ['Oruro', 'Chuquisaca', 'Tarija'],
    'Chuquisaca': ['Cochabamba', 'Potosi', 'Santa Cruz', 'Tarija'],
    'Santa Cruz': ['Cochabamba', 'Chuquisaca', 'Beni'],
    'Tarija': ['Potosi', 'Chuquisaca'],
    'Beni': ['La Paz', 'Cochabamba', 'Santa Cruz'],
    'Pando': []
}

from collections import deque

def busqueda_amplitud(mapa, inicio, fin):
    cola = deque([[inicio]])
    visitados = {inicio}

    while cola:
        camino = cola.popleft()
        ciudad_actual = camino[-1]

        if ciudad_actual == fin:
            return camino
        
        for vecino in mapa.get(ciudad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    return "No se encontró un camino."

def busqueda_profundidad(mapa, inicio, fin):
    pila = [[inicio]]
    visitados = {inicio}

    while pila:
        camino = pila.pop()
        ciudad_actual = camino[-1]

        if ciudad_actual == fin:
            return camino
        
        for vecino in mapa.get(ciudad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                pila.append(nuevo_camino)
    return "No se encontró un camino."

ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'

print(f"Buscando ruta de '{ciudad_inicio}' a '{ciudad_destino}'. \n")

print("--- Usando Busqueda en Amplitud (BFS) ---")
camino_bfs = busqueda_amplitud(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {'->'.join(camino_bfs)}")
print(f"Numero de paradas: {len(camino_bfs) - 1}\n")

print("--- Usando Busqueda en Profundidad (DFS) ---")
camino_dfs = busqueda_profundidad(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {'->'.join(camino_dfs)}")
print(f"Numero de paradas: {len(camino_dfs) - 1}")