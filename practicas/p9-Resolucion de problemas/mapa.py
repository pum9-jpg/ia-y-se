# Un grafo no dirigido que representa un mapa simplificado de Bolivia.
mapa = {
    "La Paz": ["Oruro", "Cochabamba"],
    "Oruro": ["La Paz", "Potosí", "Cochabamba"],
    "Cochabamba": ["La Paz", "Oruro", "Santa Cruz", "Sucre"],
    "Potosí": ["Oruro", "Sucre", "Tarija"],
    "Sucre": ["Potosí", "Cochabamba", "Santa Cruz", "Tarija"],
    "Santa Cruz": ["Cochabamba", "Sucre", "Tarija"],
    "Tarija": ["Potosí", "Sucre", "Santa Cruz"]
}

"""
Formulación del problema:
- Estados: las ciudades del mapa.
- Estado inicial: la ciudad de partida (ej. 'La Paz').
- Acciones: viajar a una ciudad vecina.
- Prueba de Meta: llegar a la ciudad destino (ej. 'Tarija').
"""
