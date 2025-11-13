# Mapa Mental: Unidad 1 - Contexto de los Sistemas Expertos

Este mapa mental visualiza los conceptos introductorios a la Inteligencia Artificial y los Sistemas Expertos, cubriendo los siguientes puntos clave:

-   **Noción de IA**: Distinción entre IA Débil (estrecha) e IA Fuerte (general).
-   **Comparación**: Diferencias fundamentales entre la computación convencional y los Sistemas Expertos.
-   **Historia**: Hitos en el desarrollo de los Sistemas Expertos, desde sus inicios hasta su renacimiento.
-   **Paradigmas**: Enfoques de la IA que influyeron en los SE, como la IA Simbólica.
-   **Representación del Conocimiento**: Métodos básicos para estructurar la información.
-   **Resolución de Problemas**: Componentes formales para definir y solucionar un problema.

## Código Mermaid

A continuación se presenta el código para generar el diagrama:

```mermaid
mindmap
  root((Unidad 1: Contexto de los SE))
    (Noción de IA)
      ::icon(fa fa-brain)
      (IA Débil/Estrecha)
        - Tarea específica
        - Ej: Siri, Netflix
      (IA Fuerte/General)
        - Nivel humano
        - Teórica
    (Comparación)
      ::icon(fa fa-balance-scale)
      (Computación Convencional)
        - Procesamiento de datos
        - Algoritmos
        - Determinista
      (Sistemas Expertos)
        - Procesamiento de conocimiento
        - Heurísticas
        - Separa conocimiento y lógica
    (Historia de los SE)
      ::icon(fa fa-history)
      (Años 60: Primeros Trabajos)
        - DENDRAL
      (Años 70-80: Era Dorada)
        - MYCIN
        - XCON
      (Años 80-90: Invierno de la IA)
      (Años 90-Hoy: Renacimiento)
    (Paradigmas de IA)
      ::icon(fa fa-lightbulb)
      (IA Simbólica)
        - Manipulación de símbolos y reglas
      (Búsqueda Heurística)
        - "Reglas de dedo"
      (PLN)
        - Interacción con lenguaje humano
    (Representación del Conocimiento)
      ::icon(fa fa-project-diagram)
      (Reglas de Producción IF-THEN)
      (Redes Semánticas)
      (Marcos / Frames)
    (Resolución de Problemas)
      ::icon(fa fa-puzzle-piece)
      - Estado Inicial
      - Operadores / Acciones
      - Test de Meta
      - Costo del Camino