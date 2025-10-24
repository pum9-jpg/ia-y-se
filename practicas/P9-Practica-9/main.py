# Paso 4: Ejecutar y Comparar los Algoritmos

from mapa_bolivia import mapa_bolivia
from busqueda_amplitud import busqueda_amplitud
from busqueda_profundidad import busqueda_profundidad

# - Definimos el problema -
ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'

print("=" * 60)
print("SISTEMA DE BÚSQUEDA DE RUTAS EN BOLIVIA")
print("=" * 60)
print(f"Buscando ruta de '{ciudad_inicio}' a '{ciudad_destino}'\n")

# - Ejecutar BFS -
print("-" * 40)
print("- Usando Búsqueda en Amplitud (BFS) -")
print("-" * 40)
camino_bfs = busqueda_amplitud(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' → '.join(camino_bfs)}")
print(f"Número de paradas: {len(camino_bfs) - 1}\n")

# - Ejecutar DFS -
print("-" * 40)
print("- Usando Búsqueda en Profundidad (DFS) -")
print("-" * 40)
camino_dfs = busqueda_profundidad(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' → '.join(camino_dfs)}")
print(f"Número de paradas: {len(camino_dfs) - 1}\n")

# - Comparación de Resultados -
print("=" * 60)
print("- RESUMEN COMPARATIVO -")
print("=" * 60)
print(f"BFS - Longitud del camino: {len(camino_bfs) - 1} paradas")
print(f"DFS - Longitud del camino: {len(camino_dfs) - 1} paradas")

if len(camino_bfs) < len(camino_dfs):
    print("\nBFS encontró un camino más corto (óptimo)")
elif len(camino_bfs) > len(camino_dfs):
    print("\nDFS encontró un camino más corto (caso inusual)")
else:
    print("\nAmbos algoritmos encontraron caminos de igual longitud")

# - Pruebas adicionales con otras ciudades -
print("\n" + "=" * 60)
print("- PRUEBAS ADICIONALES -")
print("=" * 60)

# Prueba 1: La Paz a Santa Cruz
print("\nPrueba 1: La Paz → Santa Cruz")
camino_bfs2 = busqueda_amplitud(mapa_bolivia, 'La Paz', 'Santa Cruz')
camino_dfs2 = busqueda_profundidad(mapa_bolivia, 'La Paz', 'Santa Cruz')
print(f"BFS: {' → '.join(camino_bfs2)} ({len(camino_bfs2)-1} paradas)")
print(f"DFS: {' → '.join(camino_dfs2)} ({len(camino_dfs2)-1} paradas)")

# Prueba 2: Oruro a Tarija
print("\nPrueba 2: Oruro → Tarija")
camino_bfs3 = busqueda_amplitud(mapa_bolivia, 'Oruro', 'Tarija')
camino_dfs3 = busqueda_profundidad(mapa_bolivia, 'Oruro', 'Tarija')
print(f"BFS: {' → '.join(camino_bfs3)} ({len(camino_bfs3)-1} paradas)")
print(f"DFS: {' → '.join(camino_dfs3)} ({len(camino_dfs3)-1} paradas)")