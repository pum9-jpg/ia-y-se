# ===============================================
# UNIDAD 7 - PRÁCTICA 10
# PARTE 2: Implementar la Búsqueda A* (A-estrella)
# ===============================================

from PRIMERA_PARTE_UNIDAD7 import mapa_bolivia_mejorado, heuristica_distancia_recta
import heapq


def busqueda_a_estrella(mapa, inicio, fin):
    """
    Encuentra el camino óptimo usando el algoritmo A*.
    f(n) = g(n) + h(n)
    - g(n): costo real del camino desde el inicio hasta n
    - h(n): costo estimado (heurístico) desde n hasta el destino
    """

    # Cola de prioridad: [(f(n), g(n), camino_actual)]
    cola_prioridad = [(0, 0, [inicio])]
    visitados = set()
    nodos_expandidos = 0

    while cola_prioridad:
        _, costo_g, camino = heapq.heappop(cola_prioridad)
        ciudad_actual = camino[-1]
        nodos_expandidos += 1

        # Evita volver a visitar nodos
        if ciudad_actual in visitados:
            continue

        visitados.add(ciudad_actual)

        # Si llegamos al destino, devolvemos el camino y el costo
        if ciudad_actual == fin:
            return camino, costo_g, nodos_expandidos

        # Explora los vecinos
        for vecino, distancia in mapa[ciudad_actual].items():
            nuevo_costo_g = costo_g + distancia
            costo_h = heuristica_distancia_recta(vecino, fin)
            costo_f = nuevo_costo_g + costo_h

            nuevo_camino = list(camino)
            nuevo_camino.append(vecino)

            heapq.heappush(cola_prioridad, (costo_f, nuevo_costo_g, nuevo_camino))

    return "No se encontró un camino.", 0, nodos_expandidos


# ======================================================
# PRUEBA DE EJECUCIÓN
# ======================================================
if __name__ == "__main__":
    print("=== BÚSQUEDA A* ENTRE CIUDADES DE BOLIVIA ===")
    inicio = "La Paz"
    destino = "Santa Cruz"

    camino, costo, expandidos = busqueda_a_estrella(mapa_bolivia_mejorado, inicio, destino)

    print(f"\nCamino encontrado: {' -> '.join(camino)}")
    print(f"Costo total del recorrido: {costo} km")
    print(f"Nodos expandidos: {expandidos}")
