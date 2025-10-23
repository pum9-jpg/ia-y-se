# 🧹 Simulación del Mundo de la Aspiradora

## 📘 Descripción General

Este programa implementa una simulación clásica del **mundo de la aspiradora**, un problema introductorio en el campo de la **Inteligencia Artificial**.  
El objetivo es comparar el desempeño de dos tipos de agentes:

1. **Agente Reactivo Simple** → actúa únicamente según su percepción inmediata.  
2. **Agente Basado en Modelos** → utiliza un modelo interno del entorno para decidir mejor sus acciones.

La simulación se desarrolla en un entorno con **dos habitaciones (A y B)**, que pueden estar **limpias o sucias**.  
El agente se mueve, aspira y obtiene una puntuación de rendimiento según sus acciones.

---

## ⚙️ Estructura del Código

El código está compuesto por **tres clases principales** y una sección de ejecución.

### 1. `EntornoAspiradora`
Representa el entorno donde se mueve el agente.

#### Atributos
- `estado_habitaciones`: diccionario con el estado de cada habitación (`Limpia` o `Sucia`).
- `ubicacion_agente`: indica si el agente está en la habitación A o B.
- `pasos`: número de acciones ejecutadas.
- `rendimiento`: puntuación total acumulada.

#### Métodos
- `obtener_percepcion()`: devuelve la percepción actual `(ubicación, estado)`.
- `ejecutar_accion(accion)`: aplica la acción del agente y actualiza el entorno y el rendimiento.
- `esta_limpio()`: verifica si todas las habitaciones están limpias.
- `simular(agente, max_pasos=10)`: ejecuta la simulación completa hasta que el entorno esté limpio o se alcance el número máximo de pasos.

#### Reglas de rendimiento
| Acción | Condición | Cambio en rendimiento |
|--------|------------|-----------------------|
| `aspirar` | Si la habitación está sucia | +10 |
| `aspirar` | Si la habitación ya está limpia | -1 |
| `ir_a_B` o `ir_a_A` | Movimiento entre habitaciones | -1 |
| `no_hacer_nada` | No afecta el rendimiento | 0 |

---

### 2. `AgenteReactivoSimple`
Decide su acción solo según la percepción actual, sin recordar estados pasados.

#### Lógica de decisión:
1. Si la habitación está sucia → **aspira**  
2. Si está limpia y está en A → **va a B**  
3. Si está limpia y está en B → **va a A**

---

### 3. `AgenteBasadoEnModelos`
Mantiene un **modelo interno del entorno** (qué sabe de cada habitación) y decide con base en esa información.

#### Lógica de decisión:
1. Actualiza el modelo con la percepción actual.  
2. Si la habitación actual está sucia → **aspira**.  
3. Si sabe que alguna habitación está sucia → **se dirige hacia ella**.  
4. Si todo está limpio → **no hace nada**.  

Este agente tiene memoria y puede evitar acciones innecesarias.

---

## ▶️ Ejecución de la Simulación

En la parte final del archivo se ejecutan dos simulaciones independientes:

```python
print("\n--- Probando Agente Reactivo Simple ---")
entorno1 = EntornoAspiradora()
agente1 = AgenteReactivoSimple()
entorno1.simular(agente1)

print("\n--- Probando Agente Basado en Modelos ---")
entorno2 = EntornoAspiradora()
agente2 = AgenteBasadoEnModelos()
entorno2.simular(agente2)
```

Cada agente comienza con un entorno generado aleatoriamente y se ejecuta hasta 10 pasos como máximo.

---

## 🧩 Ejemplo de Salida

```text
--- Probando Agente Reactivo Simple ---
Estado Inicial: {'A': 'Sucia', 'B': 'Limpia'}, Agente en: A

Paso 1: Percepción: ('A', 'Sucia'), Acción: aspirar
Paso 2: Percepción: ('A', 'Limpia'), Acción: ir_a_B

Simulación terminada en 2 pasos.
Rendimiento Final: 9
Estado Final: {'A': 'Limpia', 'B': 'Limpia'}
```

---

## 💻 Compilación y Ejecución

Este código está escrito en **Python 3**, por lo que **no requiere compilación**.  
Solo necesitas tener Python instalado en tu sistema.

### 🔧 Requisitos
- Python 3.8 o superior
- Módulo estándar `random` (ya incluido en Python)

### 🚀 Ejecución
1. Guarda el código en un archivo llamado `aspiradora.py`.
2. Abre la terminal o consola en el directorio donde guardaste el archivo.
3. Ejecuta el siguiente comando:

```bash
python aspiradora.py
```

### 💡 Nota
Cada ejecución generará un entorno diferente debido al uso del módulo `random`.

---

## 🧠 Conclusión

Este experimento muestra cómo distintos tipos de agentes pueden actuar en un mismo entorno:
- El **agente reactivo** responde sin memoria, por lo que puede repetir errores.
- El **agente basado en modelos** recuerda lo que ha percibido, siendo más eficiente.

Ambos son ejemplos de **agentes inteligentes**, pero con distintos niveles de complejidad y desempeño.

---
