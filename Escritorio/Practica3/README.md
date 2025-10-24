# Sistema Experto para Diagnóstico de Bicicletas 🚲🧠

Este script de Python simula un **Sistema Experto basado en Reglas de Producción** para diagnosticar problemas comunes en una bicicleta y sugerir soluciones. La lógica se ejecuta en dos fases secuenciales: primero, se encuentra un diagnóstico, y luego, se busca una solución para ese diagnóstico.

## 💡 Conceptos Clave

1.  **BASE DE CONOCIMIENTO (Reglas)**: Se divide en dos diccionarios:
    * `base_conocimiento_reglas`: Asocia **síntomas** (`"si"`) con un **diagnóstico** (`"entonces"`).
    * `base_conocimiento_soluciones`: Asocia un **diagnóstico** (`"si"`) con una **solución** (`"entonces"`).
2.  **HECHOS (`hechos_usuario`)**: Es la lista de síntomas que proporciona el usuario (ej. `["llanta_blanda"]`).
3.  **MOTOR DE INFERENCIA (`diagnosticar_con_reglas`)**: Aplica un proceso de **Encadenamiento Hacia Adelante** (Forward Chaining).

---

## 🚀 ¿Cómo funciona el Motor de Inferencia?

La función `diagnosticar_con_reglas` trabaja en dos etapas:

1.  **Diagnóstico**: Itera sobre `base_conocimiento_reglas`. Para una regla, verifica si **todos** sus síntomas requeridos (`"si"`) están presentes en los `hechos_usuario`. Si encuentra una coincidencia, establece el `diagnostico` y detiene la búsqueda.
2.  **Solución**: Si se encontró un `diagnostico`, itera sobre `base_conocimiento_soluciones` para encontrar una regla donde la condición (`"si"`) sea el diagnóstico recién encontrado. Devuelve la **solución** asociada.

---

## ⚙️ Requisitos

Necesitas tener **Python** instalado en tu computadora (versión 3.x recomendada).

---

## 🏃‍♂️ Ejecución Rápida

Sigue estos pasos para ejecutar el script:

### 1. Guarda el Código
Copia todo el código Python y guárdalo en un archivo llamado, por ejemplo, `diagnostico_bici.py`.

### 2. Abre la Terminal
Abre tu Terminal, Símbolo del sistema o PowerShell.

### 3. Ejecuta el Script
Navega a la carpeta donde guardaste el archivo y usa el siguiente comando:

```bash
python diagnostico_bici.py
# O, si usas la versión 3:
python3 diagnostico_bici.py
