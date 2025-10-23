# =======================================================
# UNIDAD 6 - PRÁCTICA 8: BÚSQUEDA EN AMPLITUD Y PROFUNDIDAD
# =======================================================

from collections import deque

# -------------------- MAPA DE BOLIVIA --------------------
mapa_bolivia = {
    'La Paz': ['Oruro', 'Beni'],
    'Oruro': ['La Paz', 'Cochabamba', 'Potosí'],
    'Cochabamba': ['Oruro', 'Santa Cruz', 'Chuquisaca', 'Beni'],
    'Potosí': ['Oruro', 'Chuquisaca', 'Tarija'],
    'Chuquisaca': ['Cochabamba', 'Potosí', 'Santa Cruz', 'Tarija'],
    'Santa Cruz': ['Cochabamba', 'Chuquisaca', 'Beni'],
    'Tarija': ['Potosí', 'Chuquisaca'],
    'Beni': ['La Paz', 'Cochabamba', 'Santa Cruz'],
    'Pando': []
}


# -------------------- BÚSQUEDA EN AMPLITUD (BFS) --------------------
def busqueda_amplitud(mapa, inicio, fin):
    """
    Encuentra el camino más corto entre dos ciudades usando BFS.
    """
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


# -------------------- BÚSQUEDA EN PROFUNDIDAD (DFS) --------------------
def busqueda_profundidad(mapa, inicio, fin):
    """
    Encuentra un camino entre dos ciudades usando DFS.
    """
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


# -------------------- EJECUCIÓN Y COMPARACIÓN --------------------
if __name__ == "__main__":
    ciudad_inicio = 'La Paz'
    ciudad_destino = 'Tarija'

    print(f"Buscando ruta de '{ciudad_inicio}' a '{ciudad_destino}'.\n")

    # ---- BFS ----
    print("→ Usando Búsqueda en Amplitud (BFS)")
    camino_bfs = busqueda_amplitud(mapa_bolivia, ciudad_inicio, ciudad_destino)
    print(f"Camino encontrado: {' ➜ '.join(camino_bfs)}")
    print(f"Número de paradas: {len(camino_bfs) - 1}\n")

    # ---- DFS ----
    print("→ Usando Búsqueda en Profundidad (DFS)")
    camino_dfs = busqueda_profundidad(mapa_bolivia, ciudad_inicio, ciudad_destino)
    print(f"Camino encontrado: {' ➜ '.join(camino_dfs)}")
    print(f"Número de paradas: {len(camino_dfs) - 1}")
