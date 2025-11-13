---
### **README for Unit 3**

```markdown
# Mapa Mental: Unidad 3 - Los Sistemas Expertos, Definición y Conceptos

Este mapa mental define formalmente qué es un Sistema Experto, detallando su arquitectura, características y aplicaciones. Los puntos clave incluyen:

-   **Concepto**: Un sistema que emula la capacidad de decisión de un experto humano.
-   **Arquitectura Fundamental**: La separación clave entre la **Base de Conocimiento** y el **Motor de Inferencia**.
-   **Tipos de Conocimiento**: La diferencia entre conocimiento **Superficial** (basado en experiencia) y **Profundo** (basado en principios).
-   **Características**: Cualidades distintivas como la capacidad de explicación, el manejo de incertidumbre y la especialización en un dominio.
-   **Categorías**: Las diferentes aplicaciones de los SE, como diagnóstico, planificación, diseño, etc.

## Código Mermaid

A continuación se presenta el código para generar el diagrama:

```mermaid
mindmap
  root((Unidad 3: Sistemas Expertos))
    (Concepto)
      - Emula a un experto humano
    (Arquitectura Fundamental)
      ::icon(fa fa-building)
      (Base de Conocimiento)
        - Repositorio de reglas y hechos
      (Motor de Inferencia)
        - "Cerebro" que razona
    (Tipos de Conocimiento)
      ::icon(fa fa-layer-group)
      (Superficial)
        - Basado en experiencia y heurísticas
      (Profundo)
        - Basado en principios fundamentales
    (Características)
      ::icon(fa fa-star)
      - Competencia de experto
      - Separación de conocimiento y control
      - Manejo de incertidumbre
      - Capacidad de explicación
    (Categorías)
      ::icon(fa fa-tags)
      - Diagnóstico
      - Interpretación
      - Predicción
      - Diseño
      - Planificación