# -*- coding: utf-8 -*-
from datos import mapa_costos, heuristica
from algoritmos import a_estrella, costo_uniforme

ciudad_inicio = "La Paz"
ciudad_destino = "Tarija"

print(f"Buscando la ruta más corta de '{ciudad_inicio}' a '{ciudad_destino}'\n")

# --- Búsqueda de Costo Uniforme (UCS) ---
camino_ucs, costo_ucs, exp_ucs = costo_uniforme(mapa_costos, ciudad_inicio, ciudad_destino)
print(">> Usando Búsqueda de Costo Uniforme (UCS):")
if camino_ucs:
    print("Camino encontrado:", " -> ".join(camino_ucs))
    print("Costo total (km):", costo_ucs)
    print("Nodos expandidos:", exp_ucs)
else:
    print("No se encontró un camino.\n")

# --- Búsqueda A* (A-estrella) ---
h = lambda n: heuristica(n, ciudad_destino)
camino_astar, costo_astar, exp_astar = a_estrella(mapa_costos, h, ciudad_inicio, ciudad_destino)
print("\n>> Usando Búsqueda A* (A-estrella):")
if camino_astar:
    print("Camino encontrado:", " -> ".join(camino_astar))
    print("Costo total (km):", costo_astar)
    print("Nodos expandidos:", exp_astar)
else:
    print("No se encontró un camino.\n")

# --- Análisis corto ---
print("\n--- Análisis de Resultados ---")
if costo_astar == costo_ucs:
    print("✔ Ambos métodos hallaron el mismo costo óptimo.")
else:
    print("⚠ Los costos difieren: revisa la heurística/tus datos.")

if exp_astar <= exp_ucs:
    print("✔ A* expandió igual o menos nodos que UCS (heurística efectiva).")
else:
    print("⚠ A* expandió más nodos que UCS (heurística poco informativa).")
