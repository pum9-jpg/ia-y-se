Búsqueda de Rutas - Algoritmos BFS y DFS
🗺️ Descripción
Este programa encuentra rutas entre ciudades de Bolivia usando dos algoritmos de búsqueda clásicos: BFS (Búsqueda en Amplitud) y DFS (Búsqueda en Profundidad).

🚀 Cómo Usar
bash
python busqueda_rutas.py
🔍 Algoritmos Implementados
BFS - Búsqueda en Amplitud
Explora por niveles (vecinos primero)

Garantiza el camino más corto

Usa cola (FIFO)

DFS - Búsqueda en Profundidad
Explora una ruta hasta el final

Encuentra solución rápida pero no óptima

Usa pila (LIFO)

📊 Ejemplo de Resultado
text
BFS: La Paz → Oruro → Potosi → Tarija (3 paradas)
DFS: La Paz → Beni → Santa Cruz → Chuquisaca → Tarija (4 paradas)

✅ Conclusión
Cuando ejecutamos el codigo podemos ver que BFS es mejor para encontrar el camino más corto, mientras que DFS es más rápido para encontrar cualquier solución. pero la elección del algoritmo depende del objetivoal que queremos llegar, si priorizamos la eficiencia (menos paradas) se usa BFS; si buscamos rapidez para encontrar cualquier ruta válida, usar DFS es mejor.

