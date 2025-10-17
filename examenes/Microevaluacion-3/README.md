# Microevaluación 3 — Inteligencia Artificial y Sistemas Expertos

---

##  Introducción

Este documento presenta tres **mapas mentales** que resumen las **primeras unidades del módulo “Inteligencia Artificial y Sistemas Expertos”**.  
Cada mapa refleja los conceptos principales, subtemas y relaciones clave entre los componentes de la inteligencia artificial, su representación del conocimiento y los sistemas expertos.  

El propósito es **entender la evolución de la IA** desde su contexto general hasta la construcción de **sistemas expertos capaces de razonar como humanos**.

---

## Mapa 1: Presentación y Contexto de los Sistemas Expertos

**Definición:**  
La Inteligencia Artificial es la rama de la informática que busca desarrollar sistemas capaces de realizar tareas que requieren inteligencia humana, como el razonamiento, la percepción y la toma de decisiones.  
Esta unidad introduce los fundamentos de la IA, sus diferencias con la computación convencional, los paradigmas que la sustentan y su evolución histórica hasta los primeros sistemas expertos.


mindmap
  root((Unidad 1: Presentación y Contexto de los Sistemas Expertos))
    Noción general de la Inteligencia Artificial
      Definición
        Rama de la informática dedicada a crear sistemas que realizan tareas que requieren inteligencia humana
        Ejemplos: aprendizaje, razonamiento, resolución de problemas, percepción, uso del lenguaje
      Tipos de IA
        IA Débil o Estrecha
          Se especializa en una tarea específica (Siri, Alexa, Netflix, Google)
        IA Fuerte o General
          Teórica, capaz de aprender cualquier tarea intelectual humana
      Enfoque del curso
        Se centra en la IA Débil, especialmente los Sistemas Expertos
    Computación Convencional vs Inteligencia Artificial
      Diferencias clave
        Computación convencional
          Procesa datos mediante algoritmos predefinidos
          Secuencia determinista
          Cambiar la lógica requiere reprogramación
          Busca soluciones óptimas
        Inteligencia Artificial
          Procesa conocimiento y símbolos para razonar
          Usa heurísticas para soluciones probables
          Separa conocimiento del motor de inferencia
          Imitación de decisiones humanas bajo incertidumbre
      Ejemplo
        Programa de contabilidad vs Sistema de diagnóstico médico
    Historia de la IA desde los Sistemas Expertos
      Primeros Trabajos (Años 60)
        DENDRAL: identificación de compuestos químicos
      Era Dorada (Años 70-80)
        MYCIN: diagnóstico de infecciones (factor de certeza)
        XCON: configuración de computadoras DEC (éxito comercial)
      Invierno de la IA (Finales 80 - 90)
        Caída del interés por limitaciones tecnológicas
      Renacimiento (Mediados 90 - actualidad)
        Machine Learning, agentes inteligentes, big data
    Paradigmas de IA que influyen en los Sistemas Expertos
      IA Simbólica
        Manipulación de símbolos y reglas
      Búsqueda Heurística
        Uso de reglas empíricas para eficiencia
      Procesamiento del Lenguaje Natural
        Permite interacción en lenguaje humano
    Representación del Conocimiento
      Métodos principales
        Reglas de Producción (IF-THEN)
          Ejemplo: Si paciente tiene tos seca → Probable gripe
        Redes Semánticas
          Nodos y relaciones (canario → ave → alas)
        Marcos (Frames)
          Atributos y valores, similar a objetos
    Resolución de Problemas
      Componentes
        Estado Inicial
        Operadores o Acciones
        Test de Meta
        Costo del Camino
      Objetivo
        Encontrar secuencia que transforme el estado inicial al final mediante búsqueda
---

##  Mapa 2: La Representación del Conocimiento

**Definición breve:**  
Esta unidad se centra en cómo representar formalmente el conocimiento humano para que una computadora pueda procesarlo.  
Se introducen la lógica proposicional y la lógica de predicados como bases formales, junto con la **ingeniería del conocimiento**, disciplina que permite capturar, estructurar y mantener la información proveniente de expertos humanos.

