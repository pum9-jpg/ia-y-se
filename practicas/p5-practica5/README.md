README - Sistema Experto para Diagnóstico de Automóviles
📋 Descripción
Sistema experto que diagnostica problemas comunes en automóviles cuando no encienden. Utiliza reglas de conocimiento de expertos mecánicos y puede explicar cómo llegó a cada diagnóstico.

🚀 Características Principales
Diagnóstico automático de problemas de automóviles

Base de conocimiento con reglas de expertos mecánicos

Motor de inferencia con encadenamiento hacia adelante

Sistema explicativo que muestra el proceso de razonamiento

Arquitectura modular y fácil de extender

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.x

Enfoque: Sistemas Expertos con Reglas de Producción

Algoritmo: Encadenamiento hacia adelante (Forward Chaining)

📁 Estructura del Proyecto
text
sistema-experto-autos/
│
├── sistema_experto_auto.py    # Código principal
└── README.md                  # Este archivo
🔧 Instalación y Ejecución
Prerrequisitos
Python 3.6 o superior

Ejecución
bash
python sistema_experto_auto.py
🎯 Cómo Funciona el Sistema
1. Base de Conocimiento
Contiene 6 reglas de diagnóstico basadas en experiencia mecánica:

python
base_de_conocimiento_coche = [
    {
        "nombre": "Regla 1: Problema de batería o motor de arranque",
        "si": ["coche_no_gira_llave"],
        "entonces": "problema_bateria_o_arranque"
    },
    # ... más reglas
]
2. Motor de Inferencia
Encadenamiento hacia adelante: Parte de síntomas conocidos

Aplica reglas cuando se cumplen todas las condiciones

Deduce nuevos hechos hasta agotar todas las posibilidades

3. Sistema Explicativo
Explica el razonamiento paso a paso

Muestra qué reglas se aplicaron

Reconstruye la cadena lógica del diagnóstico

📊 Reglas de Diagnóstico Implementadas
Regla	Condiciones	Diagnóstico
1	Coche no gira llave	Problema batería/arranque
2	Coche gira pero no enciende	Problema combustible/encendido
3	Problema batería + luces débiles	Batería descargada
4	Problema batería + luces OK	Motor arranque defectuoso
5	Problema combustible + huele gasolina	Sistema combustible
6	Problema combustible + no huele gasolina	Sistema encendido
💡 Ejemplos de Uso
Caso 1: Batería Descargada
Síntomas ingresados:

python
["coche_no_gira_llave", "luces_debiles_o_muertas"]
Diagnóstico obtenido:

text
diagnostico_bateria_descargada
Proceso:

Regla 1: coche_no_gira_llave → problema_bateria_o_arranque

Regla 3: problema_bateria_o_arranque + luces_debiles_o_muertas → diagnostico_bateria_descargada

Caso 2: Problema de Encendido
Síntomas ingresados:

python
["coche_gira_pero_no_enciende", "no_huele_a_gasolina"]
Diagnóstico obtenido:

text
diagnostico_sistema_encendido
🎓 Conceptos de Sistemas Expertos Aplicados
✅ Separación de Componentes
Base de Conocimiento: Reglas del experto (mecánico)

Motor de Inferencia: Lógica de razonamiento

Hechos: Síntomas proporcionados

✅ Características Implementadas
Conocimiento Superficial: Reglas basadas en experiencia

Encadenamiento hacia adelante: De síntomas a diagnóstico

Capacidad explicativa: Trazabilidad del razonamiento

Modularidad: Fácil agregar nuevas reglas

📈 Salida del Sistema
Ejemplo de Salida Completa
text
- INICIANDO DIAGNÓSTICO CASO 1 -
- Proceso de Razonamiento -
Hecho añadido: 'problema_bateria_o_arranque' (Gracias a la regla: 'Regla 1: Problema de batería o motor de arranque')
Hecho añadido: 'diagnostico_bateria_descargada' (Gracias a la regla: 'Regla 3: Batería descargada confirmada')
- Fin del Proceso de Razonamiento -

Hechos Finales Deducidos: {'luces_debiles_o_muertas', 'coche_no_gira_llave', 'problema_bateria_o_arranque', 'diagnostico_bateria_descargada'}

Diagnóstico(s) Final(es): ['diagnostico_bateria_descargada']

- EXPLICACIÓN DEL DIAGNÓSTICO -
Se llegó a la conclusión 'diagnostico_bateria_descargada' por la 'Regla 3: Batería descargada confirmada'...
🔮 Extensiones Posibles
Ampliar Base de Conocimiento

Agregar más reglas para otros problemas

Incluir reglas para diferentes marcas de autos

Mejorar Interfaz

Interfaz gráfica de usuario

Aplicación web o móvil

Características Avanzadas

Base de datos de soluciones

Sistema de recomendación de repuestos

Integración con manuales de reparación

👨‍💻 Uso Educativo
Este proyecto es ideal para aprender sobre:

Sistemas Expertos e Inteligencia Artificial

Representación del Conocimiento

Motores de Inferencia

Ingeniería del Conocimiento

📝 Licencia
Proyecto educativo para fines de aprendizaje en sistemas expertos.