
# 🧠 Documentación: Sistemas Expertos en Python

Este documento describe dos enfoques distintos para la representación del conocimiento en sistemas expertos utilizando Python:  
**Reglas de Producción** y **Marcos (Frames)**.

---

## 🔹 1. Sistema Experto Basado en Reglas de Producción

### 📘 Descripción
Este enfoque utiliza una base de conocimiento compuesta por **reglas del tipo "si-entonces"**.  
El motor de inferencia compara los **hechos proporcionados por el usuario** con las condiciones de las reglas para deducir un diagnóstico y su posible solución.

### 💻 Código
```python
# Base de conocimiento: reglas de diagnóstico
base_conocimiento_reglas = {
    "regla_1": {
        "si": ["llanta_blanda"],
        "entonces": "diagnostico_ponchadura"
    },
    "regla_2": {
        "si": ["chasquido_al_pedalear", "cadena_salta"],
        "entonces": "diagnostico_cadena_desgastada"
    }
}

# Base de conocimiento: reglas de soluciones
base_conocimiento_soluciones = {
    "regla_3": {
        "si": ["diagnostico_ponchadura"],
        "entonces": "solucion_parchar_o_cambiar_tubo"
    },
    "regla_4": {
        "si": ["diagnostico_cadena_desgastada"],
        "entonces": "solucion_reemplazar_cadena"
    }
}

# Hechos proporcionados por el usuario
hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]

print("\n--- Usando Reglas de Producción ---\n")

def diagnosticar_con_reglas(hechos, reglas_diagnostico, reglas_solucion):
    diagnostico = None

    # Buscar un diagnóstico
    for nombre_regla, contenido in reglas_diagnostico.items():
        condiciones = contenido["si"]
        if all(condicion in hechos for condicion in condiciones):
            diagnostico = contenido["entonces"]
            print(f"Diagnóstico encontrado: {diagnostico}")
            break

    # Si se encontró un diagnóstico, buscar una solución
    if diagnostico:
        for nombre_regla, contenido in reglas_solucion.items():
            if contenido["si"][0] == diagnostico:
                solucion = contenido["entonces"]
                print(f"Solución encontrada: {solucion}")
                return
    else:
        print("No se pudo encontrar un diagnóstico con los síntomas proporcionados.")

# Ejecutar la función
diagnosticar_con_reglas(hechos_usuario, base_conocimiento_reglas, base_conocimiento_soluciones)
```

### 🧩 Funcionamiento
1. El sistema analiza los hechos del usuario.
2. Busca una regla cuyo conjunto de condiciones se cumpla.
3. Determina el diagnóstico.
4. Busca una regla de solución asociada a ese diagnóstico.
5. Muestra el resultado final.

### ✅ Ejemplo de salida
```
--- Usando Reglas de Producción ---

Diagnóstico encontrado: diagnostico_cadena_desgastada
Solución encontrada: solucion_reemplazar_cadena
```

---

## 🔹 2. Sistema Experto Basado en Marcos (Frames)

### 📘 Descripción
Este enfoque representa el conocimiento como **objetos con atributos** (similar a una estructura de datos).  
Cada *frame* contiene información detallada sobre un tipo de problema, sus síntomas, solución y herramientas necesarias.

### 💻 Código
```python
# Base de conocimiento: frames
base_conocimiento_frames = {
    "ponchadura": {
        "es_un": "problema_de_llanta",
        "sintomas": ["llanta_blanda"],
        "solucion": "parchar_o_cambiar_tubo",
        "herramientas_necesarias": ["bomba_de_aire", "parches", "pegamento"]
    },
    "cadena_desgastada": {
        "es_un": "problema_de_transmision",
        "sintomas": ["chasquido_al_pedalear", "cadena_salta"],
        "solucion": "reemplazar_cadena",
        "herramientas_necesarias": ["cortacadenas", "cadena_nueva"]
    }
}

print("\n--- Usando Marcos (Frames) ---\n")

def buscar_problema_por_sintomas(sintomas_usuario, base_de_datos):
    for problema, detalles in base_de_datos.items():
        if all(sintoma in detalles["sintomas"] for sintoma in sintomas_usuario):
            return problema, detalles
    return None, None

# Hechos del usuario
hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]

# Buscar problema en la base de conocimiento
problema_encontrado, detalles_problema = buscar_problema_por_sintomas(hechos_usuario, base_conocimiento_frames)

if problema_encontrado:
    print(f" Problema identificado: {problema_encontrado}")
    print(f"   - Es un tipo de: {detalles_problema['es_un']}")
    print(f"   - La solución es: {detalles_problema['solucion']}")
    print(f"   - Herramientas necesarias: {', '.join(detalles_problema['herramientas_necesarias'])}")
else:
    print("No se encontró un problema que coincida con los síntomas dados.")
```

### 🧩 Funcionamiento
1. Cada *frame* describe un tipo de problema y sus características.
2. El sistema compara los síntomas del usuario con los almacenados.
3. Si todos los síntomas coinciden, se devuelve el problema y sus detalles.

### ✅ Ejemplo de salida
```
--- Usando Marcos (Frames) ---

 Problema identificado: cadena_desgastada
   - Es un tipo de: problema_de_transmision
   - La solución es: reemplazar_cadena
   - Herramientas necesarias: cortacadenas, cadena_nueva
```

---

## 🧩 Comparación entre ambos enfoques

| Aspecto | Reglas de Producción | Marcos (Frames) |
|----------|----------------------|-----------------|
| Representación del conocimiento | Basada en reglas condicionales | Basada en estructuras de datos tipo objeto |
| Facilidad de expansión | Media | Alta |
| Legibilidad | Media | Alta |
| Flexibilidad | Alta (motor de inferencia adaptable) | Media (estructura más fija) |
| Uso típico | Sistemas de diagnóstico y decisión | Representación estructurada de objetos o conceptos |

---

## Conclusiones
* Ambos modelos permiten representar conocimiento en un sistema experto, pero con enfoques distintos.
Las Reglas de Producción se enfocan en el razonamiento lógico, permitiendo diagnosticar problemas a partir de síntomas mediante relaciones causa y efecto.
En cambio, los Marcos (Frames) organizan la información de forma estructurada y descriptiva, mostrando los problemas como objetos con sus características y soluciones.
Ambos métodos en conjunto muestran dos formas complementarias de manejar conocimiento: uno deduce, y el otro describe.

**Kevin Ponce de León**  
Estudiante de Ingeniería de Sistemas – UCATEC  