mindmap
  root((Unidad 2: La Representación del Conocimiento))
    Introducción
      Desafío central de la IA: convertir conocimiento humano en formato procesable
      Campo clave: Ingeniería del Conocimiento
    Bases formales de la representación
      Necesidad de estructura formal y lógica
      Lógica Proposicional
        Trabaja con proposiciones verdaderas o falsas
        Usa conectores (Y, O, NO, IMPLICA)
        Limitación: no representa relaciones u objetos individuales
      Lógica de Predicados (Primer Orden)
        Representa objetos, propiedades y relaciones
        Usa cuantificadores ∀ (para todo), ∃ (existe)
        Ejemplo: ∀x (Hombre(x) → Mortal(x))
        Ventaja: mayor expresividad y realismo
    Ingeniería del Conocimiento
      Definición
        Disciplina que construye sistemas basados en conocimiento
        Combina informática, ciencia cognitiva e interacción humana
      Etapas del proceso
        Adquisición del conocimiento
        Representación formal
        Validación de consistencia
        Inferencia lógica
        Mantenimiento y actualización
    Trabajo del Ingeniero del Conocimiento
      Función
        Intermediario entre el experto humano y el sistema
      Responsabilidades
        Selección del problema adecuado
        Interacción con el experto
        Diseño de la base de conocimiento
        Implementación del prototipo
        Refinamiento y validación del sistema
    Estrategias de adquisición del conocimiento
      Entrevistas estructuradas y no estructuradas
      Análisis de casos
      Observación directa del experto
      Prototipado rápido
      Mapas conceptuales
    Cuello de botella en la adquisición del conocimiento
      Dificultades principales
        Conocimiento tácito (intuitivo y no verbalizable)
        Limitaciones o falta de cooperación del experto
        Complejidad y dinamismo del conocimiento
        Barreras de comunicación técnica
      Consecuencia
        Proceso intensivo en tiempo y recursos



---

##  Mapa 3: Los Sistemas Expertos, Definición y Conceptos

**Definición breve:**  
Un **Sistema Experto (SE)** es un programa informático diseñado para emular el razonamiento de un experto humano en un dominio específico.  
Utiliza una base de conocimiento, un motor de inferencia y una interfaz que permite al usuario interactuar con el sistema.  
Esta unidad explica su estructura, los tipos de sistemas expertos y cómo manejan el conocimiento superficial y profundo para tomar decisiones inteligentes.

mindmap
  root((Unidad 3: Los Sistemas Expertos, Definición y Conceptos))
    Concepto de Sistema Experto
      Definición
        Programa que utiliza conocimiento específico y mecanismos de inferencia
        Resuelve problemas a nivel de experto humano
      Arquitectura
        Base de Conocimiento
          Reglas, hechos y heurísticas extraídas de expertos
        Motor de Inferencia
          Aplica reglas lógicas a hechos para deducir conclusiones
        Otros componentes
          Interfaz de usuario
          Módulo de explicación
    Conocimiento superficial y profundo
      Conocimiento superficial
        Basado en experiencia y heurísticas
        Ejemplo: sonido al arrancar → batería descargada
      Conocimiento profundo
        Comprensión de principios causales
        Ejemplo: modelo del circuito eléctrico
      Diferencia clave
        Superficial: rápido, limitado
        Profundo: complejo, flexible y robusto
    Características distintivas de los SE
      Competencia de experto
      Separación del conocimiento y el control
      Manejo de incertidumbre (factores de certeza)
      Capacidad de explicación (justificación de razonamientos)
      Dominio específico
    Tipos o categorías de Sistemas Expertos
      Diagnóstico
        Ejemplo: MYCIN
      Interpretación
        Ejemplo: análisis de datos geológicos
      Predicción
        Ejemplo: mercados financieros
      Diseño y Configuración
        Ejemplo: XCON (DEC)
      Planificación
        Ejemplo: misiones robóticas
      Monitoreo y Control
        Ejemplo: plantas nucleares
      Depuración (debugging)
      Instrucción o tutoría inteligente
    Ejercicio Práctico
      Sistema Experto de Diagnóstico de automóvil
        Paso 1: Definir Base de Conocimiento
          Reglas con síntomas y conclusiones (problemas de batería, combustible, encendido)
        Paso 2: Motor de Inferencia
          Encadenamiento hacia adelante
          Guarda historial de inferencias
        Paso 3: Ejecución y Explicación
          Diagnóstico final: batería descargada
          Capacidad de explicación paso a paso
      Conclusión
        Implementación práctica de la estructura y características de un SE
