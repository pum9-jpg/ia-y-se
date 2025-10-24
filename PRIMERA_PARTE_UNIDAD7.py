# ===============================================
# UNIDAD 7 - PRÁCTICA 10
# PARTE 1: Mapa Mejorado y Función Heurística
# ===============================================

import math
import heapq  # Usaremos una cola de prioridad para A*

# 1. El mapa ahora incluye costos (distancias en km) en las conexiones.
mapa_bolivia_mejorado = {
    'La Paz': {'Oruro': 230, 'Beni': 1060},
    'Oruro': {'La Paz': 230, 'Cochabamba': 210, 'Potosí': 330},
    'Cochabamba': {'Oruro': 210, 'Santa Cruz': 470, 'Chuquisaca': 360, 'Beni': 900},
    'Potosí': {'Oruro': 330, 'Chuquisaca': 160, 'Tarija': 345},
    'Chuquisaca': {'Cochabamba': 360, 'Potosí': 160, 'Santa Cruz': 470, 'Tarija': 480},
    'Santa Cruz': {'Cochabamba': 470, 'Chuquisaca': 490, 'Beni': 280},
    'Tarija': {'Potosí': 345, 'Chuquisaca': 480},
    'Beni': {'La Paz': 1060, 'Cochabamba': 900, 'Santa Cruz': 280}
}

# 2. Coordenadas (x, y) aproximadas para cada ciudad (usadas por la heurística)
coordenadas_ciudades = {
    'La Paz': (16, 68),
    'Oruro': (17, 67),
    'Cochabamba': (17, 66),
    'Potosí': (19, 65),
    'Chuquisaca': (19, 64),
    'Santa Cruz': (17, 63),
    'Tarija': (21, 64),
    'Beni': (14, 65)
}

# 3. Función Heurística
def heuristica_distancia_recta(ciudad_a, ciudad_b):
    """
    Calcula la distancia Euclidiana (en línea recta) entre dos ciudades.
    """
    (x1, y1) = coordenadas_ciudades[ciudad_a]
    (x2, y2) = coordenadas_ciudades[ciudad_b]
    # Multiplicador para escalar la distancia a unidades de km
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) * 100


# Prueba rápida
if __name__ == "__main__":
    print("=== MAPA DE BOLIVIA (MEJORADO) ===")
    for ciudad, conexiones in mapa_bolivia_mejorado.items():
        print(f"{ciudad} -> {conexiones}")

    print("\n=== PRUEBA DE HEURÍSTICA ===")
    print(f"Distancia estimada (La Paz → Santa Cruz): {heuristica_distancia_recta('La Paz', 'Santa Cruz'):.2f} km")
    print(f"Distancia estimada (Oruro → Tarija): {heuristica_distancia_recta('Oruro', 'Tarija'):.2f} km")
