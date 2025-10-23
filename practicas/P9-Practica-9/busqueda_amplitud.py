# Paso 2: Implementar Búsqueda en Amplitud (BFS)

from collections import deque

def busqueda_amplitud(mapa, inicio, fin):
    """
    Encuentra el camino más corto entre dos ciudades usando BFS.
    """
    # La cola guarda tuplas de (camino_actual)
    cola = deque([[inicio]])
    
    # El conjunto 'visitados' nos ayuda a "Evitar estados repetidos"
    visitados = {inicio}
    
    while cola:
        camino = cola.popleft()
        ciudad_actual = camino[-1]
        
        if ciudad_actual == fin:
            return camino  # Hemos encontrado la meta
        
        for vecino in mapa.get(ciudad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    
    return "No se encontró un camino."