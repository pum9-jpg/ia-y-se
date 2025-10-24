# Recomendador Convencional de Bebidas 🍹

Este es un simple script en Python que **recomienda una bebida** basándose en la hora del día, si el usuario quiere cafeína y si prefiere algo dulce. Toda la **lógica de negocio** (las reglas para la recomendación) está escrita directamente en una función dentro del código.

## 🚀 ¿Cómo funciona?

El programa tiene una función llamada `recomendar_bebida_convencional` que toma tres parámetros del usuario:
1.  **`hora_del_dia`**: (ej. 'mañana', 'tarde', 'noche').
2.  **`preferencia_cafeina`**: (ej. 'si' o 'no').
3.  **`le_gusta_dulce`**: (ej. `True` o `False`).

La función utiliza una serie de sentencias `if`/`elif`/`else` (condiciones) anidadas para revisar estas preferencias y devolver la bebida que mejor se ajusta a ellas según la lógica predefinida.

### Ejemplo de Lógica Integrada

| Hora del Día | ¿Cafeína? | ¿Dulce? | Recomendación |
| :---: | :---: | :---: | :---: |
| **Mañana** | Sí | Sí | Mocha |
| **Mañana** | Sí | No | Americano |
| **Tarde** | No | Sí | Frappuccino sin café |
| **Noche** | No | Cualquier | Té de Manzanilla |

---

## ⚙️ Requisitos

Necesitas tener **Python** instalado en tu computadora (versión 3.x recomendada).

---

## 🏃‍♂️ Ejecución Rápida

Sigue estos sencillos pasos para probar el código:

### 1. Guarda el Código
Copia el código Python en un archivo y guárdalo como, por ejemplo, `bebidas.py`.

### 2. Abre la Terminal
Abre tu Terminal, Símbolo del sistema o PowerShell.

### 3. Ejecuta el Script
Navega a la carpeta donde guardaste el archivo y usa el siguiente comando:

```bash
python bebidas.py
# O, si usas la versión 3:
python3 bebidas.py
```

