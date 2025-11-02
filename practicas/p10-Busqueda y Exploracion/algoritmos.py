# -*- coding: utf-8 -*-
import heapq

def reconstruir_camino(padre, inicio, fin):
    camino = [fin]
    actual = fin
    while actual != inicio:
        actual = padre[actual]
        camino.append(actual)
    camino.reverse()
    return camino

# ----------------------------
#        A* (A-estrella)
# ----------------------------
def a_estrella(grafo, h, inicio, fin):
    """
    Retorna (camino, costo_total, nodos_expandidos)
    f(n) = g(n) + h(n), donde g es el costo real acumulado.
    """
    frontera = []  # priority queue por f(n)
    heapq.heappush(frontera, (0, inicio))
    mejor_g = {inicio: 0}
    padre = {}
    visitados = set()
    expandidos = 0

    while frontera:
        f_actual, nodo_actual = heapq.heappop(frontera)

        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)
        expandidos += 1

        if nodo_actual == fin:
            camino = reconstruir_camino(padre, inicio, fin) if fin in padre or fin == inicio else [inicio]
            return camino, mejor_g[fin], expandidos

        for vecino, costo in grafo[nodo_actual].items():
            g_nuevo = mejor_g[nodo_actual] + costo
            if vecino not in mejor_g or g_nuevo < mejor_g[vecino]:
                mejor_g[vecino] = g_nuevo
                padre[vecino] = nodo_actual
                f_nuevo = g_nuevo + h(vecino)
                heapq.heappush(frontera, (f_nuevo, vecino))

    return None, float("inf"), expandidos


# -----------------------------------------
#  Costo Uniforme (UCS)  ~ A* con h(n)=0
# -----------------------------------------
def costo_uniforme(grafo, inicio, fin):
    """
    Retorna (camino, costo_total, nodos_expandidos).
    Equivalente a Dijkstra con todos los costos no negativos.
    """
    frontera = []
    heapq.heappush(frontera, (0, inicio))
    mejor_g = {inicio: 0}
    padre = {}
    visitados = set()
    expandidos = 0

    while frontera:
        g_actual, nodo_actual = heapq.heappop(frontera)

        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)
        expandidos += 1

        if nodo_actual == fin:
            camino = reconstruir_camino(padre, inicio, fin) if fin in padre or fin == inicio else [inicio]
            return camino, g_actual, expandidos

        for vecino, costo in grafo[nodo_actual].items():
            g_nuevo = g_actual + costo
            if vecino not in mejor_g or g_nuevo < mejor_g[vecino]:
                mejor_g[vecino] = g_nuevo
                padre[vecino] = nodo_actual
                heapq.heappush(frontera, (g_nuevo, vecino))

    return None, float("inf"), expandidos
