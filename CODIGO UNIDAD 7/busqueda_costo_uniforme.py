import heapq
from mapa_mejorado_heuristica import mapa_bolivia_mejorado

def busqueda_costo_uniforme(mapa, inicio, destino):
    frontera = [(0, inicio, [inicio])]
    costos = {inicio: 0}
    nodos_expandidos = 0

    while frontera:
        (costo, ciudad_actual, camino) = heapq.heappop(frontera)
        nodos_expandidos += 1

        if ciudad_actual == destino:
            return camino, costo, nodos_expandidos

        for vecino, costo_vecino in mapa[ciudad_actual].items():
            nuevo_costo = costo + costo_vecino
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                heapq.heappush(frontera, (nuevo_costo, vecino, camino + [vecino]))

    return None, float('inf'), nodos_expandidos
