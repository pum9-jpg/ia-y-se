from mapa import mapa_bolivia_mejorado
from busqueda_costo_uniforme import busqueda_costo_uniforme
from busqueda_a_estrella import busqueda_a_estrella

ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'

print(f"Buscando la ruta más corta de '{ciudad_inicio}' a '{ciudad_destino}'. \n")

# -  Ejecutar Búsqueda de Costo Uniforme (No Informada) -
print("-     Usando Búsqueda de Costo Uniforme (UCS) - ")
camino_ucs, costo_ucs, expandidos_ucs = busqueda_costo_uniforme(
    mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' → '.join(camino_ucs)}")
print(f"Costo total del viaje: {costo_ucs} km")
print(f"Ciudades (nodos) expandidas: {expandidos_ucs}\n")

# -  Ejecutar Búsqueda A* (Informada) -
print("-     Usando Búsqueda A* (Informada) - ")
camino_a_estrella, costo_a_estrella, expandidos_a_estrella = busqueda_a_estrella(
    mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' → '.join(camino_a_estrella)}")
print(f"Costo total del viaje: {costo_a_estrella} km")
print(f"Ciudades (nodos) expandidas: {expandidos_a_estrella}\n")

# -   Análisis   -
print("—   Análisis de Resultados —  ")
if expandidos_a_estrella < expandidos_ucs:
    print(f"A* fue más eficiente: expandió {expandidos_ucs - expandidos_a_estrella} nodos menos que UCS para encontrar la misma ruta óptima.")
else:
    print("Ambos algoritmos fueron igualmente eficientes.")
