import math

# Mapa de Bolivia mejorado con distancias reales (en km)
mapa_bolivia_mejorado = {
    'La Paz': {'Oruro': 230, 'Beni': 1060},
    'Oruro': {'La Paz': 230, 'Cochabamba': 210, 'Potosi': 330},
    'Cochabamba': {'Oruro': 210, 'Santa Cruz': 470, 'Chuquisaca': 360, 'Beni': 900},
    'Potosi': {'Oruro': 330, 'Chuquisaca': 160, 'Tarija': 345},
    'Chuquisaca': {'Cochabamba': 360, 'Potosi': 160, 'Santa Cruz': 490, 'Tarija': 480},
    'Santa Cruz': {'Cochabamba': 470, 'Chuquisaca': 490, 'Beni': 280},
    'Tarija': {'Potosi': 345, 'Chuquisaca': 480},
    'Beni': {'La Paz': 1060, 'Cochabamba': 900, 'Santa Cruz': 280}
}

# Coordenadas aproximadas (x, y) para cada ciudad
coordenadas_ciudades = {
    'La Paz': (16, 68), 'Oruro': (17, 67), 'Cochabamba': (17, 66),
    'Potosi': (19, 65), 'Chuquisaca': (19, 65), 'Santa Cruz': (17, 63),
    'Tarija': (21, 64), 'Beni': (14, 65)
}

# Función heurística: distancia euclidiana (en línea recta)
def heuristica_distancia_recta(ciudad_a, ciudad_b):
    (x1, y1) = coordenadas_ciudades[ciudad_a]
    (x2, y2) = coordenadas_ciudades[ciudad_b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2) * 100  # Escala aproximada
