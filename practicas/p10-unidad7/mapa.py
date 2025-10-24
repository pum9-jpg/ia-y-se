import math

# Usaremos una cola de prioridad para A*
# 1. El mapa ahora incluye costes (distancias en km) en las conexiones.
mapa_bolivia_mejorado = {
    'La Paz': {'Oruro': 230, 'Beni': 1080},
    'Oruro': {'La Paz': 230, 'Cochabamba': 210, 'Potosí': 330},
    'Cochabamba': {'Oruro': 210, 'Santa Cruz': 400, 'Sucre': 360, 'Beni': 900},
    'Potosí': {'Oruro': 330, 'Chuquisaca': 160, 'Tarija': 345},
    'Chuquisaca': {'Potosí': 160, 'Tarija': 340, 'Cochabamba': 360},
    'Tarija': {'Potosí': 345, 'Chuquisaca': 340},
    'Santa Cruz': {'Cochabamba': 470, 'Chuquisaca': 450, 'Beni': 280},
    'Beni': {'La Paz': 1080, 'Cochabamba': 900, 'Santa Cruz': 280},
    'Sucre': {'Cochabamba': 360, 'Chuquisaca': 100, 'Potosí': 150}
}
# 2. Coordenadas (x, y) aproximadas para cada ciudad para la heurística.
coordenadas_ciudades = {
    'La Paz': (76, 69),
    'Oruro': (61, 67),
    'Cochabamba': (17, 66),
    'Sucre': (63, 64),
    'Chuquisaca': (65, 63),
    'Santa Cruz': (17, 60),
    'Tarija': (21, 64),
    'Beni': (14, 68),
    'Potosí': (62, 65)  
}


# 3. La función heurística
def heuristica_distancia_recta(ciudad_a, ciudad_b):
    """Calcula la distancia Euclidiana (en línea recta) entre dos ciudades."""
    (x1, y1) = coordenadas_ciudades[ciudad_a]
    (x2, y2) = coordenadas_ciudades[ciudad_b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) * 100  # Escala
