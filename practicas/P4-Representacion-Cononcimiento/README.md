# Sistemas Expertos: Reglas de Producción y Marcos (Frames)

Este proyecto demuestra dos métodos fundamentales para la **representación del conocimiento** en sistemas de Inteligencia Artificial: **Reglas de Producción** y **Marcos (Frames)**. Ambos implementan un sistema de diagnóstico simple en **Python**.

## 1. Sistema Basado en Reglas de Producción ⚙️

Este enfoque utiliza un **motor de inferencia** que aplica lógica "SI-ENTONCES" (IF-THEN) para encadenar síntomas a un diagnóstico y, posteriormente, a una solución.

### Estructura del Conocimiento

El conocimiento se almacena en diccionarios de reglas:

| Base de Conocimiento | Propósito | Ejemplo de Regla |
| :--- | :--- | :--- |
| `base_conocimiento_reglas` | Diagnóstico (Síntomas → Problema) | **SI:** `["llanta blanda"]` **ENTONCES:** `"diagnostico_ponchadura"` |
| `base_conocimiento_soluciones` | Solución (Problema → Acción) | **SI:** `["diagnostico_ponchadura"]` **ENTONCES:** `"solucion_parchar_o_cambiar_tubo"` |

### Proceso de Inferencia

Se utiliza **Encadenamiento Hacia Adelante** (*Forward Chaining*):
1.  El sistema toma los **hechos del usuario** (síntomas).
2.  Busca una regla de diagnóstico donde **TODAS** las condiciones (`"si"`) coincidan con los hechos.
3.  Si se encuentra un diagnóstico, busca la regla de solución que coincida con ese diagnóstico.

---

## 2. Sistema Basado en Marcos (Frames) 🖼️

Los **Marcos** son estructuras de datos orientadas a objetos que representan conceptos o problemas del dominio mediante **slots** (atributos) y sus valores.

### Estructura del Conocimiento

Todo el conocimiento está en el diccionario `base_conocimiento_frames`. Cada clave es un **Frame** (el problema) y su valor es otro diccionario con sus **slots**:

| Slot (Atributo) | Descripción | Ejemplo de Valor |
| :--- | :--- | :--- |
| `es_un` | Clasificación jerárquica. | `"problema_de_transmision"` |
| `sintomas` | Lista de síntomas requeridos. | `["chasquido_al_pedalear", "cadena_salta"]` |
| `solucion` | Acción correctiva. | `"reemplazar_cadena"` |
| `herramientas_necesarias` | Recursos necesarios. | `["cortacadenas", "cadena_nueva"]` |

### Proceso de Consulta

La función `buscar_problema_por_sintoma` itera a través de los Marcos para encontrar aquel cuyo slot `"sintomas"` contenga **todos** los síntomas reportados por el usuario. Una vez identificado el Frame, se pueden consultar directamente todos sus atributos.

---

## Uso y Ejecución

Para ejecutar los ejemplos, asegúrate de haber definido las estructuras de conocimiento (`base_conocimiento_reglas`, `base_conocimiento_soluciones`, `base_conocimiento_frames`) y las funciones (`diagnosticar_con_reglas`, `buscar_problema_por_sintoma`) en un script de Python.

**Ejemplo de Hechos de Prueba (Ambos Sistemas):**
```python
hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]