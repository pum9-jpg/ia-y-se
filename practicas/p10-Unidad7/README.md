# 🛣️ Búsqueda de Ruta Óptima en Bolivia:

## 🔎 Búsqueda de Costo Uniforme (UCS)
La Búsqueda de Costo Uniforme (UCS) es un algoritmo de búsqueda no informada que explora el grafo priorizando los nodos con el menor costo acumulado desde el inicio.
``` bash
def busqueda_costo_uniforme(mapa, inicio, fin):
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
        for vecino, distancia in mapa[ciudad_actual].items():
            if vecino not in visitados:
                nuevo_costo = costo + distancia
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                heapq.heappush(cola_prioridad, (nuevo_costo, nuevo_camino))
    return "No se encontró un camino", 0, nodos_expandidos
```

## ✨ Búsqueda A* (A-Star) Informada
La Búsqueda A* es un algoritmo de búsqueda informada que combina el costo real recorrido con una estimación del costo restante hasta el destino, lo que le permite "guiarse" de manera más eficiente.
``` bash
def busqueda_a_estrella(mapa, inicio, fin):
    cola_prioridad = [(0, 0, [inicio])]
    visitados = set()
    nodos_expandidos = 0

    while cola_prioridad:
        _, costo_g, camino = heapq.heappop(cola_prioridad)
        ciudad_actual = camino[-1]

        nodos_expandidos += 1

        if ciudad_actual in visitados:
            continue
           
        visitados.add(ciudad_actual)

        if ciudad_actual == fin:
            return camino, costo_g, nodos_expandidos
           
        for vecino, distancia in mapa[ciudad_actual].items():
            if vecino not in visitados:
                nuevo_costo_g = costo_g + distancia
                costo_h = heuristica_distancia_recta(vecino, fin)
                costo_f = nuevo_costo_g + costo_h

                nuevo_camino = list(vecino)
                nuevo_camino.append(vecino)
                heapq.heappush(cola_prioridad, (costo_f, nuevo_costo_g, nuevo_camino))

    return "No se encontró un camino", 0, nodos_expandidos
```

## 📊 Ejecución y Resultados
```bash
Buscando la ruta más corta de 'La Paz' a 'Tarija'. 

-    Usando Búsqueda de Costo Uniforme (UCS)    -
Camino encontrado: La Paz->Oruro->Potosi->Tarija
Costo total del viaje: 895 km
Ciudades (nodos) expandidas: 7

-    Usando Búsqueda A* (Informada)    -
Camino encontrado: T->a->r->i->j->a->Tarija
Costo total del viaje: 895 km
Ciudades (nodos) expandidas: 4

-    Analisis de Resultados    -
A* fue más eficiente: expandio 3 nodos menos que UCS para encontrar la misma ruta optima.
```