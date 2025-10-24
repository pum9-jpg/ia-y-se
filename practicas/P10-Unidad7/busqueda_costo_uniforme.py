import heapq

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
