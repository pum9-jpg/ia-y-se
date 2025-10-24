from collections import deque

# Un grafo no dirigido que representa un mapa simplificado de Bolivia.
# Las claves son las ciudades y los valores son las ciudades conectadas directamente.
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

def busqueda_amplitud(mapa, inicio, fin):
    """
    Encuentra el camino más corto entre dos ciudades usando BFS.
    """
    # La cola guarda tuplas de (camino_actual)
    cola = deque([[inicio]])
    # El conjunto 'visitados' nos ayuda a "Evitar estados repetidos"
    visitados = {inicio}

    while cola:
        camino = cola.popleft()
        ciudad_actual = camino[-1]

        if ciudad_actual == fin:
            return camino  # Hemos encontrado la meta

        for vecino in mapa.get(ciudad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return "No se encontró un camino."

def busqueda_profundidad(mapa, inicio, fin):
    """
    Encuentra un camino entre dos ciudades usando DFS.
    """
    # La pila guarda tuplas de (camino_actual)
    pila = [[inicio]]
    # También usamos 'visitados' para evitar bucles infinitos
    visitados = {inicio}

    while pila:
        camino = pila.pop()
        ciudad_actual = camino[-1]

        if ciudad_actual == fin:
            return camino  # Hemos encontrado la meta

        for vecino in mapa.get(ciudad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                pila.append(nuevo_camino)

    return "No se encontró un camino."

# - Definimos el problema -
ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'

print(f"Buscando ruta de '{ciudad_inicio}' a '{ciudad_destino}'.\n")

# - Ejecutar BFS -
print("- Usando Búsqueda en Amplitud (BFS) -")
camino_bfs = busqueda_amplitud(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' -> '.join(camino_bfs)}")
print(f"Número de paradas: {len(camino_bfs) - 1}\n")

# - Ejecutar DFS -
print("- Usando Búsqueda en Profundidad (DFS) -")
camino_dfs = busqueda_profundidad(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' -> '.join(camino_dfs)}")
print(f"Número de paradas: {len(camino_dfs) - 1}")