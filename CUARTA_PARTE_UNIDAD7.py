# ===============================================
# UNIDAD 7 - PRÁCTICA 10
# PARTE 4: Ejecutar y Analizar los Resultados
# ===============================================

from PRIMERA_PARTE_UNIDAD7 import mapa_bolivia_mejorado
from SEGUNDA_PARTE_UNIDAD7 import busqueda_a_estrella
from TERCERA_PARTE_UNIDAD7 import busqueda_costo_uniforme

# Definir los puntos de inicio y destino
ciudad_inicio = "La Paz"
ciudad_destino = "Tarija"

print(f"\nBuscando la ruta más corta de '{ciudad_inicio}' a '{ciudad_destino}'.\n")

# -------------------------------
# Ejecutar Búsqueda No Informada (UCS)
# -------------------------------
print("–  Usando Búsqueda de Costo Uniforme (UCS)  –")

camino_ucs, costo_ucs, expandidos_ucs = busqueda_costo_uniforme(
    mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino
)

print(f"Camino encontrado: {' ➜ '.join(camino_ucs)}")
print(f"Costo total del viaje: {costo_ucs} km")
print(f"Ciudades (nodos) expandidas: {expandidos_ucs}\n")

# -------------------------------
# Ejecutar Búsqueda Informada (A*)
# -------------------------------
print("–  Usando Búsqueda A* (Informada)  –")

camino_a, costo_a, expandidos_a = busqueda_a_estrella(
    mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino
)

print(f"Camino encontrado: {' ➜ '.join(camino_a)}")
print(f"Costo total del viaje: {costo_a} km")
print(f"Ciudades (nodos) expandidas: {expandidos_a}\n")

# -------------------------------
# Análisis de Resultados
# -------------------------------
print("–  Análisis de Resultados  –")

if expandidos_a < expandidos_ucs:
    print(
        f"A* fue más eficiente: expandió {expandidos_ucs - expandidos_a} "
        f"nodos menos que UCS para encontrar la misma ruta óptima."
    )
else:
    print("Ambos algoritmos fueron igualmente eficientes.")
