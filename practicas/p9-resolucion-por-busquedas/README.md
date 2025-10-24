# Búsqueda de Caminos en un Mapa de Bolivia

Este proyecto implementa algoritmos de búsqueda para encontrar rutas entre ciudades en un mapa simplificado de Bolivia. Se utilizan dos técnicas principales:

- **Búsqueda en Amplitud (BFS)**
- **Búsqueda en Profundidad (DFS)**

---

## Descripción

El mapa de Bolivia está representado como un grafo donde cada nodo es una ciudad y las aristas son conexiones directas entre ellas. El objetivo es encontrar un camino desde una ciudad de inicio hasta una ciudad destino utilizando los algoritmos BFS y DFS.

---

## Cómo funciona

- **BFS (Breadth-First Search)**: Explora los nodos en capas, primero todos los vecinos directos, luego los vecinos de esos vecinos, y así sucesivamente. Garantiza encontrar el camino más corto en términos de número de paradas.

- **DFS (Depth-First Search)**: Explora lo más profundo posible en una rama antes de retroceder y explorar otras. Puede encontrar caminos más largos y no garantiza el camino más corto.

---

## Comparación rápida

| Característica            | BFS                                           | DFS                                              |
|---------------------------|-----------------------------------------------|--------------------------------------------------|
| Garantiza el camino más corto | Sí                                            | No                                               |
| Uso de memoria            | Mayor (por la cola de nodos a explorar)      | Menor (por la pila de nodos en exploración)     |
| Tiempo de ejecución       | Similar en mapas pequeños                     | Similar en mapas pequeños                        |
| Tipo de camino encontrado | Caminos más cortos                            | Caminos potencialmente más largos              |
## Cómo correr el código en la consola

1. **Guardar el código**:
   - Copia todo el código proporcionado en un archivo llamado `busqueda.py`.

2. **Abrir la consola o terminal**:
   - En Windows: Abre CMD o PowerShell.
   - En macOS o Linux: Abre la terminal.

3. **Navegar hasta la carpeta donde guardaste el archivo**:
   - Usa el comando `cd` para cambiar de directorio. Por ejemplo:
     ```
     cd ruta/a/tu/carpeta
     ```
   - Reemplaza `ruta/a/tu/carpeta` por la ruta real donde guardaste `busqueda.py`.

4. **Ejecutar el script**:
   - Escribe y ejecuta:
     ```
     python busqueda.py
     ```
   - Asegúrate de tener Python instalado y configurado en tu PATH.

## Conclusión

Este ejemplo muestra cómo diferentes algoritmos de búsqueda pueden ser utilizados para resolver problemas de rutas en mapas. La elección entre BFS y DFS depende de si quieres el camino más corto o simplemente alguna ruta posible. Ambos algoritmos son fundamentales en ciencias de la computación y sistemas, y entenderlos ayuda a resolver problemas relacionados con grafos y redes.
