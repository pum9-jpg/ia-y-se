"""
===========================================================
UNIDAD 6: RESOLUCIÓN DE PROBLEMAS MEDIANTE BÚSQUEDAS
Práctica 8 – Agente Resolvente: Búsqueda en Amplitud (BFS) 
y Búsqueda en Profundidad (DFS)
===========================================================

📘 INTRODUCCIÓN
Esta práctica implementa un "Agente Resolvente" capaz de encontrar rutas entre ciudades 
de un mapa simplificado de Bolivia utilizando dos estrategias clásicas de búsqueda 
no informada: la Búsqueda en Amplitud (BFS) y la Búsqueda en Profundidad (DFS).

El objetivo es comprender cómo los agentes pueden planificar sus acciones 
modelando los problemas como un espacio de estados, aplicando algoritmos de búsqueda 
para encontrar la secuencia óptima de pasos hacia una meta.

-----------------------------------------------------------
🔹 OBJETIVOS DE LA UNIDAD
-----------------------------------------------------------
1. Entender el funcionamiento de los agentes resolventes.
2. Modelar un problema de búsqueda mediante estados, acciones y metas.
3. Implementar algoritmos de búsqueda no informada.
4. Comparar el comportamiento y eficiencia de BFS y DFS.

-----------------------------------------------------------
🔹 FORMULACIÓN DEL PROBLEMA
-----------------------------------------------------------
- Estados: Las ciudades del mapa de Bolivia.
- Estado inicial: Ciudad de partida (por ejemplo, “La Paz”).
- Estado meta: Ciudad destino (por ejemplo, “Tarija”).
- Acciones: Viajar a una ciudad vecina conectada directamente.
- Costo de camino: Número de pasos o paradas entre el inicio y la meta.

-----------------------------------------------------------
🔹 REPRESENTACIÓN DEL ENTORNO
-----------------------------------------------------------
El mapa se modela como un grafo no dirigido, donde cada ciudad es un nodo 
y las conexiones son las aristas. Se implementa mediante un diccionario de Python.

Ejemplo:
mapa_bolivia = {
    'La Paz': ['Oruro', 'Beni'],
    'Oruro': ['La Paz', 'Cochabamba', 'Potosí'],
    ...
}

-----------------------------------------------------------
🔹 ALGORITMOS IMPLEMENTADOS
-----------------------------------------------------------

1️⃣ **Búsqueda en Amplitud (BFS)**
   - Utiliza una cola (FIFO).
   - Explora primero los vecinos más cercanos antes de avanzar.
   - Siempre encuentra el camino más corto (óptimo).
   - Requiere más memoria.

2️⃣ **Búsqueda en Profundidad (DFS)**
   - Utiliza una pila (LIFO).
   - Explora una ruta completa antes de retroceder (backtracking).
   - No garantiza el camino más corto.
   - Requiere menos memoria.

-----------------------------------------------------------
🔹 FUNCIONAMIENTO DEL AGENTE
-----------------------------------------------------------
1. Formula el problema con estado inicial y meta.
2. Usa BFS o DFS para explorar el mapa.
3. Devuelve el camino encontrado y el número de paradas.
4. Compara los resultados entre ambos métodos.

-----------------------------------------------------------
🔹 RESULTADOS ESPERADOS
-----------------------------------------------------------
Buscando ruta de 'La Paz' a 'Tarija'.

→ Usando Búsqueda en Amplitud (BFS)
Camino encontrado: La Paz ➜ Oruro ➜ Potosí ➜ Tarija
Número de paradas: 3

→ Usando Búsqueda en Profundidad (DFS)
Camino encontrado: La Paz ➜ Beni ➜ Santa Cruz ➜ Chuquisaca ➜ Tarija
Número de paradas: 4

-----------------------------------------------------------
🔹 CONCLUSIONES
-----------------------------------------------------------
El desarrollo permitio comprender de forma práctica cómo los agentes inteligentes pueden resolver problemas a través de algoritmos de búsqueda.
El algoritmo BFS demostró ser más eficiente para encontrar el camino más corto, aunque su mayor consumo de memoria puede representar una desventaja en entornos más complejos.
Por otro lado, el DFS evidenció una ejecución más rápida y sencilla, pero no siempre garantiza la mejor ruta, ya que puede desviarse por caminos más largos o innecesarios.

En conjunto, ambos métodos son esenciales dentro del campo de la Inteligencia Artificial, pues constituyen la base de los procesos de toma de decisiones y planificación en sistemas autónomos.
Esta práctica evidencia cómo un agente racional puede analizar su entorno, evaluar alternativas y seleccionar un conjunto de acciones coherentes para alcanzar un objetivo definido.


===========================================================
"""
