# 🗺️ Búsqueda en Grafos: Ruta entre Departamentos de Bolivia
## Mapa de Bolivia (Grafo)
El grafo representa los nueve departamentos de Bolivia, donde cada nodo es un departamento y las aristas son las fronteras terrestres o conexiones directas.
```bash
mapa_bolivia = {
    'La Paz': ['Oruro', 'Beni'],
    'Oruro': ['La Paz', 'Cochabamba', 'Potosi'],
    'Cochabamba': ['Oruro', 'Santa Cruz', 'Chuquisaca', 'Beni'],
    'Potosi': ['Oruro', 'Chuquisaca', 'Tarija'],
    'Chuquisaca': ['Cochabamba', 'Potosi', 'Santa Cruz', 'Tarija'],
    'Santa Cruz': ['Cochabamba', 'Chuquisaca', 'Beni'],
    'Tarija': ['Potosi', 'Chuquisaca'],
    'Beni': ['La Paz', 'Cochabamba', 'Santa Cruz'],
    'Pando': []
}   
```

## 🔎 Búsqueda en Amplitud (BFS)
La función busqueda_amplitud implementa BFS, que garantiza encontrar el camino con el menor número de paradas (el más corto en términos de saltos).
``` bash
def busqueda_amplitud(mapa, inicio, fin):
    cola = deque([[inicio]])
    visitados = {inicio}

    while cola:
        camino = cola.popleft()
        ciudad_actual = camino[-1]

        if ciudad_actual == fin:
            return camino
        
        for vecino in mapa.get(ciudad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    return "No se encontró un camino.
```

## 🧠 Búsqueda en Profundidad (DFS)
La función busqueda_profundidad implementa DFS, que explora lo más lejos posible a lo largo de cada rama antes de retroceder (backtracking).
``` bash
def busqueda_profundidad(mapa, inicio, fin):
    pila = [[inicio]]
    visitados = {inicio}

    while pila:
        camino = pila.pop()
        ciudad_actual = camino[-1]

        if ciudad_actual == fin:
            return camino
        
        for vecino in mapa.get(ciudad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                pila.append(nuevo_camino)
    return "No se encontró un camino."
```

## 💻 Resultados de la Simulación
``` bash
Buscando ruta de 'La Paz' a 'Tarija'. 

--- Usando Busqueda en Amplitud (BFS) ---
Camino encontrado: La Paz->Oruro->Potosi->Tarija
Numero de paradas: 3

--- Usando Busqueda en Profundidad (DFS) ---
Camino encontrado: La Paz->Beni->Santa Cruz->Chuquisaca->Tarija
Numero de paradas: 4
```