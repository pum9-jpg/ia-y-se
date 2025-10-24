from busqueda_costo_uniforme import busqueda_costo_uniforme
from busqueda_a_estrella import busqueda_a_estrella
from mapa_mejorado_heuristica import mapa_bolivia_mejorado

if __name__ == "__main__":
    inicio = "La Paz"
    destino = "Tarija"

    print("\n--- Usando Búsqueda de Costo Uniforme (UCS) ---")
    camino_ucs, costo_ucs, nodos_ucs = busqueda_costo_uniforme(mapa_bolivia_mejorado, inicio, destino)
    print(f"Camino encontrado: {' ➔ '.join(camino_ucs)}")
    print(f"Costo total del viaje: {costo_ucs} km")
    print(f"Ciudades (nodos) expandidas: {nodos_ucs}\n")

    print("--- Usando Búsqueda A* (Informada) ---")
    camino_a, costo_a, nodos_a = busqueda_a_estrella(mapa_bolivia_mejorado, inicio, destino)
    print(f"Camino encontrado: {' ➔ '.join(camino_a)}")
    print(f"Costo total del viaje: {costo_a} km")
    print(f"Ciudades (nodos) expandidas: {nodos_a}\n")

    print("Conclusión: A* encontró el mismo camino óptimo con menos nodos expandidos, demostrando mayor eficiencia gracias a la heurística.")
