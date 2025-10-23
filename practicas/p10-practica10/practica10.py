import math
import heapq

# 1. El mapa ahora incluye costos (distancias en km) en las conexiones.
mapa_bolivia_mejorado = {
    'La Paz': {'Oruro': 230, 'Beni': 1060},
    'Oruro': {'La Paz': 230, 'Cochabamba': 210, 'Potosi': 330},
    'Cochabamba': {'Oruro': 210, 'Santa Cruz': 470, 'Chuquisaca': 360, 'Beni': 900},
    'Potosi': {'Oruro': 330, 'Chuquisaca': 160, 'Tarija': 345},
    'Chuquisaca': {'Cochabamba': 360, 'Potosi': 160, 'Santa Cruz': 490, 'Tarija': 480},
    'Santa Cruz': {'Cochabamba': 470, 'Chuquisaca': 490, 'Beni': 280},
    'Tarija': {'Potosi': 345, 'Chuquisaca': 480},
    'Beni': {'La Paz': 1060, 'Cochabamba': 900, 'Santa Cruz': 280}
}

# 2. Coordenadas (x, y) aproximadas para cada ciudad para la heurística.
coordenadas_ciudades = {
    'La Paz': (16, 66), 
    'Oruro': (17, 67), 
    'Cochabamba': (17, 66), 
    'Potosi': (19, 65), 
    'Chuquisaca': (19, 65), 
    'Santa Cruz': (17, 63),
    'Tarija': (21, 64), 
    'Beni': (14, 65)
}

# 3. La Función Heurística
def heuristica_distancia_recta(ciudad_a, ciudad_b):
    """Calcula la distancia Euclidiana (en línea recta) entre dos ciudades."""
    (x1, y1) = coordenadas_ciudades[ciudad_a]
    (x2, y2) = coordenadas_ciudades[ciudad_b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2) * 100  # Multiplicador para escalar

# Paso 2: Implementar la Búsqueda A* (A-estrella)
def busqueda_a_estrella(mapa, inicio, fin):
    """
    Encuentra el camino óptimo usando el algoritmo A*.
    """
    # La cola de prioridad guarda tuplas de (f(n), g(n), camino_actual)
    # g(n) es el costo para llegar, f(n) es g(n) + h(n)
    cola_prioridad = [(0, 0, [inicio])]
    visitados = set()
    nodos_expandidos = 0

    while cola_prioridad:
        _, costo_g, camino = heapq.heappop(cola_prioridad)
        ciudad_actual = camino[-1]

        nodos_expandidos += 1

        if ciudad_actual in visitados:
            continue

        visitados.add(ciudad_actual)

        if ciudad_actual == fin:
            return camino, costo_g, nodos_expandidos  # ¡Éxito!

        for vecino, distancia in mapa[ciudad_actual].items():
            if vecino not in visitados:
                nuevo_costo_g = costo_g + distancia
                costo_h = heuristica_distancia_recta(vecino, fin)
                costo_f = nuevo_costo_g + costo_h

                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                heapq.heappush(cola_prioridad, (costo_f, nuevo_costo_g, nuevo_camino))

    return "No se encontró un camino.", 0, nodos_expandidos

# Paso 3: Búsqueda de Costo Uniforme (UCS)
def busqueda_costo_uniforme(mapa, inicio, fin):
    # En UCS, la prioridad es simplemente el costo acumulado g(n)
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

# Paso 4: Ejecutar y Analizar los Resultados
ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'

print(f"Buscando la ruta más corta de '{ciudad_inicio}' a '{ciudad_destino}'. \n")

# - Ejecutar Búsqueda de Costo Uniforme (No Informada) -
print("- Usando Búsqueda de Costo Uniforme (UCS) - ")
camino_ucs, costo_ucs, expandidos_ucs = busqueda_costo_uniforme(mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' → '.join(camino_ucs)}")
print(f"Costo total del viaje: {costo_ucs} km")
print(f"Ciudades (nodos) expandidas: {expandidos_ucs}\n")

# - Ejecutar Búsqueda A* (Informada) -
print("- Usando Búsqueda A* (Informada) - ")
camino_a_estrella, costo_a_estrella, expandidos_a_estrella = busqueda_a_estrella(mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' → '.join(camino_a_estrella)}")
print(f"Costo total del viaje: {costo_a_estrella} km")
print(f"Ciudades (nodos) expandidas: {expandidos_a_estrella}\n")

# - Análisis -
print("- Análisis de Resultados - ")
if expandidos_a_estrella < expandidos_ucs:
    print(f"A* fue más eficiente: expandió {expandidos_ucs - expandidos_a_estrella} nodos menos que UCS para encontrar la misma ruta óptima.")
else:
    print("Ambos algoritmos fueron igualmente eficientes.")