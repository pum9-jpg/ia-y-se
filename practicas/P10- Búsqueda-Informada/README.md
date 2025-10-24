# Algoritmos de Búsqueda de Rutas en Bolivia (UCS y A*)

Este proyecto implementa y compara dos algoritmos de búsqueda, la **Búsqueda de Costo Uniforme (UCS)** y el algoritmo **A\***, para encontrar la ruta óptima con menor distancia entre ciudades de Bolivia.

## 🛠️ Herramientas Necesarias (Requisitos)

Para poder ejecutar el código Python, necesitarás el siguiente software instalado en tu sistema:

1.  **Python 3:** El código está escrito en Python y se recomienda la versión 3.x.
2.  **Módulos de Python:**
    * **`math`**: Módulo estándar de Python, usado para la función `math.sqrt` en la heurística.
    * **`heapq`**: Módulo estándar de Python, usado para implementar la cola de prioridad en ambos algoritmos.

**Instalación (si no tienes Python 3):**

Puedes descargar la última versión de Python desde [python.org](https://www.python.org/).

**Verificación de Módulos:**

Dado que `math` y `heapq` son módulos de la librería estándar de Python, no se requiere una instalación adicional con `pip`. Si el entorno de Python funciona correctamente, ambos módulos estarán disponibles.

## 🏃 Cómo Correr el Programa

1.  **Guarda el código:** Copia el código transcrito en un archivo llamado, por ejemplo, `busqueda_rutas.py`.
2.  **Ejecuta desde la terminal:** Abre tu terminal o línea de comandos, navega hasta el directorio donde guardaste el archivo y ejecuta el comando:

    ```bash
    python busqueda_rutas.py
    ```

## 📝 Conclusiones de los Resultados

El programa ejecuta ambos algoritmos de búsqueda (UCS y A\*) para encontrar la ruta más corta desde **'La Paz'** hasta **'Tarija'** en el mapa definido (`mapa_bolivia_mejorado`). La métrica clave de comparación es la cantidad de **nodos expandidos** (ciudades visitadas) por cada algoritmo.

### 1. Ruta Óptima y Costo Total

* Ambos algoritmos, **UCS** (no informada) y **A\*** (informada y admisible), garantizan encontrar el **camino óptimo** con el **mínimo costo** (menor distancia en kilómetros).
* El camino y el costo total del viaje serán idénticos para ambos.

### 2. Comparación de Eficiencia (Nodos Expandidos)

El principal objetivo de A\* es ser **más eficiente** que UCS.

| Algoritmo | Tipo de Búsqueda | Métrica Principal |
| :---: | :---: | :---: |
| **UCS** | **No Informada** | Minimiza $g(n)$ (costo actual) |
| **A\*** | **Informada** | Minimiza $f(n) = g(n) + h(n)$ (costo total estimado) |

* **UCS (Costo Uniforme):** Expande los nodos en orden de