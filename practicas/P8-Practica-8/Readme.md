# Sistema de Agentes Inteligentes para Aspiradora Autónoma

## Descripción General

Este proyecto implementa y compara dos tipos de agentes inteligentes para controlar una aspiradora autónoma en un entorno de dos habitaciones. El sistema demuestra la diferencia fundamental entre agentes reactivos simples y agentes basados en modelos, mostrando cómo la capacidad de mantener un estado interno afecta la eficiencia y inteligencia del comportamiento.

## Arquitectura del Sistema

### Componentes Principales

**1. Entorno de la Aspiradora (entorno_aspiradora.py)**
- Simula un entorno con dos habitaciones (A y B)
- Maneja el estado de limpieza de cada habitación
- Controla la ubicación del agente
- Calcula el rendimiento basado en las acciones
- Proporciona percepciones al agente

**2. Agente Reactivo Simple (agente_reactivo.py)**
- Toma decisiones basadas únicamente en la percepción actual
- No mantiene memoria del estado pasado
- Implementa reglas condicionales simples
- Comportamiento determinista y inmediato

**3. Agente Basado en Modelos (agente_modelos.py)**
- Mantiene un modelo interno del mundo
- Recuerda el estado de ambas habitaciones
- Toma decisiones considerando información no visible
- Planifica acciones basadas en conocimiento acumulado

**4. Sistema Principal (main.py)**
- Coordina las simulaciones de ambos agentes
- Presenta comparativas de rendimiento
- Ejecuta secuencias de prueba automatizadas

## Instalación y Requisitos

### Prerrequisitos
- Python 3.6 o superior
- No se requieren librerías externas

### Estructura de Archivos
```
proyecto_aspiradora/
│
├── entorno_aspiradora.py
├── agente_reactivo.py
├── agente_modelos.py
├── main.py
└── README.md
```

## Ejecución del Sistema

### Ejecución completa
```bash
python main.py
```

### Ejecución individual de componentes
```bash
# Para probar solo el entorno
python -c "from entorno_aspiradora import EntornoAspiradora; print('Entorno funcionando')"

# Para probar solo el agente reactivo
python -c "from agente_reactivo import AgenteReactivoSimple; print('Agente reactivo funcionando')"
```

## Mecánica del Entorno

### Estados del Sistema
- **Habitaciones**: Pueden estar 'Limpia' o 'Sucia'
- **Agente**: Puede estar en 'A' o 'B'
- **Acciones posibles**: 'aspirar', 'ir_a_A', 'ir_a_B', 'no_hacer_nada'

### Sistema de Recompensas
- **+10 puntos**: Por limpiar una habitación sucia
- **-1 punto**: Por moverse entre habitaciones
- **-1 punto**: Por intentar limpiar una habitación ya limpia

## Comportamiento de los Agentes

### Agente Reactivo Simple
```python
# Lógica de decisión
if habitación_actual_sucia → aspirar
else if en_A → ir_a_B
else if en_B → ir_a_A
```

### Agente Basado en Modelos
```python
# Lógica de decisión mejorada
if habitación_actual_sucia → aspirar
else if modelo_indica_A_sucia → ir_a_A
else if modelo_indica_B_sucia → ir_a_B
else if todo_limpio → no_hacer_nada
else → cambiar_de_habitación
```

## Flujo de Ejecución

### Ciclo de Simulación
1. **Inicialización**: Estado aleatorio de habitaciones y posición
2. **Percepción**: Agente recibe (ubicación, estado_actual)
3. **Decisión**: Agente elige acción basada en su tipo
4. **Ejecución**: Entorno aplica la acción y actualiza estado
5. **Evaluación**: Se calcula nuevo rendimiento
6. **Terminación**: Cuando todo está limpio o se alcanza máximo de pasos

### Ejemplo de Ejecución
```
Estado Inicial: {'A': 'Sucia', 'B': 'Limpia'}, Agente en: A
Paso 1: Percepcion ('A', 'Sucia'), Acción=aspirar
Paso 2: Percepcion ('A', 'Limpia'), Acción=ir_a_B
...
Simulación terminada en 3 pasos. Rendimiento final: 8
```

## Casos de Prueba

### Escenario 1: Ambas Habitaciones Sucias
- Agente Reactivo: Cambia constantemente entre habitaciones
- Agente Modelos: Limpia sistemáticamente una tras otra

### Escenario 2: Una Habitación Sucia
- Agente Reactivo: Puede pasar por habitaciones sin limpiar
- Agente Modelos: Dirige eficientemente hacia la habitación sucia

### Escenario 3: Ambas Limpias
- Agente Reactivo: Sigue moviéndose innecesariamente
- Agente Modelos: Se detiene al reconocer todo limpio

## Conclusión

Este proyecto demuestra claramente la evolución en arquitecturas de agentes inteligentes. El agente reactivo simple, aunque funcional, presenta limitaciones significativas debido a su naturaleza miope - solo responde a estímulos inmediatos sin capacidad de planificación o memoria. Su comportamiento, aunque correcto, resulta ineficiente en muchos escenarios.

El agente basado en modelos representa un salto cualitativo en inteligencia artificial. Al mantener un estado interno del mundo, puede tomar decisiones informadas que consideran información no directamente perceptible. Esta capacidad de "recordar" y "inferir" le permite optimizar su comportamiento, evitando acciones redundantes y dirigiendo sus esfuerzos de manera más eficiente.

La diferencia fundamental radica en que el agente reactivo opera en el presente absoluto, mientras que el agente basado en modelos integra pasado, presente y expectativas futuras en su proceso de decisión. Esta capacidad de modelado mental es lo que acerca a estos sistemas a formas más avanzadas de inteligencia, permitiéndoles no solo reaccionar al entorno sino anticiparse y planificar.

La implementación presentada sirve como base fundamental para entender principios clave de la inteligencia artificial: percepción, acción, modelado del estado, y la relación entre complejidad arquitectónica y eficiencia operativa. Estos conceptos son extensibles a sistemas más complejos como robots autónomos, sistemas de recomendación, y agentes de software en entornos dinámicos.