import math
import heapq

# 1. Mapa con costos en km
mapa_bolivia_mejorado = {
    'La Paz': {'Oruro': 230, 'Beni': 1080},
    'Oruro': {'La Paz': 230, 'Cochabamba': 210, 'Potosí': 330},
    'Cochabamba': {'Oruro': 210, 'Santa Cruz': 400, 'Sucre': 360, 'Beni': 900},
    'Potosí': {'Oruro': 330, 'Chuquisaca': 160, 'Tarija': 345},
    'Chuquisaca': {'Potosí': 160, 'Tarija': 340, 'Cochabamba': 360},
    'Tarija': {'Potosí': 345, 'Chuquisaca': 340},
    'Santa Cruz': {'Cochabamba': 470, 'Chuquisaca': 450, 'Beni': 280},
    'Beni': {'La Paz': 1080, 'Cochabamba': 900, 'Santa Cruz': 280},
    'Sucre': {'Cochabamba': 360, 'Chuquisaca': 100, 'Potosí': 150}
}

# 2. Coordenadas para heurística
coordenadas_ciudades = {
    'La Paz': (76, 69),
    'Oruro': (61, 67),
    'Cochabamba': (17, 66),
    'Sucre': (63, 64),
    'Chuquisaca': (65, 63),
    'Santa Cruz': (17, 60),
    'Tarija': (21, 64),
    'Beni': (14, 68),
    'Potosí': (62, 65)
}

# 3. Función heurística (distancia en línea recta)
def heuristica_distancia_recta(ciudad_a, ciudad_b):
    (x1, y1) = coordenadas_ciudades[ciudad_a]
    (x2, y2) = coordenadas_ciudades[ciudad_b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) * 100

# 4. Búsqueda de costo uniforme (UCS)
def busqueda_costo_uniforme(mapa, inicio, fin):
    """Algoritmo de Búsqueda de Costo Uniforme (UCS)."""
    cola_prioridad = [(0, [inicio])]  # (costo, camino)
    visitados = set()
    nodos_expandidos = 0

    while cola_prioridad:
        costo, camino = heapq.heappop(cola_prioridad)
        ciudad_actual = camino[-1]
        nodos_expandidos += 1

        if ciudad_actual in visitados:
            continue
        visitados.add(ciudad_actual)

        if ciudad_actual == fin:
            return camino, costo, nodos_expandidos

        for vecino, distancia in mapa[ciudad_actual].items():
            if vecino not in visitados:
                nuevo_costo = costo + distancia
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                heapq.heappush(cola_prioridad, (nuevo_costo, nuevo_camino))

    return "No se encontró un camino.", 0, nodos_expandidos

# 5. Búsqueda A* (informada)
def busqueda_a_estrella(mapa, inicio, fin):
    """
    Encuentra el camino óptimo usando A*.
    """
    # La cola de prioridad guarda tuplas de (f(n), g(n), camino_actual)
    cola_prioridad = [(0, 0, [inicio])]
    visitados = set()
    nodos_expandidos = 0

    while cola_prioridad:
        costo_f, costo_g, camino = heapq.heappop(cola_prioridad)
        ciudad_actual = camino[-1]
        nodos_expandidos += 1

        if ciudad_actual in visitados:
            continue
        visitados.add(ciudad_actual)

        if ciudad_actual == fin:
            return camino, costo_g, nodos_expandidos  # Éxito

        for vecino, distancia in mapa[ciudad_actual].items():
            if vecino not in visitados:
                nuevo_costo_g = costo_g + distancia
                costo_h = heuristica_distancia_recta(vecino, fin)
                costo_f = nuevo_costo_g + costo_h
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                heapq.heappush(cola_prioridad, (costo_f, nuevo_costo_g, nuevo_camino))

    return "No se encontró un camino.", 0, nodos_expandidos

# --- Ejemplo de ejecución ---
ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'

print(f"Buscando la ruta más corta de '{ciudad_inicio}' a '{ciudad_destino}'. \n")

# Búsqueda de Costo Uniforme (UCS)
print("-     Usando Búsqueda de Costo Uniforme (UCS) - ")
camino_ucs, costo_ucs, expandidos_ucs = busqueda_costo_uniforme(mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' → '.join(camino_ucs)}")
print(f"Costo total del viaje: {costo_ucs} km")
print(f"Ciudades (nodos) expandidas: {expandidos_ucs}\n")

# Búsqueda A*
print("-     Usando Búsqueda A* (Informada) - ")
camino_a_estrella, costo_a_estrella, expandidos_a_estrella = busqueda_a_estrella(mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' → '.join(camino_a_estrella)}")
print(f"Costo total del viaje: {costo_a_estrella} km")
print(f"Ciudades (nodos) expandidas: {expandidos_a_estrella}\n")

# Análisis
print("—   Análisis de Resultados —  ")
if expandidos_a_estrella < expandidos_ucs:
    print(f"A* fue más eficiente: expandió {expandidos_ucs - expandidos_a_estrella} nodos menos que UCS para encontrar la misma ruta óptima.")
else:
    print("Ambos algoritmos fueron igualmente eficientes.")