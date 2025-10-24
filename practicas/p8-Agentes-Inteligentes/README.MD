# Agentes Inteligentes

## 1. Introducción

Esta documentación explica el funcionamiento de dos tipos de agentes inteligentes implementados en Python dentro del entorno de una aspiradora:  
* **Agente Reactivo Simple:** actúa directamente en función de sus percepciones actuales sin recordar estados anteriores.  
* **Agente Basado en Modelos:** utiliza un modelo interno del entorno para tomar decisiones más racionales y eficientes.  

El propósito de este proyecto es mostrar cómo un agente puede percibir, decidir y actuar de forma autónoma para mantener su entorno limpio.

---

## 2. Requisitos para ejecutar

* **Python**
* No se requieren librerías externas (todo está implementado con código nativo de Python).

Para ejecutar el código, basta con guardarlo en un archivo `agentes_inteligentes.py` y ejecutarlo con:

```bash
python agentes_inteligentes.py
```

---

## 3. Código de los Agentes Inteligentes

### Entorno de la Aspiradora

Este entorno simula dos habitaciones (A y B), que pueden estar limpias o sucias. El agente se mueve entre ellas y aspira la suciedad según sus percepciones.

```python
class EntornoAspiradora:
    def __init__(self):
        self.estado = {'A': 'Sucia', 'B': 'Sucia'}
        self.ubicacion_agente = 'A'
        self.rendimiento = 0

    def percibir(self):
        return (self.ubicacion_agente, self.estado[self.ubicacion_agente])

    def ejecutar_accion(self, accion):
        if accion == 'aspirar':
            if self.estado[self.ubicacion_agente] == 'Sucia':
                self.estado[self.ubicacion_agente] = 'Limpia'
                self.rendimiento += 10
        elif accion == 'ir_a_A':
            self.ubicacion_agente = 'A'
            self.rendimiento -= 1
        elif accion == 'ir_a_B':
            self.ubicacion_agente = 'B'
            self.rendimiento -= 1

    def simular(self, agente):
        pasos = 0
        print(f"Estado Inicial: {self.estado}, Agente en: {self.ubicacion_agente}\n")
        while 'Sucia' in self.estado.values():
            percepcion = self.percibir()
            accion = agente.programa(percepcion)
            print(f"Paso {pasos+1}: Percepción: {percepcion}, Acción: {accion}\n")
            self.ejecutar_accion(accion)
            pasos += 1
        print(f"Simulación terminada en {pasos} pasos.")
        print(f"Rendimiento Final: {self.rendimiento}")
        print(f"Estado Final: {self.estado}\n")
```

---

### Agente Reactivo Simple

Este agente toma decisiones **solo basadas en la percepción actual**. Si el lugar donde está está sucio, aspira; si no, se mueve al otro lado.

```python
class AgenteReactivoSimple:
    def programa(self, percepcion):
        ubicacion, situacion = percepcion
        if situacion == 'Sucia':
            return 'aspirar'
        elif ubicacion == 'A':
            return 'ir_a_B'
        else:
            return 'ir_a_A'
```

---

### Agente Basado en Modelos

Este agente **mantiene un modelo interno** del entorno (un registro de qué habitaciones están limpias o sucias). Esto le permite tomar decisiones más racionales y completas.

```python
class AgenteBasadoEnModelos:
    def __init__(self):
        self.modelo = {'A': None, 'B': None}

    def programa(self, percepcion):
        ubicacion, situacion = percepcion
        self.modelo[ubicacion] = situacion

        if self.modelo[ubicacion] == 'Sucia':
            return 'aspirar'
        elif ubicacion == 'A':
            return 'ir_a_B'
        elif ubicacion == 'B':
            return 'ir_a_A'
```

---

## 4. Ejecución de la Simulación

Ambos agentes se prueban en el entorno de la aspiradora con diferentes configuraciones iniciales.

```python
# - Simulación 1: Agente Reactivo Simple -
print("\n--- Probando Agente Reactivo Simple ---")
entorno1 = EntornoAspiradora()
entorno1.estado = {'A': 'Sucia', 'B': 'Limpia'}
entorno1.ubicacion_agente = 'A'
agente1 = AgenteReactivoSimple()
entorno1.simular(agente1)

# - Simulación 2: Agente Basado en Modelos -
print("\n--- Probando Agente Basado en Modelos ---")
entorno2 = EntornoAspiradora()
entorno2.estado = {'A': 'Sucia', 'B': 'Sucia'}
entorno2.ubicacion_agente = 'A'
agente2 = AgenteBasadoEnModelos()
entorno2.simular(agente2)
```

---

## 5. Resultados Esperados

### Ejemplo de salida

```
--- Probando Agente Reactivo Simple ---
Estado Inicial: {'A': 'Sucia', 'B': 'Limpia'}, Agente en: A
Paso 1: Percepción: ('A', 'Sucia'), Acción: aspirar
Simulación terminada en 1 pasos.
Rendimiento Final: 10
Estado Final: {'A': 'Limpia', 'B': 'Limpia'}

--- Probando Agente Basado en Modelos ---
Estado Inicial: {'A': 'Sucia', 'B': 'Sucia'}, Agente en: A
Paso 1: Percepción: ('A', 'Sucia'), Acción: aspirar
Paso 2: Percepción: ('A', 'Limpia'), Acción: ir_a_B
Paso 3: Percepción: ('B', 'Sucia'), Acción: aspirar
Simulación terminada en 3 pasos.
Rendimiento Final: 19
Estado Final: {'A': 'Limpia', 'B': 'Limpia'}
```

---

## 6. Explicación del Funcionamiento

1. El **entorno** define el estado inicial de las habitaciones y las posibles acciones.  
2. El **agente** percibe el entorno (ubicación y estado del lugar actual).  
3. Según el tipo de agente:
   * El **Reactivo Simple** actúa solo con la percepción inmediata.
   * El **Basado en Modelos** actualiza un registro interno y actúa en función de su conocimiento previo.  
4. La simulación continúa hasta que todas las habitaciones estén limpias.  
5. Se calcula el **rendimiento**, premiando la limpieza y penalizando los movimientos.

---

## 7. Conclusión

Los resultados llegan a demuestrar que el Agente Reactivo Simple es rápido y eficaz en entornos pequeños, pero se limita por su falta de memoria.  
En cambio, el Agente Basado en Modelos llega a mostrar un comportamiento más racional y adaptativo, ya que usa conocimiento interno para planificar mejor sus acciones.  
Este experimento llega  a evidenciar cómo la incorporación de memoria y razonamiento mejora la inteligencia de los agentes.