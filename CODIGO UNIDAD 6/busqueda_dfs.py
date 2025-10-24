# busqueda_dfs.py

def busqueda_profundidad(grafo, inicio, meta, camino=None, visitados=None):
    """Búsqueda en profundidad (DFS): explora una rama hasta el final antes de retroceder."""
    if camino is None:
        camino = [inicio]
    if visitados is None:
        visitados = set()

    nodo = camino[-1]
    if nodo == meta:
        return camino

    visitados.add(nodo)

    for vecino in grafo.get(nodo, []):
        if vecino not in visitados:
            nuevo_camino = list(camino)
            nuevo_camino.append(vecino)
            resultado = busqueda_profundidad(grafo, inicio, meta, nuevo_camino, visitados)
            if resultado:
                return resultado

    return None
