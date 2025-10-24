# Simulación de Agentes Inteligentes: El Mundo de la Aspiradora 🧹

Este script de Python implementa el **Mundo de la Aspiradora (Vacuum World)** para simular y comparar la eficiencia de dos estructuras de Agentes Inteligentes: el **Reactivo Simple** (sin memoria) y el **Basado en Modelos** (con memoria).

## 💡 Conceptos Implementados y Comparación

| Estructura del Agente | Mecanismo Principal | Ventaja/Desventaja | Rendimiento Típico |
| :---: | :---: | :---: | :---: |
| **Agente Reactivo Simple** | Reglas SI-ENTONCES basadas en la **percepción actual**. | **Ineficiente.** Entra en bucles infinitos de movimiento si encuentra una habitación limpia, ya que no recuerda el estado previo. | Bajo |
| **Agente Basado en Modelos** | Mantiene un **modelo interno (memoria)** del estado de ambas habitaciones. | **Eficiente y Racional.** Evita acciones redundantes y se detiene cuando su modelo interno confirma que el objetivo está completo. | Alto |

---

## ⚙️ Estructura del Código

El código se divide en tres clases principales:

### 1. Entorno (`EntornoAspiradora`)
* Define el **Estado** del mundo (habitaciones A y B, `Limpias` o `Sucias`).
* Gestiona la **Percepción** del Agente y el impacto de sus **Acciones** (`aspirar`, `ir_a_A`, `ir_a_B`).
* Controla el **Rendimiento** (+10 por limpiar, -1 por moverse).

### 2. Agente Reactivo Simple (`AgenteReactivoSimple`)
* Su función `actuar` solo chequea: `SI [ubicacion]` y `SI [estado_habitacion]`. Si la habitación actual está limpia, siempre elige moverse.

### 3. Agente Basado en Modelos (`AgenteBasadoEnModelos`)
* Utiliza un slot (`self.modelo = {'A': 'Desconocido', 'B': 'Desconocido'}`) para **almacenar memoria**.
* Su `actuar` primero **actualiza** el modelo con la percepción y luego decide la acción basándose en el estado completo del modelo.

---

## 🏃‍♂️ Ejecución y Comparación

Para probar y comparar el rendimiento, sigue estos pasos:

### 1. Guarda el Código
Copia **todo el código completo** (las tres clases y el bloque de ejecución) en un archivo llamado `agentes_simulacion.py`.

### 2. Ejecuta el Script
Abre tu Terminal, navega a la carpeta del archivo y ejecuta:

```bash
python agentes_simulacion.py
# O, si usas la versión 3:
python3 agentes_simulacion.py

```
Salida Esperada
El script ejecutará dos simulaciones. Notarás que el Agente Basado en Modelos generalmente termina en muchos menos pasos y con un Rendimiento significativamente más alto que el Agente Reactivo Simple.

```bash

- Probando Agente Reactivo Simple -
... (muchos pasos)
Rendimiento final: [Número bajo debido a movimientos excesivos]

- Probando Agente Basado en Modelos -
... (pocos pasos)
Rendimiento final: [Número alto, cerca del máximo posible]

```
### Conclusión 
Este ejercicio demuestra que la memoria (Modelo Interno) es crucial para la racionalidad. El Agente Basado en Modelos es capaz de alcanzar su objetivo y detenerse, lo que resulta en un comportamiento más racional y eficiente en comparación con el agente reactivo, cuya falta de contexto (memoria) lo condena a gastar rendimiento en movimientos innecesarios.
