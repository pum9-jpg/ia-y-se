# Función de búsqueda en amplitud (BFS)
def busqueda_amplitud(mapa, inicio, fin):
    """
    Encuentra un camino entre dos ciudades usando BFS.
    """
    from collections import deque
    cola = deque([[inicio]])
    visitados = {inicio}

    while cola:
        camino = cola.popleft()
        cuidad_actual = camino[-1]

        if cuidad_actual == fin:
            return camino

        for vecino in mapa.get(cuidad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    return ["No se encontró camino"]

# Función de búsqueda en profundidad (DFS)
def busqueda_profundidad(mapa, inicio, fin):
    """
    Encuentra un camino entre dos ciudades usando DFS.
    """
    pila = [[inicio]]
    visitados = {inicio}

    while pila:
        camino = pila.pop()
        cuidad_actual = camino[-1]

        if cuidad_actual == fin:
            return camino

        for vecino in mapa.get(cuidad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                pila.append(nuevo_camino)
    return ["No se encontró camino"]

# Datos del mapa de Bolivia (simplificado)
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

# Problema
ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'

print(f"Buscando ruta de '{ciudad_inicio}' a '{ciudad_destino}'.\n")

# Ejecutar BFS
print("- Usando Búsqueda en Amplitud (BFS) -")
camino_bfs = busqueda_amplitud(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' ➔ '.join(camino_bfs)}")
print(f"Número de paradas: {len(camino_bfs) - 1}\n")

# Ejecutar DFS
print("- Usando Búsqueda en Profundidad (DFS) -")
camino_dfs = busqueda_profundidad(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' ➔ '.join(camino_dfs)}")
print(f"Número de paradas: {len(camino_dfs) - 1}")