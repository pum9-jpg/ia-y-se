# Resolución de Problemas Mediante Búsquedas
---
## 🧩 Descripción General  

Este programa implementa dos algoritmos de búsqueda —**Búsqueda en Amplitud (BFS)** y **Búsqueda en Profundidad (DFS)**— para encontrar rutas entre ciudades de Bolivia representadas como un **grafo no dirigido**.  

Cada ciudad es un **nodo**, y las conexiones entre ellas son **aristas** que representan carreteras directas.  

El objetivo del programa es **encontrar un camino desde una ciudad inicial hasta una ciudad destino**, mostrando los pasos y el número total de paradas intermedias.

---

## ⚙️ Requisitos para Ejecutar el Código  

### 1. Instalación de Python  
Asegúrate de tener instalado **Python 3.7 o superior**.  
Puedes verificarlo ejecutando en la terminal:  

```bash
python --version
```

Si no lo tienes, descárgalo desde:  
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Crear el archivo del programa  
Copia el código completo en un archivo llamado, por ejemplo:  

```
busqueda_ciudades.py
```

### 3. Ejecutar el programa  
Abre una terminal en la carpeta donde guardaste el archivo y ejecuta:  

```bash
python busqueda_ciudades.py
```

El programa mostrará los resultados de la búsqueda en amplitud y en profundidad.  

---

## 🧠 Funcionamiento del Código  

### 1. Representación del Mapa  
El mapa se modela como un **diccionario (grafo)**, donde cada clave es una ciudad y su valor es una lista de las ciudades conectadas directamente.  

```python
mapa_bolivia = {
    'La Paz': ['Oruro', 'Beni'],
    'Oruro': ['La Paz', 'Cochabamba', 'Potosi'],
    ...
}
```

Este enfoque permite recorrer las conexiones entre ciudades de manera eficiente.

---

### 2. Algoritmo de **Búsqueda en Amplitud (BFS)**  

La función `busqueda_amplitud()` utiliza una **cola (`deque`)** para explorar primero las rutas más cortas.  
Sigue un proceso de **exploración por niveles**, garantizando encontrar el **camino más corto** en términos de número de paradas.

**Etapas del algoritmo:**  
1. Se inicia desde la ciudad de origen.  
2. Se exploran todas las ciudades vecinas (nivel 1).  
3. Luego las ciudades conectadas a esas vecinas (nivel 2), y así sucesivamente.  
4. Cuando se encuentra el destino, se retorna el camino completo.

```python
cola = deque([[inicio]])
visitados = {inicio}
```

---

### 3. Algoritmo de **Búsqueda en Profundidad (DFS)**  

La función `busqueda_profundidad()` utiliza una **pila** para explorar primero los caminos más profundos.  
Este método no garantiza el camino más corto, pero encuentra **una posible ruta válida**.

**Etapas del algoritmo:**  
1. Se parte desde la ciudad inicial.  
2. Se avanza lo más profundo posible por un camino.  
3. Si se llega a un punto sin salida, se retrocede (“backtracking”).  
4. Se repite hasta hallar el destino o agotar las opciones.

```python
pila = [[inicio]]
visitados = {inicio}
```

---

### 4. Ejecución Principal  

El código define las ciudades de inicio y destino:

```python
ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'
```

Luego ejecuta ambos algoritmos y muestra los resultados:  

```python
print("→ Usando Búsqueda en Amplitud (BFS) ←")
print("→ Usando Búsqueda en Profundidad (DFS) ←")
```

**Salida esperada (ejemplo):**  
```
Buscando ruta de 'La Paz' a 'Tarija'.

→ Usando Búsqueda en Amplitud (BFS) ←
Camino encontrado: La Paz ➜ Oruro ➜ Potosi ➜ Tarija
Número de paradas: 3

→ Usando Búsqueda en Profundidad (DFS) ←
Camino encontrado: La Paz ➜ Oruro ➜ Cochabamba ➜ Chuquisaca ➜ Tarija
Número de paradas: 4
```

---

## 🧾 Conclusión  

Este programa aplica los algoritmos de búsqueda BFS y DFS para resolver problemas de rutas en un grafo que representa el mapa de Bolivia.
Permite observar cómo cada método ofrece estrategias distintas de exploración, siendo BFS ideal para el camino más corto y DFS útil para explorar todas las rutas posibles.
