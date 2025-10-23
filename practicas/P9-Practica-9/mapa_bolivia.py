# Paso 1: Formulación del Problema y Representación del Mapa

# Un grafo no dirigido que representa un mapa simplificado de Bolivia.
# Las claves son las ciudades y los valores son las ciudades conectadas directamente.
mapa_bolivia = {
    'La Paz': ['Oruro', 'Beni'],
    'Oruro': ['La Paz', 'Cochabamba', 'Potosi'],
    'Cochabamba': ['Oruro', 'Santa Cruz', 'Chuquisaca', 'Beni'],
    'Potosi': ['Oruro', 'Chuquisaca', 'Tarija'],
    'Chuquisaca': ['Cochabamba', 'Potosi', 'Santa Cruz', 'Tarija'],
    'Santa Cruz': ['Cochabamba', 'Chuquisaca', 'Beni'],
    'Tarija': ['Potosi', 'Chuquisaca'],
    'Beni': ['La Paz', 'Cochabamba', 'Santa Cruz'],
    'Pando': []  # Pando está aislado en este mapa simplificado
}