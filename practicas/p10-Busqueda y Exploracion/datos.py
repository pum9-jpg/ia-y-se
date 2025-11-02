# -*- coding: utf-8 -*-
import math

# Grafo no dirigido: costos reales por carretera entre ciudades (en km aprox.)
mapa_costos = {
    "La Paz": {"Oruro": 230, "Cochabamba": 380},
    "Oruro": {"La Paz": 230, "Potosí": 340, "Cochabamba": 220},
    "Cochabamba": {"La Paz": 380, "Oruro": 220, "Santa Cruz": 480, "Sucre": 330},
    "Potosí": {"Oruro": 340, "Sucre": 160, "Tarija": 250},
    "Sucre": {"Potosí": 160, "Cochabamba": 330, "Santa Cruz": 360, "Tarija": 460},
    "Santa Cruz": {"Cochabamba": 480, "Sucre": 360, "Tarija": 520},
    "Tarija": {"Potosí": 250, "Sucre": 460, "Santa Cruz": 520},
}

# Coordenadas (x, y) relativas para una heurística geométrica simple (no a escala real)
coords = {
    "La Paz": (0, 9),
    "Oruro": (1, 7),
    "Cochabamba": (3, 7),
    "Potosí": (2, 5),
    "Sucre": (4, 5),
    "Santa Cruz": (6, 6),
    "Tarija": (5, 3),
}

def heuristica(nodo, objetivo):
    """
    h(n): distancia en línea recta (euclídea) desde 'nodo' hasta 'objetivo'.
    Es admisible y consistente si las coordenadas guardan la relación espacial.
    """
    (x1, y1) = coords[nodo]
    (x2, y2) = coords[objetivo]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
