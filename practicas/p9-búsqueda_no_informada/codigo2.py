def dfs(grafo, inicio, objetivo, visitados=None, camino=None):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = [inicio]
    
    visitados.add(inicio)
    
    if inicio == objetivo:
        return camino

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            nuevo_camino = dfs(grafo, vecino, objetivo, visitados, camino + [vecino])
            if nuevo_camino:
                return nuevo_camino
    return None

# Ejemplo de grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Camino encontrado (DFS) de A a F:", dfs(grafo, 'A', 'F'))
