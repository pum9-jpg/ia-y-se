# 🧹 Simulador de Agentes de Aspiradora
Este proyecto implementa la simulación del Mundo de la Aspiradora (Vacuum World), un entorno clásico en la Inteligencia Artificial para probar el desempeño de diferentes tipos de agentes.

## 🎯 Objetivo
El objetivo principal es comparar el rendimiento y el comportamiento de dos arquitecturas de agentes distintas dentro de un entorno simple:
- Agente Reactivo Simple
- Agente Basado en Modelo
El entorno consta de dos habitaciones (A y B), cada una puede estar Limpia o Sucia

## ⚙️ Estructura del Código
El código está organizado en tres clases principales:
1. Entorno Aspirador

    Esta clase define el mundo en el que opera el agente.
- Estado Inicial: Se inicializan aleatoriamente los estados de las habitaciones ('Limpia' o 'Sucia') y la ubicación del agente ('A' o 'B').
- Percepción: El método obntener_percepcion devuelve la ubicación actual del agente y el estado de esa habitación (e.g., ('A', 'Sucia')).
- Acciones: El método ejecutar_accion procesa las acciones del agente ('aspirar', 'ir_a_A', 'ir_a_B') actualizando el estado del entorno y el rendimiento.
- Métrica de Rendimiento:

    - +10 por aspirar una habitación sucia.

    - -1 por mover el agente.

    - -1 por aspirar una habitación limpia.

- Simulación (simular): Ejecuta el ciclo de percepción-acción del agente hasta que ambas habitaciones estén limpias o se alcance el límite de pasos (max_pasos).
2. AgenteReactivoSimple

    Este agente toma decisiones basándose únicamente en su percepción actual (la ubicación y el estado de la habitación actual). No tiene memoria del estado pasado ni conocimiento del estado de la otra habitación.

    ```bash
    Percepción,                             Decisión
    Estado es 'Sucia'                       'aspirar'
    Estado es 'Limpia' y Ubicación es 'A'   'ir_a_B'
    Estado es 'Limpia' y Ubicación es 'B'   'ir_a_A'
    ```

3. AgenteBasadaEnModelo

    Este agente mantiene un modelo interno del mundo (self.modelo), que rastrea el estado conocido de ambas habitaciones (A y B). Esto le permite tomar decisiones más informadas para maximizar el rendimiento.

    ```bash
    Modelo / Percepción                         Decisión
    Estado actual es 'Sucia'                    'aspirar'
    Habitación 'A' es 'Sucia' (en el modelo)    'ir_a_A'
    Habitación 'B' es 'Sucia' (en el modelo)    'ir_a_B'
    Ambas son 'Limpia' (en el modelo)           'no_hacer_nada'
    Default (Exploración)                       Cambiar de habitación
    ```

## 🚀 Cómo Ejecutar
Simplemente guarda el código completo en un archivo (aspiradora.py por ejemplo) y ejecútalo. El script automáticamente:

1. Crea un entorno aleatorio para el Agente Reactivo Simple.

2. Simula su comportamiento.

3. Crea un nuevo entorno aleatorio para el Agente Basado en Modelo.

4. Simula su comportamiento.

```bash
python main.py
```