# Unidad 5 — Ejercicio 2: Agente Basado en Modelo

## Descripción
A diferencia del agente reactivo, este agente mantiene un **modelo interno del entorno**.  
Utiliza la información percibida y su conocimiento previo para decidir acciones más efectivas.  
Este enfoque mejora el rendimiento en entornos donde el estado no siempre es visible completamente.

---

## Código (copiado del libro)
```python
# Agente basado en modelo (Mundo del aspirador)
import random

class AgenteModelo:
    def __init__(self):
        self.modelo = {"A": None, "B": None}

    def percibir_y_actuar(self, posicion, estado):
        print(f"El agente está en {posicion}, el entorno es {estado[posicion]}")
        self.modelo[posicion] = estado[posicion]

        if estado[posicion] == "sucio":
            print("Acción: limpiar")
            estado[posicion] = "limpio"
        elif self.modelo["A"] == "limpio" and self.modelo["B"] == "limpio":
            print("Acción: detener (ambiente limpio)")
            return None, estado
        else:
            nueva_posicion = "B" if posicion == "A" else "A"
            print(f"Acción: moverse a {nueva_posicion}")
            posicion = nueva_posicion
        return posicion, estado

# Simulación
estado = {"A": random.choice(["sucio", "limpio"]), "B": random.choice(["sucio", "limpio"])}
agente = AgenteModelo()
posicion = random.choice(["A", "B"])

for _ in range(5):
    if posicion is None:
        break
    posicion, estado = agente.percibir_y_actuar(posicion, estado)
    print("Modelo interno:", agente.modelo)
    print("Estado actual:", estado, "\n")
```
# Ejemplo de salida esperada

El agente está en la posición A y el estado es sucio
Acción: limpiar
Estado actual: {'A': 'limpio', 'B': 'sucio'}

El agente está en la posición A y el estado es limpio
Acción: moverse a B
Estado actual: {'A': 'limpio', 'B': 'sucio'}

## Observaciones

El agente no tiene memoria: 
- Actua solo segun el estado actual, representando la forma mas basica de inteligencia reactiva.

- Util para entornos simples y deterministas.

## Conclusión

El agente reactivo demuestra cómo un sistema puede actuar de manera autónoma sin memoria, respondiendo directamente a su entorno, siendo el punto de partida para agentes más complejos.