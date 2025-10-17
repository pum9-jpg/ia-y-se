UNIDAD 1 — Presentación y Contexto de los Sistemas Expertos
├── 1.1 Noción general de la Inteligencia Artificial
│ ├── IA Débil (Estrecha)
│ │ ├── Ejecuta tareas específicas con alto rendimiento
│ │ ├── Ejemplos:
│ │ │ ├── Asistentes de voz (Siri, Alexa)
│ │ │ ├── Motores de búsqueda (Google)
│ │ │ └── Sistemas de recomendación (Netflix)
│ └── IA Fuerte (General)
│ ├── Capaz de aprender y razonar como un humano
│ └── Actualmente teórica
│
├── 1.2 IA vs Computación Convencional
│ ├── Computación convencional
│ │ ├── Algoritmos deterministas
│ │ └── Modificación requiere reprogramar código
│ └── Inteligencia Artificial
│ ├── Razonamiento con conocimiento
│ ├── Uso de heurísticas (no siempre soluciones óptimas)
│ └── Separación entre conocimiento y motor de inferencia
│
├── 1.3 Historia de la IA
│ ├── 1956 — Conferencia de Dartmouth (nacimiento formal de la IA)
│ ├── Años 60 — Primeros SE: DENDRAL
│ ├── Años 70–80 — Era Dorada
│ │ ├── Sistemas MYCIN y XCON
│ │ └── Primeros éxitos comerciales
│ ├── Finales 80–90 — Invierno de la IA
│ └── Mediados 90–Presente — Renacimiento
│ ├── Aumento de datos y potencia
│ └── Integración con Machine Learning y agentes inteligentes
│
├── 1.4 Paradigmas de IA que influyen en los SE
│ ├── IA Simbólica (manipulación de símbolos y reglas)
│ ├── Búsqueda heurística (atajos para encontrar soluciones)
│ └── Procesamiento de Lenguaje Natural (PLN)
│
├── 1.5 Representación del Conocimiento
│ ├── Reglas de Producción (IF - THEN)
│ ├── Redes Semánticas (nodos + relaciones)
│ └── Marcos (frames — atributos y valores)
│
└── 1.6 Resolución de Problemas
├── Estado inicial
├── Operadores (acciones disponibles)
├── Test de meta (objetivo)
└── Costo del camino



UNIDAD 2 — Representación del Conocimiento
├── 2.1 Bases formales
│ ├── Lógica Proposicional
│ │ ├── Proposiciones → Verdadero o falso
│ │ └── Conectores lógicos: Y, O, NO, implica
│ └── Lógica de Predicados
│ ├── Más expresiva
│ ├── Usa cuantificadores (∀, ∃)
│ └── Representa objetos, propiedades y relaciones
│
├── 2.2 Ingeniería del Conocimiento
│ ├── Objetivo: extraer conocimiento humano y formalizarlo
│ ├── Proceso:
│ │ 1. Adquisición
│ │ 2. Representación
│ │ 3. Validación
│ │ 4. Inferencia
│ │ 5. Mantenimiento
│
├── 2.3 Rol del Ingeniero del Conocimiento
│ ├── Intermediario entre experto y sistema
│ ├── Selecciona dominios adecuados
│ ├── Extrae conocimiento tácito y explícito
│ ├── Diseña base de conocimiento
│ └── Refinamiento iterativo con retroalimentación
│
├── 2.4 Estrategias útiles
│ ├── Entrevistas estructuradas / no estructuradas
│ ├── Análisis de casos
│ ├── Observación directa
│ ├── Prototipado rápido
│ └── Mapas conceptuales
│
└── 2.5 Cuello de Botella en la Adquisición de Conocimiento
├── Conocimiento tácito (difícil de verbalizar)
├── Complejidad y cambios constantes
├── Barreras de comunicación
├── Falta de tiempo del experto
└── Limitaciones humanas


UNIDAD 3 — Sistemas Expertos
├── 3.1 Definición
│ ├── Programa basado en conocimiento y razonamiento
│ ├── Componentes:
│ │ ├── Base de conocimiento
│ │ ├── Motor de inferencia
│ │ ├── Interfaz de usuario
│ │ └── Módulo de explicación
│
├── 3.2 Tipos de conocimiento
│ ├── Superficial (empírico)
│ │ ├── Reglas de dedo (atajos)
│ │ └── Ejemplo: “Si suena clic al encender → batería muerta”
│ └── Profundo (modelos causales)
│ ├── Basado en principios físicos o lógicos
│ └── Permite razonar ante casos nuevos
│
├── 3.3 Características de los Sistemas Expertos
│ ├── Nivel experto en un dominio
│ ├── Separación conocimiento/control
│ ├── Manejo de incertidumbre (factores de certeza)
│ ├── Capacidad de explicación (razonamiento trazable)
│ └── Enfocado en dominios específicos
│
└── 3.4 Tipos de Sistemas Expertos
├── Diagnóstico → Identificar causas (ej. MYCIN)
├── Interpretación → Análisis de datos
├── Predicción → Pronósticos de eventos futuros
├── Diseño y configuración → Sistemas complejos
├── Planificación → Secuencias de acciones
├── Monitoreo y control → Supervisión de sistemas críticos
├── Depuración → Identificación de fallos
└── Instrucción → Tutoría inteligente
