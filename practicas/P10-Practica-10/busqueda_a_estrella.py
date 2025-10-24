# Paso 2: Implementar la Búsqueda A* (A-estrella)

import heapq

def busqueda_a_estrella(mapa, inicio, fin):
    """
    Encuentra el camino óptimo usando el algoritmo A*.
    """
    from mapa_mejorado import heuristica_distancia_recta
    
    # La cola de prioridad guarda tuplas de (f(n), g(n), camino_actual)
    # g(n) es el costo para llegar, f(n) es g(n) + h(n)
    cola_prioridad = [(0, 0, [inicio])]
    visitados = set()
    nodos_expandidos = 0
    
    while cola_prioridad:
        f_costo, costo_g, camino = heapq.heappop(cola_prioridad)
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
                # f(n) = g(n) + h(n)
                f_nuevo = nuevo_costo_g + heuristica_distancia_recta(vecino, fin)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                heapq.heappush(cola_prioridad, (f_nuevo, nuevo_costo_g, nuevo_camino))
    
    return "No se encontró un camino.", 0, nodos_expandidos