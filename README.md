# Unidad 7: Búsqueda Informada y Exploración

Esta unidad explica cómo los algoritmos de **búsqueda informada** utilizan conocimiento adicional (heurística) para guiar la exploración de soluciones de manera más eficiente.

## 7.1 Estrategias de búsqueda informada (Heurística)
La búsqueda informada emplea una función heurística que estima la distancia o costo restante hacia el objetivo.
- **Búsqueda Voraz (Greedy Best-First)**: Expande el nodo más prometedor según la heurística, sin considerar el costo real.
- **Búsqueda A***: Combina el costo real recorrido y la estimación heurística, garantizando soluciones óptimas si la heurística es admisible.

## 7.2 Funciones Heurísticas
Una función heurística (h(n)) estima el costo desde un nodo hasta la meta. Debe ser **admisible** (no sobrestimar el costo real).  
Ejemplo: distancia en línea recta entre dos ciudades.

## 7.3 Algoritmos de búsqueda local y optimización
Los algoritmos de búsqueda local operan en un solo estado, intentando mejorarlo:
- **Ascenso de colina (Hill Climbing)**: se mueve hacia el mejor vecino.
- **Recocido simulado (Simulated Annealing)**: introduce aleatoriedad para evitar quedar atrapado en máximos locales.

## 7.4 Búsqueda local en espacios continuos
Cuando los estados son valores continuos, se usa el **Descenso de Gradiente**, moviéndose en la dirección contraria al gradiente para minimizar el error.

## 7.5 Agentes de búsqueda online y ambientes desconocidos
Los agentes online exploran ambientes desconocidos, aprendiendo mientras actúan. Deben equilibrar **exploración** (probar nuevas acciones) y **explotación** (usar conocimiento actual).

## Ejercicio Práctico – Comparación UCS vs A*
Se implementan dos algoritmos sobre un mapa de Bolivia:
1. **UCS (Costo Uniforme)**: búsqueda no informada.
2. **A***: búsqueda informada con heurística (distancia euclidiana).

### Resultados esperados:
- Ambos hallan el camino óptimo La Paz ➔ Oruro ➔ Potosí ➔ Tarija (905 km).
- A* expande menos nodos (mayor eficiencia).

## Conclusión
Las estrategias informadas como A* mejoran drásticamente la eficiencia al guiar la búsqueda mediante heurísticas, reduciendo el espacio explorado y el tiempo de cómputo.
