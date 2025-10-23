README - Búsqueda Informada con Algoritmo A*
📋 Descripción del Proyecto
Este proyecto implementa y compara dos algoritmos de búsqueda de rutas óptimas en un grafo que representa ciudades de Bolivia:

Búsqueda de Costo Uniforme (UCS): Algoritmo no informado

Búsqueda A*: Algoritmo informado con heurística

El objetivo es demostrar la superioridad en eficiencia de los algoritmos informados cuando se dispone de información adicional (heurística).

🏗️ Estructura del Código
1. Mapa de Conexiones
python
mapa_bolivia_mejorado = {
    'La Paz': {'Oruro': 230, 'Beni': 1060},
    'Oruro': {'La Paz': 230, 'Cochabamba': 210, 'Potosi': 330},
    # ... más conexiones
}
Representa las conexiones entre ciudades con distancias reales en kilómetros.

2. Coordenadas para Heurística
python
coordenadas_ciudades = {
    'La Paz': (16, 66),
    'Oruro': (17, 67),
    # ... más coordenadas
}
Coordenadas aproximadas (x,y) para calcular distancias en línea recta.

3. Función Heurística
python
def heuristica_distancia_recta(ciudad_a, ciudad_b):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2) * 100
Calcula la distancia Euclidiana entre dos ciudades, multiplicada por 100 para escalar.

4. Algoritmo A*
f(n) = g(n) + h(n)

g(n): costo real desde el inicio

h(n): costo estimado al destino (heurística)

Usa cola de prioridad basada en f(n)

5. Algoritmo de Costo Uniforme
Versión simplificada de A* con h(n) = 0

Búsqueda "a ciegas" sin información heurística

🚀 Cómo Ejecutar
Asegúrate de tener Python instalado

Ejecuta el script:

bash
python busqueda_a_estrella.py
📊 Resultados Esperados
text
Buscando la ruta más corta de 'La Paz' a 'Tarija'.

- Usando Búsqueda de Costo Uniforme (UCS) -
Camino encontrado: La Paz → Oruro → Potosi → Tarija
Costo total del viaje: 905 km
Ciudades (nodos) expandidas: 8

- Usando Búsqueda A* (Informada) -
Camino encontrado: La Paz → Oruro → Potosi → Tarija
Costo total del viaje: 905 km
Ciudades (nodos) expandidas: 5

- Análisis de Resultados -
A* fue más eficiente: expandió 3 nodos menos que UCS
🔍 Análisis de los Resultados
Eficiencia Comparativa
A*: Expandió 5 nodos

UCS: Expandió 8 nodos

Mejora: 37.5% menos nodos expandidos

Características de la Heurística
Admisible: Nunca sobreestima el costo real

Consistente: Satisface la desigualdad triangular

Óptima: Garantiza encontrar el camino de menor costo

💡 Conclusiones
1. Eficiencia en la Búsqueda
El algoritmo A* demostró ser significativamente más eficiente que la búsqueda de costo uniforme, expandiendo un 37.5% menos nodos para encontrar la misma ruta óptima.

2. Importancia de la Heurística
La función heurística bien diseñada (distancia en línea recta) permite:

Guiar la búsqueda hacia el objetivo

Evitar explorar caminos poco prometedores

Mantener la optimalidad de la solución

3. Aplicaciones Prácticas
Este enfoque tiene aplicaciones en:

Sistemas de navegación GPS

Planificación de rutas logísticas

Juegos para pathfinding de IA

Optimización de redes de transporte

4. Limitaciones y Consideraciones
La calidad de la heurística afecta directamente el rendimiento

En problemas muy grandes, el consumo de memoria puede ser alto

La optimalidad depende de que la heurística sea admisible


Conclusión final
En codigo de ambos algoritmos (UCS y A*) llegan a encontrar la misma ruta entre las ciudades, pero A* lo hizo explorando menos nodos solamente (5 frente a 8, 37.5% menos), esto pasa porque A* utiliza una heurística (la distancia en línea recta) que estima qué tan cerca está cada ciudad del destino y así prioriza caminos directos, evitando investigar rutas largas o irrelevantes asi la heurística no sobreestima y son consistente, A* sigue garantizando la mejor solución, por lo que, en la práctica, usar A* significa menos trabajo computacional y respuestas más rápidas en grafos grandes, aunque puede necesitar más memoria, y siempre conviene diseñar bien la heurística para obtener esos beneficios.
