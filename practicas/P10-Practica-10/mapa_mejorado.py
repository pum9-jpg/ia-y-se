# Paso 1: Mejorar el Mapa y Definir la Heurística

import math

# 1. El mapa ahora incluye costos (distancias en km) en las conexiones.
mapa_bolivia_mejorado = {
    'La Paz': {'Oruro': 230, 'Beni': 1000},
    'Oruro': {'La Paz': 230, 'Cochabamba': 210, 'Potosi': 330},
    'Cochabamba': {'Oruro': 210, 'Santa Cruz': 470, 'Chuquisaca': 360, 'Beni': 800},
    'Potosi': {'Oruro': 330, 'Chuquisaca': 160, 'Tarija': 345},
    'Chuquisaca': {'Cochabamba': 360, 'Potosi': 160, 'Santa Cruz': 490, 'Tarija': 480},
    'Santa Cruz': {'Cochabamba': 470, 'Chuquisaca': 490, 'Beni': 280},
    'Tarija': {'Potosi': 345, 'Chuquisaca': 480},
    'Beni': {'La Paz': 1000, 'Cochabamba': 900, 'Santa Cruz': 280}
}

# 2. Coordenadas (x, y) aproximadas para cada ciudad para la heurística.
coordenadas_ciudades = {
    'La Paz': (16, 68), 'Oruro': (17, 67), 'Cochabamba': (17, 66),
    'Potosi': (19, 65), 'Chuquisaca': (19, 65), 'Santa Cruz': (17, 63),
    'Tarija': (21, 64), 'Beni': (14, 65)
}

# 3. La Función Heurística
def heuristica_distancia_recta(ciudad_a, ciudad_b):
    """Calcula la distancia Euclidiana (en línea recta) entre dos ciudades."""
    (x1, y1) = coordenadas_ciudades[ciudad_a]
    (x2, y2) = coordenadas_ciudades[ciudad_b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2) * 100  # Multiplicador para escalar