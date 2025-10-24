# ===============================================
# UNIDAD 7 - PRÁCTICA 10
# PARTE 3: Comparar con una Búsqueda No Informada (Costo Uniforme - UCS)
# ===============================================

from PRIMERA_PARTE_UNIDAD7 import mapa_bolivia_mejorado
import heapq


def busqueda_costo_uniforme(mapa, inicio, fin):
    """
    Implementa la Búsqueda de Costo Uniforme (Uniform Cost Search - UCS).
    Similar a A*, pero sin heurística (h(n) = 0).
    Encuentra el camino más barato garantizado, aunque sea más lenta.
    """
    # Cola de prioridad: [(costo acumulado g(n), camino)]
    cola_prioridad = [(0, [inicio])]
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

        # Explora vecinos
        for vecino, distancia in mapa[ciudad_actual].items():
            if vecino not in visitados:
                nuevo_costo = costo + distancia
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                heapq.heappush(cola_prioridad, (nuevo_costo, nuevo_camino))

    return "No se encontró un camino.", 0, nodos_expandidos


# ======================================================
# PRUEBA DE COMPARACIÓN ENTRE UCS y A*
# ======================================================
if __name__ == "__main__":
    from SEGUNDA_PARTE_UNIDAD7 import busqueda_a_estrella
    from PRIMERA_PARTE_UNIDAD7 import heuristica_distancia_recta

    inicio = "La Paz"
    destino = "Santa Cruz"

    print("=== COMPARACIÓN ENTRE A* Y COSTO UNIFORME ===")

    # Búsqueda A*
    camino_a, costo_a, expandidos_a = busqueda_a_estrella(mapa_bolivia_mejorado, inicio, destino)
    print(f"\n[A*] Camino encontrado: {' -> '.join(camino_a)}")
    print(f"[A*] Costo total: {costo_a} km | Nodos expandidos: {expandidos_a}")

    # Búsqueda de Costo Uniforme
    camino_uc, costo_uc, expandidos_uc = busqueda_costo_uniforme(mapa_bolivia_mejorado, inicio, destino)
    print(f"\n[UCS] Camino encontrado: {' -> '.join(camino_uc)}")
    print(f"[UCS] Costo total: {costo_uc} km | Nodos expandidos: {expandidos_uc}")
