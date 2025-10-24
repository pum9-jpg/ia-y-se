# Sistema Experto de Diagnóstico con Marcos (Frames) 🖼️

Este script demuestra un **Sistema Experto** que utiliza **Marcos (Frames)** para representar el conocimiento. En lugar de usar reglas tipo "SI... ENTONCES...", el conocimiento se organiza en **objetos** con propiedades bien definidas (slots). Esto es genial para describir cosas en detalle, como problemas, piezas, o herramientas.

## 💡 Conceptos Clave

1.  **BASE DE CONOCIMIENTO (`base_conocimiento_frames`)**: Es el diccionario central. Cada clave principal (`"ponchadura"`, `"cadena_desgastada"`) es un **Frame** (o Marco).
2.  **SLOTS (Atributos)**: Son las claves dentro de cada Frame (ej. `"sintomas"`, `"solucion"`, `"herramientas_necesarias"`). Describen las características del problema.
3.  **FUNCIÓN DE BÚSQUEDA (`buscar_problema_por_sintoma`)**: Actúa como un motor de consulta que busca un Frame que coincida con los síntomas del usuario. Una vez que encuentra el Frame, puede acceder a toda la información asociada (solución, herramientas, tipo, etc.).

---

## 🚀 ¿Cómo funciona el Motor de Consulta?

La función `buscar_problema_por_sintoma` recorre cada Frame en la base de conocimiento:

* Para cada problema (Frame), verifica si **todos** los síntomas que el usuario reportó (`hechos_usuario`) están incluidos en el slot `"sintomas"` de ese Frame.
* Si encuentra un Frame que contenga todos los síntomas reportados, devuelve el nombre del problema y todos sus detalles. Esto permite recuperar de golpe toda la información de diagnóstico y solución.

---

## ⚙️ Requisitos

Necesitas tener **Python** instalado en tu computadora (versión 3.x recomendada).

---

## 🏃‍♂️ Ejecución Rápida

Sigue estos pasos para ejecutar el script:

### 1. Guarda el Código
Copia todo el código Python y guárdalo en un archivo llamado, por ejemplo, `diagnostico_frames.py`.

### 2. Abre la Terminal
Abre tu Terminal, Símbolo del sistema o PowerShell.

### 3. Ejecuta el Script
Navega a la carpeta donde guardaste el archivo y usa el siguiente comando:

```bash
python diagnostico_frames.py
# O, si usas la versión 3:
python3 diagnostico_frames.py
