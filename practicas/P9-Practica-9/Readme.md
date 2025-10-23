# Sistema de Búsqueda de Rutas en Bolivia - BFS vs DFS

## Descripción General

Este proyecto implementa y compara dos algoritmos fundamentales de búsqueda en inteligencia artificial: Búsqueda en Amplitud (BFS) y Búsqueda en Profundidad (DFS). El sistema resuelve el problema de encontrar rutas entre ciudades bolivianas, demostrando las diferencias en eficiencia y optimalidad entre ambos enfoques algorítmicos.

## Arquitectura del Sistema

### Componentes Principales

**1. Mapa de Bolivia (mapa_bolivia.py)**
- Representa el grafo de conexiones entre ciudades bolivianas
- Modela las rutas terrestres como un grafo no dirigido
- Define las conexiones directas entre ciudades vecinas
- Incluye 8 ciudades principales con sus conexiones

**2. Búsqueda en Amplitud - BFS (busqueda_amplitud.py)**
- Implementa el algoritmo de búsqueda por niveles
- Utiliza una cola (FIFO) para gestionar nodos por visitar
- Garantiza encontrar el camino más corto en términos de número de ciudades
- Evita ciclos mediante conjunto de nodos visitados

**3. Búsqueda en Profundidad - DFS (busqueda_profundidad.py)**
- Implementa el algoritmo de búsqueda en profundidad
- Utiliza una pila (LIFO) para gestionar nodos por visitar
- Explora ramas completas antes de retroceder
- Puede encontrar caminos más largos pero con menos uso de memoria

**4. Sistema Principal (main.py)**
- Coordina la ejecución de ambos algoritmos
- Presenta comparativas detalladas de resultados
- Ejecuta múltiples casos de prueba
- Analiza la optimalidad de las soluciones

## Formulación del Problema

### Elementos del Problema de Búsqueda
- **Estados**: Las ciudades del mapa boliviano
- **Estado Inicial**: Ciudad de partida (ej. 'La Paz')
- **Acciones**: Viajar a una ciudad vecina conectada
- **Prueba de Meta**: Llegar a la ciudad destino (ej. 'Tarija')
- **Costo de Camino**: Número de ciudades intermedias (todas las acciones tienen costo 1)

### Representación del Grafo
```python
mapa_bolivia = {
    'La Paz': ['Oruro', 'Beni'],
    'Oruro': ['La Paz', 'Cochabamba', 'Potosi'],
    'Cochabamba': ['Oruro', 'Santa Cruz', 'Chuquisaca', 'Beni'],
    # ... más conexiones
}
```

## Instalación y Requisitos

### Prerrequisitos
- Python 3.6 o superior
- No se requieren librerías externas (solo collections.deque de la biblioteca estándar)

### Estructura de Archivos
```
proyecto_busqueda_bolivia/
│
├── mapa_bolivia.py
├── busqueda_amplitud.py
├── busqueda_profundidad.py
├── main.py
└── README.md
```

## Ejecución del Sistema

### Ejecución Completa
```bash
python main.py
```

### Ejecución de Componentes Individuales
```bash
# Para verificar el mapa
python -c "from mapa_bolivia import mapa_bolivia; print('Mapa cargado correctamente')"

# Para probar BFS específicamente
python -c "from busqueda_amplitud import busqueda_amplitud; from mapa_bolivia import mapa_bolivia; print(busqueda_amplitud(mapa_bolivia, 'La Paz', 'Tarija'))"
```

## Algoritmos Implementados

### Búsqueda en Amplitud (BFS)
**Características:**
- Completo: Siempre encuentra solución si existe
- Óptimo: Encuentra el camino con menor número de pasos
- Complejidad temporal: O(b^d) donde b es el factor de ramificación y d la profundidad
- Complejidad espacial: O(b^d) - puede ser alto para grafos grandes

**Flujo:**
1. Iniciar con nodo raíz en la cola
2. Expandir todos los vecinos del nodo actual
3. Añadir vecinos no visitados a la cola
4. Repetir hasta encontrar meta o agotar nodos

### Búsqueda en Profundidad (DFS)
**Características:**
- Completo: En grafos finitos sin ciclos infinitos
- No óptimo: Puede encontrar caminos más largos
- Complejidad temporal: O(b^m) donde m es la profundidad máxima
- Complejidad espacial: O(bm) - más eficiente en memoria

**Flujo:**
1. Iniciar con nodo raíz en la pila
2. Expandir un vecino y profundizar
3. Retroceder cuando no haya más vecinos por explorar
4. Repetir hasta encontrar meta

## Casos de Prueba Incluidos

### Caso Principal: La Paz → Tarija
- **BFS**: Encuentra ruta más directa (La Paz → Oruro → Potosi → Tarija)
- **DFS**: Puede encontrar rutas alternativas más largas

### Casos Adicionales:
1. **La Paz → Santa Cruz**: Múltiples rutas posibles
2. **Oruro → Tarija**: Ruta directa vs rutas alternativas
3. **Ciudades conectadas vs aisladas**: Prueba con Pando

## Métricas de Evaluación

### Criterios de Comparación
- **Longitud del camino**: Número de ciudades intermedias
- **Optimalidad**: Si encuentra el camino más corto
- **Completitud**: Capacidad de encontrar solución si existe
- **Eficiencia**: Uso de memoria y tiempo de ejecución

### Ejemplo de Salida
```
BFS: La Paz → Oruro → Potosi → Tarija (3 paradas)
DFS: La Paz → Beni → Cochabamba → Chuquisaca → Tarija (4 paradas)
```

## Conclusión

# Sistema de Búsqueda de Rutas en Bolivia - BFS vs DFS

## Conclusión

Este proyecto demuestra que **BFS (Búsqueda en Amplitud) es mejor para encontrar rutas óptimas** entre ciudades, ya que siempre encuentra el camino más corto. **DFS (Búsqueda en Profundidad)** puede encontrar rutas alternativas, pero no garantiza que sean las más cortas.

**BFS** explora todas las opciones por niveles, lo que le permite encontrar la ruta con menos paradas. **DFS** se adentra en una dirección hasta el final antes de probar otras, usando menos memoria pero pudiendo encontrar caminos más largos.

La elección depende del objetivo: si buscas la ruta más directa, usa BFS; si tienes memoria limitada, DFS puede ser útil. Ambos algoritmos son fundamentales en inteligencia artificial para resolver problemas de búsqueda y planificación.