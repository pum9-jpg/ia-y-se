from mapa import mapa
from busquedas import busqueda_amplitud, busqueda_profundidad

# Definimos el problema
ciudad_inicio = "La Paz"
ciudad_destino = "Tarija"

print(f"Buscando ruta de '{ciudad_inicio}' a '{ciudad_destino}'\n")

# --- BFS ---
camino_bfs = busqueda_amplitud(mapa, ciudad_inicio, ciudad_destino)
print("Usando Búsqueda en Amplitud (BFS):")
if camino_bfs:
    print(f"Camino encontrado: {' -> '.join(camino_bfs)}")
else:
    print("No se encontró un camino.\n")

# --- DFS ---
camino_dfs = busqueda_profundidad(mapa, ciudad_inicio, ciudad_destino)
print("\nUsando Búsqueda en Profundidad (DFS):")
if camino_dfs:
    print(f"Camino encontrado: {' -> '.join(camino_dfs)}")
else:
    print("No se encontró un camino.\n")

print("\nComparación completa finalizada.")
