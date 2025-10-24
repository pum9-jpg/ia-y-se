# Sistema de Razonamiento Deductivo Simple (Clasificación de Animales) 🐦🐠

Este script en Python simula un **Sistema Experto Deductivo** que clasifica un animal misterioso basándose en reglas generales. El sistema utiliza el **Encadenamiento Hacia Adelante** para inferir nuevos hechos a partir de los hechos iniciales del usuario.

---

## 💡 Conceptos Clave

1.  **BASE DE CONOCIMIENTO (`reglas_animales`)**: Contiene las reglas generales de clasificación (e.g., "Si tiene plumas, entonces es ave").
2.  **HECHOS (`hechos_especificos`)**: Los síntomas o atributos iniciales que se conocen del objeto (e.g., "tiene plumas" y "canta").
3.  **MOTOR DE INFERENCIA (`SistemaExpertoDeductivo.razonar`)**: La función que aplica las reglas de manera iterativa hasta que no se puede deducir ningún hecho nuevo, yendo de los hechos conocidos a las conclusiones.

---

## 🚀 ¿Cómo funciona el Razonamiento Deductivo?

El método de **Encadenamiento Hacia Adelante** trabaja así:

1.  **Inicialización**: La lista de hechos conocidos comienza con los hechos que el usuario proporciona.
2.  **Bucle de Inferencia**: El sistema revisa la lista de reglas repetidamente.
3.  **Activación de Reglas**: Si las condiciones (`"si"`) de una regla son un subconjunto de los hechos conocidos, la regla se activa y su conclusión (`"entonces"`) se **añade** a los hechos conocidos.
4.  **Conclusión**: El proceso continúa hasta que ninguna regla puede añadir un hecho nuevo. La clasificación final es uno de los hechos deducidos (los que empiezan por `"es_"`).

**En el Ejemplo (`{"tiene_plumas", "canta"}`):**
1.  **Paso 1**: Se cumplen las condiciones de `{"si": ["tiene_plumas"], "entonces": "es_ave"}`. Se añade **"es_ave"**.
2.  **Paso 2**: Ahora se cumplen las condiciones de `{"si": ["es_ave", "canta"], "entonces": "es_canario"}`. Se añade **"es_canario"**.
3.  **Final**: No se pueden añadir más hechos. La conclusión es "es_canario".

---

## ⚙️ Requisitos

Necesitas tener **Python** instalado en tu computadora (versión 3.x recomendada).

---

## 🏃‍♂️ Ejecución Rápida

Sigue estos pasos para ejecutar el script:

### 1. Guarda el Código
Copia todo el código Python y guárdalo en un archivo llamado, por ejemplo, `deductivo_simple.py`.

### 2. Abre la Terminal
Abre tu Terminal, Símbolo del sistema o PowerShell.

### 3. Ejecuta el Script
Navega a la carpeta donde guardaste el archivo y usa el siguiente comando:

```bash
python deductivo_simple.py
# O, si usas la versión 3:
python3 deductivo_simple.py
```
### Conclusión 
Este código demuestra de manera efectiva la transparencia y escalabilidad del razonamiento deductivo basado en reglas. La separación entre la Base de Conocimiento (las reglas) y el Motor de Inferencia (el método razonar) es la característica más valiosa. Permite que los expertos modifiquen, añadan o eliminen reglas de clasificación (como añadir un nuevo tipo de ave o pez) sin necesidad de cambiar ni una sola línea del código del motor. Esto hace que el sistema sea fácil de mantener y expandir para clasificar muchos más objetos o fenómenos.
