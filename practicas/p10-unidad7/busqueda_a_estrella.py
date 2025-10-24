import heapq
from mapa import heuristica_distancia_recta

def busqueda_a_estrella(mapa, inicio, fin):
    """
    Encuentra el camino óptimo usando el algoritmo A*.
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
