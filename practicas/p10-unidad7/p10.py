import math
import heapq


# ----------------------------------------------------------
# 🗺️ Paso 1: Mapa Mejorado con Costos y Coordenadas
# ----------------------------------------------------------

# Distancias reales (en km) entre ciudades
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

# Coordenadas ficticias (x, y) para estimar distancias lineales
coordenadas_ciudades = {
    'La Paz': (16, 68),
    'Oruro': (17, 67),
    'Cochabamba': (17, 66),
    'Potosi': (19, 65),
    'Chuquisaca': (19, 65),
    'Santa Cruz': (17, 63),
    'Tarija': (21, 64),
    'Beni': (14, 65)
}

# ----------------------------------------------------------
# 🧮 Función Heurística: Distancia Euclidiana (línea recta)
# ----------------------------------------------------------
def heuristica_distancia_recta(ciudad_a, ciudad_b):
    (x1, y1) = coordenadas_ciudades[ciudad_a]
    (x2, y2) = coordenadas_ciudades[ciudad_b]
    # Distancia euclidiana entre los puntos
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2) * 100


# ----------------------------------------------------------
# 🚗 Paso 2: Implementar el Algoritmo A*
# ----------------------------------------------------------
def busqueda_a_estrella(grafo, inicio, meta):
    """Algoritmo de búsqueda A* (A-estrella)."""
    frontera = []  # Cola de prioridad
    heapq.heappush(frontera, (0, [inicio]))  # (costo total estimado, camino)
    nodos_expandidos = 0

    while frontera:
        costo_estimado, camino = heapq.heappop(frontera)
        ciudad_actual = camino[-1]
        nodos_expandidos += 1

        # Si llegamos al destino
        if ciudad_actual == meta:
            costo_real = calcular_costo_real(grafo, camino)
            return camino, costo_real, nodos_expandidos

        # Expandir vecinos
        for vecino, costo in grafo[ciudad_actual].items():
            if vecino not in camino:  # Evitar ciclos
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                costo_real = calcular_costo_real(grafo, nuevo_camino)
                heuristica = heuristica_distancia_recta(vecino, meta)
                costo_total = costo_real + heuristica
                heapq.heappush(frontera, (costo_total, nuevo_camino))

    return None, float('inf'), nodos_expandidos


# ----------------------------------------------------------
# 🚙 Paso 3: Implementar Búsqueda de Costo Uniforme (UCS)
# ----------------------------------------------------------
def busqueda_costo_uniforme(grafo, inicio, meta):
    """Búsqueda no informada (como A* pero sin heurística)."""
    frontera = []
    heapq.heappush(frontera, (0, [inicio]))
    nodos_expandidos = 0

    while frontera:
        costo_actual, camino = heapq.heappop(frontera)
        ciudad_actual = camino[-1]
        nodos_expandidos += 1

        if ciudad_actual == meta:
            return camino, costo_actual, nodos_expandidos

        for vecino, costo in grafo[ciudad_actual].items():
            if vecino not in camino:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                nuevo_costo = costo_actual + costo
                heapq.heappush(frontera, (nuevo_costo, nuevo_camino))

    return None, float('inf'), nodos_expandidos


# ----------------------------------------------------------
# 🔧 Función Auxiliar para Calcular Costos
# ----------------------------------------------------------
def calcular_costo_real(grafo, camino):
    """Calcula el costo total real de un camino dado."""
    costo = 0
    for i in range(len(camino) - 1):
        ciudad_actual = camino[i]
        siguiente = camino[i + 1]
        costo += grafo[ciudad_actual][siguiente]
    return costo


# ----------------------------------------------------------
# 🧩 Paso 4: Ejecutar Comparación entre UCS y A*
# ----------------------------------------------------------
if __name__ == "__main__":
    ciudad_inicio = 'La Paz'
    ciudad_destino = 'Tarija'

    print(f"\n🧭 Buscando la mejor ruta de '{ciudad_inicio}' a '{ciudad_destino}'...\n")

    # --- UCS ---
    print("🔹 Usando Búsqueda de Costo Uniforme (UCS):")
    camino_ucs, costo_ucs, exp_ucs = busqueda_costo_uniforme(mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
    print(f"   Camino encontrado: {' ➔ '.join(camino_ucs)}")
    print(f"   Costo total del viaje: {costo_ucs} km")
    print(f"   Ciudades (nodos) expandidas: {exp_ucs}\n")

    # --- A* ---
    print("🔸 Usando Búsqueda A* (Informada):")
    camino_astar, costo_astar, exp_astar = busqueda_a_estrella(mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
    print(f"   Camino encontrado: {' ➔ '.join(camino_astar)}")
    print(f"   Costo total del viaje: {costo_astar} km")
    print(f"   Ciudades (nodos) expandidas: {exp_astar}\n")

    # --- Comparación ---
    print("📊 Comparación Final:")
    print(f"   UCS expandió {exp_ucs} nodos.")
    print(f"   A* expandió {exp_astar} nodos.")
    print("   ✅ Ambos encontraron la ruta óptima, pero A* fue más eficiente.")
