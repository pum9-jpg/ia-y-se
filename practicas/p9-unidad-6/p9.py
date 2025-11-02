from collections import deque


# ----------------------------------------------------------
# 🗺️ Paso 1: Representación del mapa de Bolivia (grafo)
# ----------------------------------------------------------
mapa_bolivia = {
    'La Paz': ['Oruro', 'Beni'],
    'Oruro': ['La Paz', 'Cochabamba', 'Potosi'],
    'Cochabamba': ['Oruro', 'Santa Cruz', 'Chuquisaca', 'Beni'],
    'Potosi': ['Oruro', 'Chuquisaca', 'Tarija'],
    'Chuquisaca': ['Cochabamba', 'Potosi', 'Santa Cruz', 'Tarija'],
    'Santa Cruz': ['Cochabamba', 'Chuquisaca', 'Beni'],
    'Tarija': ['Potosi', 'Chuquisaca'],
    'Beni': ['La Paz', 'Cochabamba', 'Santa Cruz'],
    'Pando': []  # Ciudad aislada
}

# ----------------------------------------------------------
# 🚀 Paso 2: Implementar Búsqueda en Amplitud (BFS)
# ----------------------------------------------------------
def busqueda_amplitud(grafo, inicio, meta):
    """Explora el mapa por capas, garantizando la ruta más corta (en número de pasos)."""
    cola = deque([[inicio]])  # Cola de caminos
    visitados = set()

    while cola:
        camino = cola.popleft()  # Extrae el primer camino en la cola
        ciudad_actual = camino[-1]

        if ciudad_actual == meta:
            return camino  # ¡Meta encontrada!

        if ciudad_actual not in visitados:
            visitados.add(ciudad_actual)
            for vecino in grafo[ciudad_actual]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None  # Si no hay camino


# ----------------------------------------------------------
# 🌄 Paso 3: Implementar Búsqueda en Profundidad (DFS)
# ----------------------------------------------------------
def busqueda_profundidad(grafo, inicio, meta):
    """Explora una ruta hasta el final antes de retroceder (no garantiza el camino más corto)."""
    pila = [[inicio]]  # Pila de caminos
    visitados = set()

    while pila:
        camino = pila.pop()  # Extrae el último camino
        ciudad_actual = camino[-1]

        if ciudad_actual == meta:
            return camino  # ¡Meta encontrada!

        if ciudad_actual not in visitados:
            visitados.add(ciudad_actual)
            for vecino in grafo[ciudad_actual]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                pila.append(nuevo_camino)

    return None


# ----------------------------------------------------------
# 🧩 Paso 4: Ejecutar y Comparar las Simulaciones
# ----------------------------------------------------------
if __name__ == "__main__":
    ciudad_inicio = 'La Paz'
    ciudad_destino = 'Tarija'

    print(f"\n🧭 Buscando ruta de '{ciudad_inicio}' a '{ciudad_destino}'...\n")

    # --- Búsqueda en Amplitud (BFS) ---
    print("🔹 Usando Búsqueda en Amplitud (BFS):")
    camino_bfs = busqueda_amplitud(mapa_bolivia, ciudad_inicio, ciudad_destino)
    if camino_bfs:
        print(f"   Camino encontrado: {' ➔ '.join(camino_bfs)}")
        print(f"   Número de paradas: {len(camino_bfs) - 1}\n")
    else:
        print("   ❌ No se encontró una ruta.\n")

    # --- Búsqueda en Profundidad (DFS) ---
    print("🔸 Usando Búsqueda en Profundidad (DFS):")
    camino_dfs = busqueda_profundidad(mapa_bolivia, ciudad_inicio, ciudad_destino)
    if camino_dfs:
        print(f"   Camino encontrado: {' ➔ '.join(camino_dfs)}")
        print(f"   Número de paradas: {len(camino_dfs) - 1}\n")
    else:
        print("   ❌ No se encontró una ruta.\n")


