# Unidad 6: Resolución de Problemas Mediante Búsquedas

## Introducción
Esta unidad explica cómo un **agente inteligente** puede resolver problemas mediante la **búsqueda en espacios de estados**. El objetivo es hallar una secuencia de acciones que lleve al agente desde un estado inicial hasta un objetivo.

## 6.1 Agentes Resolventes
Un **agente resolvente** formula su meta, define su problema, busca una secuencia de acciones y luego las ejecuta. Este agente:
1. Formula un objetivo.
2. Define el problema.
3. Usa un algoritmo de búsqueda.
4. Ejecuta las acciones encontradas.

## 6.2 Búsqueda de Soluciones
Un problema de búsqueda se define por cinco elementos:
- **Estado inicial:** punto de partida.
- **Acciones:** movimientos posibles.
- **Modelo de transición:** describe los resultados de las acciones.
- **Prueba de meta:** determina si se alcanzó el objetivo.
- **Costo del camino:** mide la calidad de la solución.

## 6.3 Estrategias de Búsqueda No Informada
Estas estrategias no tienen información sobre la meta, solo distinguen entre estado meta y no meta.

### Tipos principales:
- **BFS (Amplitud):** explora por niveles, encuentra el camino más corto.
- **DFS (Profundidad):** explora hasta el fondo antes de retroceder.
- **UCS (Costo Uniforme):** usa el menor costo acumulado.
- **IDS (Profundidad Iterativa):** combina BFS y DFS.

## 6.4 Evitar Estados Repetidos
Los algoritmos deben evitar bucles infinitos mediante una **lista cerrada** o conjunto de estados ya visitados.

## 6.5 Búsqueda con Información Parcial
Cuando el agente no conoce todo el entorno, utiliza **estados de creencia**, es decir, conjuntos de posibles estados.

## Ejercicio Práctico - Búsqueda en un Mapa de Bolivia
Implementación de un agente resolvente que encuentra rutas entre ciudades.

### Archivos del Proyecto
1. **mapa_bolivia.py:** define el grafo del mapa.
2. **busqueda_bfs.py:** implementa la búsqueda en amplitud.
3. **busqueda_dfs.py:** implementa la búsqueda en profundidad.
4. **comparacion_busquedas.py:** ejecuta y compara ambos algoritmos.

### Resultados
- **BFS:** encontró la ruta *La Paz ➔ Beni ➔ Santa Cruz ➔ Chuquisaca ➔ Tarija* (óptima).
- **DFS:** encontró otra ruta válida, pero más larga.

## Conclusión
BFS garantiza soluciones óptimas pero consume más memoria, mientras que DFS es más rápido pero menos óptimo. Ambos ilustran la base de los métodos de **búsqueda no informada** en inteligencia artificial.
