# 🧭 Búsqueda de Rutas Óptimas en Bolivia 🇧🇴

Este proyecto implementa **dos algoritmos clásicos de Inteligencia Artificial (IA)** para la búsqueda de rutas entre ciudades bolivianas:
- **Búsqueda de Costo Uniforme (UCS)**: un algoritmo no informado que garantiza la ruta más corta.  
- **Búsqueda A\*** (A estrella): un algoritmo informado que combina el costo recorrido y una heurística para optimizar la búsqueda.

---

## ⚙️ Requisitos para compilar y ejecutar el código

### 🧩 Requisitos previos
1. Tener instalado **Python 3.10 o superior**.
2. Asegurarse de que todos los archivos estén en la misma carpeta:
   - `main.py`
   - `mapa.py`
   - `busqueda_costo_uniforme.py`
   - `busqueda_a_estrella.py`
3. No requiere librerías externas.
4. Para ejecutar el programa, abrir la terminal en la carpeta del proyecto y escribir:

```bash
python main.py
```

---

## 🧱 Explicación detallada del código

### 🗺️ 1. `mapa.py`
Define la **representación del mapa de Bolivia** como un **grafo ponderado**.  
Cada ciudad es un nodo, y las conexiones (carreteras) entre ciudades son las aristas con sus respectivos kilómetros.

Ejemplo de estructura:
```python
mapa_bolivia_mejorado = {
    "La Paz": {"Oruro": 230, "Cochabamba": 380},
    "Oruro": {"Potosí": 320, "Sucre": 450},
    ...
}
```
También contiene las **coordenadas aproximadas** de cada ciudad, usadas por la heurística del algoritmo A\*.  
Además, define la función `heuristica_distancia_recta(ciudad_a, ciudad_b)` que calcula la distancia estimada entre dos ciudades (basada en sus coordenadas).

---

### 🔍 2. `busqueda_costo_uniforme.py`
Implementa el algoritmo **Uniform Cost Search (UCS)**.  
Este algoritmo utiliza una **cola de prioridad** que siempre expande el camino con el menor costo acumulado.

Flujo básico:
1. Empieza desde la ciudad de origen.
2. En cada paso, expande la ciudad con el menor costo total.
3. Si encuentra la ciudad destino, devuelve el camino, el costo total y cuántas ciudades analizó.

Fragmento clave:
```python
for vecino, distancia in mapa[ciudad_actual].items():
    nuevo_costo = costo_actual + distancia
    ...
```
Esto asegura que cada vecino se evalúe sumando la distancia total recorrida hasta ese punto.

---

### 🌟 3. `busqueda_a_estrella.py`
Implementa el algoritmo **A\*** (A estrella).  
A diferencia del UCS, este utiliza una **heurística informada** que estima la distancia restante al destino.

Fórmula usada:
```
f(n) = g(n) + h(n)
```
Donde:
- `g(n)` = costo acumulado real del camino.
- `h(n)` = estimación heurística (distancia recta al destino).

Esto permite encontrar la mejor ruta más rápido, ya que prioriza los caminos más prometedores.

Fragmento principal:
```python
costo_h = heuristica_distancia_recta(vecino, fin)
nuevo_costo_total = costo_g + costo_h
```
Aquí se combina el costo recorrido (`costo_g`) con la heurística (`costo_h`).

---

### 🚀 4. `main.py`
Coordina la ejecución de los algoritmos.  
Define el punto de inicio y destino, ejecuta ambos métodos y muestra los resultados.

```python
ciudad_inicio = "La Paz"
ciudad_destino = "Tarija"

camino_ucs, costo_ucs, expandidos_ucs = busqueda_costo_uniforme(mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
camino_a_estrella, costo_a_estrella, expandidos_a_estrella = busqueda_a_estrella(mapa_bolivia_mejorado, ciudad_inicio, ciudad_destino)
```
Finalmente imprime los resultados comparando ambos algoritmos.

---

## 💡 Salida esperada

Al ejecutar `main.py`, el programa muestra algo similar a lo siguiente:

```
Buscando la ruta más corta de 'La Paz' a 'Tarija'.

-     Usando Búsqueda de Costo Uniforme (UCS) -
Camino encontrado: La Paz → Oruro → Potosí → Tarija
Costo total del viaje: 905 km
Ciudades (nodos) expandidas: 8

-     Usando Búsqueda A* (Informada) -
Camino encontrado: La Paz → Cochabamba → Sucre → Tarija
Costo total del viaje: 870 km
Ciudades (nodos) expandidas: 5
```

Esto demuestra que A\* es más eficiente (menos ciudades analizadas) al usar información heurística.

---

## 🧩 Conclusión

Este proyecto llega a mostrar cómo los algoritmos de búsqueda informada y no informada pueden encontrar rutas entre ciudades de Bolivia. UCS garantiza la ruta más corta pero explora más nodos, mientras que A* llega a usar heurísticas para ser más rápido y eficiente. La comparación llega a demostrar cómo una buena heurística nos permite tomar decisiones más inteligentes, optimizando tiempo y recursos en problemas de planificación de rutas.