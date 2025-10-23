# Paso 3: Implementar Búsqueda en Profundidad (DFS)

def busqueda_profundidad(mapa, inicio, fin):
    """
    Encuentra un camino entre dos ciudades usando DFS.
    """
    # La pila guarda tuplas de (camino_actual)
    pila = [[inicio]]
    # También usamos 'visitados' para evitar bucles infinitos
    visitados = {inicio}
    
    while pila:
        camino = pila.pop()
        ciudad_actual = camino[-1]
        
        if ciudad_actual == fin:
            return camino  # Hemos encontrado la meta
        
        for vecino in mapa.get(ciudad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                pila.append(nuevo_camino)
    
    return "No se encontró un camino."