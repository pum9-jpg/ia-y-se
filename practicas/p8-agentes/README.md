# Simulación de un Agente Aspiradora

Este proyecto simula un entorno simple de dos habitaciones (A y B) en el que un agente aspiradora realiza tareas de limpieza. El entorno y los agentes interactúan mediante percepciones y acciones, siguiendo diferentes estrategias de decisión.

---

## ¿Cómo funciona?

- **Entorno (`EntornoAspiradora`)**:
  - Tiene dos habitaciones, cada una puede estar limpia o sucia.
  - El agente comienza en una habitación al azar.
  - Permite percepciones (ubicación y estado de la habitación actual).
  - Permite ejecutar acciones como aspirar, moverse entre habitaciones.
  - Lleva registro del número de pasos y el rendimiento total.

- **Agentes**:
  - **Agente Reactivo Simple**:
    - Decide actuar solo en base a la percepción actual.
    - Si la habitación está sucia, la aspira.
    - Si está limpia, se mueve a la otra habitación.
  
  - **Agente Basado en Modelos**:
    - Mantiene un modelo interno del estado de las habitaciones.
    - Toma decisiones considerando el historial del entorno.
    - Aspira si la habitación está sucia; si no, se mueve a la otra habitación hasta que ambas estén limpias.

- **Simulación (`simular`)**:
  - Ejecuta el ciclo de percepción y decisión.
  - Detiene la simulación cuando todas las habitaciones están limpias o después de 10 pasos.
  - Muestra en consola los estados, percepciones, acciones y rendimiento final.

---

## ¿Cómo ejecutarlo?

1. Asegúrate de tener Python instalado en tu sistema.
2. Copia todo el código en un archivo llamado, por ejemplo, `aspiradora.py`.
3. Corre el script desde la terminal o consola:

```bash
python aspiradora.py
```

4. Verás en la consola las simulaciones con ambos tipos de agentes y sus resultados.

---

## Conclusión

Este código muestra cómo diferentes estrategias de agentes pueden influir en la eficiencia en tareas simples de limpieza. El agente reactivo es más básico y reacciona solo a la situación actual, mientras que el agente basado en modelos intenta recordar y planear mejor, logrando potencialmente un rendimiento mejor en entornos más complejos.
