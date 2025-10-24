# Unidad 5 — Ejercicio 1: Agente Reactivo Simple

## Descripción
Este ejercicio introduce el concepto de **agente inteligente**, comenzando con un **agente reactivo**.  
El agente toma decisiones basadas únicamente en su percepción actual, sin considerar el historial de acciones previas.  
El ejemplo más común es el **mundo del aspirador**, donde el agente limpia si detecta suciedad en su ubicación.

---

## Código (copiado del libro)
```python
# Simulación del mundo del aspirador (Agente Reactivo)
import random

# Estado inicial del entorno
ambiente = ["sucio", "limpio"]
posicion = random.choice(["A", "B"])
estado = {"A": random.choice(ambiente), "B": random.choice(ambiente)}

def agente_reactivo(posicion, estado):
    print(f"El agente está en la posición {posicion} y el estado es {estado[posicion]}")
    if estado[posicion] == "sucio":
        print("Acción: limpiar")
        estado[posicion] = "limpio"
    else:
        nueva_posicion = "B" if posicion == "A" else "A"
        print(f"Acción: moverse a {nueva_posicion}")
        posicion = nueva_posicion
    return posicion, estado

# Bucle de simulación
for _ in range(4):
    posicion, estado = agente_reactivo(posicion, estado)
    print("Estado actual:", estado, "\n")
```

# Ejemplo de salida esperada
El agente está en la posición A y el estado es sucio
Acción: limpiar
Estado actual: {'A': 'limpio', 'B': 'sucio'}

El agente está en la posición A y el estado es limpio
Acción: moverse a B
Estado actual: {'A': 'limpio', 'B': 'sucio'}

# Observaciones

- El agente no tiene memoria: actua solo segun el estado actual.

- Representa la forma mas básica de inteligencia reactiva.

- Util para entornos simples y deterministas.

# Conclusión

El agente reactivo demuestra cómo un sistema puede actuar de manera autónoma sin memoria, respondiendo directamente a su entorno, haciendo que el punto de partida para agentes sea más complejo.