import heapq
from mapa_mejorado_heuristica import mapa_bolivia_mejorado, heuristica_distancia_recta

def busqueda_a_estrella(mapa, inicio, destino):
    frontera = [(0, inicio, [inicio])]
    costos = {inicio: 0}
    nodos_expandidos = 0

    while frontera:
        (costo_estimado, ciudad_actual, camino) = heapq.heappop(frontera)
        nodos_expandidos += 1

        if ciudad_actual == destino:
            return camino, costos[ciudad_actual], nodos_expandidos

        for vecino, costo in mapa[ciudad_actual].items():
            nuevo_costo = costos[ciudad_actual] + costo
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica_distancia_recta(vecino, destino)
                heapq.heappush(frontera, (prioridad, vecino, camino + [vecino]))

    return None, float('inf'), nodos_expandidos
