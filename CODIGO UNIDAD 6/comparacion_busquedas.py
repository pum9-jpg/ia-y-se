# comparacion_busquedas.py
from mapa_bolivia import mapa_bolivia
from busqueda_bfs import busqueda_amplitud
from busqueda_dfs import busqueda_profundidad

ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'

print(f"Buscando ruta de '{ciudad_inicio}' a '{ciudad_destino}'.\n")

print("- Usando Búsqueda en Amplitud (BFS) -")
camino_bfs = busqueda_amplitud(mapa_bolivia, ciudad_inicio, ciudad_destino)
if camino_bfs:
    print(f"Camino encontrado: {' ➔ '.join(camino_bfs)}")
    print(f"Número de paradas: {len(camino_bfs) - 1}\n")
else:
    print("No se encontró un camino usando BFS.\n")

print("- Usando Búsqueda en Profundidad (DFS) -")
camino_dfs = busqueda_profundidad(mapa_bolivia, ciudad_inicio, ciudad_destino)
if camino_dfs:
    print(f"Camino encontrado: {' ➔ '.join(camino_dfs)}")
    print(f"Número de paradas: {len(camino_dfs) - 1}")
else:
    print("No se encontró un camino usando DFS.")
