# 🗺️ Búsqueda de Rutas en un Mapa Simplificado de Bolivia

## 📘 Descripción General

Este programa implementa un **grafo no dirigido** que representa un mapa simplificado de Bolivia.  
Cada ciudad está conectada con aquellas que tienen una relación directa (por ejemplo, carreteras o rutas).  
Se implementan dos algoritmos clásicos de búsqueda en grafos:

1. **Búsqueda en Amplitud (BFS)** → encuentra el camino más corto entre dos ciudades.  
2. **Búsqueda en Profundidad (DFS)** → encuentra un camino cualquiera, explorando lo más profundo posible antes de retroceder.

---

## 🧩 Representación del Mapa

El mapa se define como un **diccionario de listas**, donde cada clave es una ciudad y su valor son las ciudades vecinas directamente conectadas.

```python
mapa_bolivia = {
    'La Paz': ['Oruro', 'Beni'],
    'Oruro': ['La Paz', 'Cochabamba', 'Potosi'],
    'Cochabamba': ['Oruro', 'Santa Cruz', 'Chuquisaca', 'Beni'],
    'Potosi': ['Oruro', 'Chuquisaca', 'Tarija'],
    'Chuquisaca': ['Cochabamba', 'Potosi', 'Santa Cruz', 'Tarija'],
    'Santa Cruz': ['Cochabamba', 'Chuquisaca', 'Beni'],
    'Tarija': ['Potosi', 'Chuquisaca'],
    'Beni': ['La Paz', 'Cochabamba', 'Santa Cruz'],
    'Pando': []  # Pando está aislado en este mapa simplificado
}
```

📍 **Nota:** Pando se deja sin conexiones para ilustrar el caso de una ciudad aislada.

---

## 🔍 Función: `busqueda_amplitud()`

Esta función implementa el algoritmo **Breadth-First Search (BFS)**.  
Busca el camino más corto desde una ciudad inicial hasta una ciudad destino.

### 🔧 Lógica:
1. Se utiliza una **cola (`deque`)** para explorar las ciudades por niveles.  
2. Se guarda un conjunto `visitados` para evitar repetir estados.  
3. En cada iteración:
   - Se toma el primer camino de la cola.
   - Se verifica si la ciudad actual es la meta.
   - Se agregan sus vecinos no visitados a la cola.

```python
def busqueda_amplitud(mapa, inicio, fin):
    cola = deque([[inicio]])
    visitados = {inicio}

    while cola:
        camino = cola.popleft()
        ciudad_actual = camino[-1]

        if ciudad_actual == fin:
            return camino

        for vecino in mapa.get(ciudad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return "No se encontró un camino."
```

✅ **Ventaja:** garantiza el camino más corto.  
⚠️ **Desventaja:** puede usar más memoria en grafos grandes.

---

## 🔍 Función: `busqueda_profundidad()`

Implementa el algoritmo **Depth-First Search (DFS)**.  
Explora lo más profundo posible antes de retroceder.

### 🔧 Lógica:
1. Usa una **pila (lista con `pop()`)** para almacenar los caminos.
2. Guarda las ciudades visitadas en un conjunto.
3. En cada paso:
   - Se toma el último camino de la pila.
   - Se comprueba si la ciudad actual es la meta.
   - Se agregan sus vecinos no visitados a la pila.

```python
def busqueda_profundidad(mapa, inicio, fin):
    pila = [[inicio]]
    visitados = {inicio}

    while pila:
        camino = pila.pop()
        ciudad_actual = camino[-1]

        if ciudad_actual == fin:
            return camino

        for vecino in mapa.get(ciudad_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                pila.append(nuevo_camino)

    return "No se encontró un camino."
```

✅ **Ventaja:** menor consumo de memoria.  
⚠️ **Desventaja:** no garantiza el camino más corto.

---

## ▶️ Ejecución del Programa

En la parte final del archivo se define el punto de partida y destino, y se ejecutan ambos algoritmos:

```python
ciudad_inicio = 'La Paz'
ciudad_destino = 'Tarija'

print(f"Buscando ruta de '{ciudad_inicio}' a '{ciudad_destino}'.\n")

# Búsqueda en amplitud
camino_bfs = busqueda_amplitud(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' ➜ '.join(camino_bfs)}")
print(f"Número de paradas: {len(camino_bfs) - 1}\n")

# Búsqueda en profundidad
camino_dfs = busqueda_profundidad(mapa_bolivia, ciudad_inicio, ciudad_destino)
print(f"Camino encontrado: {' ➜ '.join(camino_dfs)}")
print(f"Número de paradas: {len(camino_dfs) - 1}")
```

---

## 🧠 Ejemplo de Salida

```text
Buscando ruta de 'La Paz' a 'Tarija'.

   → Usando Búsqueda en Amplitud (BFS) ←
Camino encontrado: La Paz ➜ Oruro ➜ Potosi ➜ Tarija
Número de paradas: 3

   → Usando Búsqueda en Profundidad (DFS) ←
Camino encontrado: La Paz ➜ Oruro ➜ Cochabamba ➜ Chuquisaca ➜ Tarija
Número de paradas: 4
```

---

## 💻 Ejecución

### 🔧 Requisitos
- Python 3.8 o superior
- Módulo estándar `collections` (ya incluido)

### 🚀 Pasos para ejecutar
1. Guarda el código en un archivo llamado `busqueda_mapa.py`.
2. Abre la terminal o consola en el directorio donde guardaste el archivo.
3. Ejecuta el siguiente comando:

```bash
python busqueda_mapa.py
```

### 💡 Nota
Cada ejecución puede producir diferentes caminos dependiendo de cómo estén conectadas las ciudades.

---

## Conclusión

* El programa muestra cómo se pueden usar los algoritmos de búsqueda en grafos para encontrar rutas entre ciudades.
* Mediante BFS y DFS, se comparan dos formas de recorrer el mapa de Bolivia, una buscando el camino más corto y otra explorando más a fondo. Es un ejemplo claro y sencillo de cómo aplicar la teoría de grafos en un problema real 
