# Unidad 6 — Ejercicio 2: Búsqueda en Profundidad (DFS)

## Descripción
El algoritmo de **búsqueda en profundidad (DFS)** explora un grafo o árbol recorriendo primero las ramas más profundas antes de retroceder.  
Es útil cuando se requiere recorrer todos los nodos o cuando las soluciones están en niveles profundos del árbol.

---

## Código (copiado del libro)
```python
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
```

# Ejemplo de salida esperada

Camino encontrado (DFS) de A a F: ['A', 'B', 'E', 'F']

# Observaciones

-**Explora ramas completas antes de retroceder.**
-**Usa recursión o una pila (LIFO) para manejar los estados.**
-**Consume menos memoria que BFS, pero no siempre encuentra el camino más corto.**

# Conclusión
La búsqueda en profundidad es un método eficaz para explorar completamente un problema, aunque no garantiza el camino más corto, es rápida y requiere poca memoria.