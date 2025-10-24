# Sistema Experto de Recomendación de Bebidas (Basado en Reglas) ☕🧠

Este script demuestra un **Sistema Experto** simple que recomienda una bebida. La clave de este enfoque es la **separación** de la lógica (las reglas) del mecanismo que aplica esa lógica (el motor de inferencia).

## 💡 Conceptos Clave

1.  **BASE DE CONOCIMIENTO (El "qué")**: Es una lista de diccionarios (reglas). Cada regla define un conjunto de condiciones (`"si"`) y una única conclusión (`"entonces"`). Es la parte que contiene el "conocimiento" sobre las bebidas.
2.  **MOTOR DE INFERENCIA (El "cómo")**: Es la función (`motor_de_inferencia`) que recorre las reglas y compara sus condiciones (`"si"`) con los hechos proporcionados por el usuario. Su trabajo es encontrar la primera regla que coincida completamente.

## 🚀 ¿Cómo funciona?

La función `motor_de_inferencia` toma los **hechos** (preferencias del usuario) y la **base de conocimiento** (las reglas) y las evalúa una por una.

* Para cada regla, verifica si *todos* los pares clave-valor de la condición (`"si"`) se encuentran y coinciden en los `hechos_usuario`.
* Si una regla coincide completamente, detiene la búsqueda y devuelve el valor de su conclusión (`"entonces"`).

---

## ⚙️ Requisitos

Necesitas tener **Python** instalado en tu computadora (versión 3.x recomendada).

---

## 🏃‍♂️ Ejecución Rápida

Sigue estos pasos para ejecutar el script:

### 1. Guarda el Código
Copia todo el código Python (incluyendo la Base de Conocimiento y la función) y guárdalo en un archivo llamado, por ejemplo, `sistema_experto.py`.

### 2. Edita y Completa la Ejecución
El ejemplo de uso al final del código está comentado y solo tiene la definición de los hechos. **Debes añadir las líneas de ejecución para ver el resultado.**

Asegúrate de que tu archivo `sistema_experto.py` se vea así al final:

```python
# - Ejemplo de uso -
hechos_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

# La llamada a la función para obtener la recomendación estaría aquí:
recomendacion = motor_de_inferencia(hechos_usuario, base_de_conocimiento)
print(f"Enfoque SE: {recomendacion}") # Añade esta línea
