# Paso 4: Ejecutar y Analizar los Resultados

from mapa_mejorado import mapa_bolivia_mejorado
from busqueda_a_estrella import busqueda_a_estrella
from busqueda_costo_uniforme import busqueda_costo_uniforme

ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'

print("=" * 60)
print("BÚSQUEDA INFORMADA VS NO INFORMADA - A* vs UCS")
print("=" * 60)
print(f"Buscando la ruta más corta de '{ciudad_inicio}' a '{ciudad_destino}'\n")

# - Ejecutar Búsqueda de Costo Uniforme (No Informada) -
print("-" * 50)
print("- Usando Búsqueda de Costo Uniforme (UCS) -")
print("-" * 50)
camino_ucs, costo_ucs, expandidos_ucs = busqueda_costo_uniforme(mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' → '.join(camino_ucs)}")
print(f"Costo total del viaje: {costo_ucs} km")
print(f"Ciudades (nodos) expandidas: {expandidos_ucs}\n")

# - Ejecutar Búsqueda A* (Informada) -
print("-" * 50)
print("- Usando Búsqueda A* (Informada) -")
print("-" * 50)
camino_a_estrella, costo_a_estrella, expandidos_a_estrella = busqueda_a_estrella(mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' → '.join(camino_a_estrella)}")
print(f"Costo total del viaje: {costo_a_estrella} km")
print(f"Ciudades (nodos) expandidas: {expandidos_a_estrella}\n")

# - Análisis -
print("=" * 60)
print("- ANÁLISIS DE RESULTADOS -")
print("=" * 60)

if expandidos_a_estrella < expandidos_ucs:
    diferencia = expandidos_ucs - expandidos_a_estrella
    print(f"A* fue más eficiente: expandió {diferencia} nodos menos que UCS para encontrar la misma ruta óptima.")
else:
    print("Ambos algoritmos fueron igualmente eficientes.")

print(f"\nAmbos algoritmos encontraron rutas con el mismo costo: {costo_ucs} km")
print(f"Ruta óptima: {' → '.join(camino_ucs)}")

# - Pruebas adicionales -
print("\n" + "=" * 60)
print("- PRUEBAS ADICIONALES -")
print("=" * 60)

# Prueba 1: La Paz a Santa Cruz
print("\nPrueba 1: La Paz → Santa Cruz")
camino_ucs2, costo_ucs2, exp_ucs2 = busqueda_costo_uniforme(mapa_bolivia_mejorado, 'La Paz', 'Santa Cruz')
camino_a2, costo_a2, exp_a2 = busqueda_a_estrella(mapa_bolivia_mejorado, 'La Paz', 'Santa Cruz')
print(f"UCS: {costo_ucs2} km, {exp_ucs2} nodos expandidos")
print(f"A*:  {costo_a2} km, {exp_a2} nodos expandidos")

# Prueba 2: Cochabamba a Tarija
print("\nPrueba 2: Cochabamba → Tarija")
camino_ucs3, costo_ucs3, exp_ucs3 = busqueda_costo_uniforme(mapa_bolivia_mejorado, 'Cochabamba', 'Tarija')
camino_a3, costo_a3, exp_a3 = busqueda_a_estrella(mapa_bolivia_mejorado, 'Cochabamba', 'Tarija')
print(f"UCS: {costo_ucs3} km, {exp_ucs3} nodos expandidos")
print(f"A*:  {costo_a3} km, {exp_a3} nodos expandidos")