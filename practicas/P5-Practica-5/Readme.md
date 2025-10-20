# Sistema Experto para Diagnóstico de Problemas Automotrices

## Descripción General

Este proyecto implementa un sistema experto para diagnosticar problemas comunes en automóviles. El sistema utiliza un motor de inferencia basado en reglas que simula el conocimiento de un mecánico experto, permitiendo diagnosticar fallas a partir de síntomas reportados por el usuario.

## Arquitectura del Sistema

### Componentes Principales

**1. Base de Conocimiento (base_conocimiento.py)**
Contiene el conocimiento experto estructurado en reglas "SI-ENTONCES". Cada regla representa una pieza del conocimiento del mecánico:

- Reglas de diagnóstico primario
- Reglas de confirmación de problemas
- Reglas de diagnóstico específico

**2. Motor de Inferencia (sistema_experto.py)**
Implementa la lógica de razonamiento mediante la clase SistemaExperto:

- Encadenamiento hacia adelante
- Gestión de hechos y conclusiones
- Capacidad explicativa
- Filtrado de diagnósticos

**3. Sistema Principal (main.py)**
Orquesta la ejecución del sistema y maneja la interacción con los casos de uso.

## Base de Conocimiento

El sistema contiene 6 reglas principales que cubren:

1. **Problemas de batería o motor de arranque** - Cuando el coche no gira la llave
2. **Problemas de combustible o encendido** - Cuando el coche gira pero no enciende
3. **Diagnóstico de batería descargada** - Cuando hay problemas de arranque y luces débiles
4. **Diagnóstico de motor de arranque defectuoso** - Cuando hay problemas de arranque pero luces funcionan
5. **Diagnóstico de sistema de combustible** - Cuando hay problemas de encendido y huele a gasolina
6. **Diagnóstico de sistema de encendido** - Cuando hay problemas de encendido y no huele a gasolina

## Flujo de Ejecución

### Proceso de Razonamiento

1. **Entrada de síntomas**: El usuario proporciona los hechos iniciales (síntomas observados)
2. **Aplicación de reglas**: El motor de inferencia aplica las reglas de conocimiento
3. **Encadenamiento hacia adelante**: Deriva nuevos hechos a partir de los existentes
4. **Obtención de diagnósticos**: Filtra las conclusiones finales
5. **Generación de explicaciones**: Muestra el razonamiento seguido

### Ejemplo de Caso de Uso

```python
# Síntomas reportados por el usuario
hechos_usuario = ["coche_no_gira_llave", "luces_debiles_o_muertas"]

# El sistema deduce:
# 1. problema_bateria_o_arranque (Regla 1)
# 2. diagnostico_bateria_descargada (Regla 3)
```

## Características Técnicas

### Motor de Inferencia

- **Algoritmo**: Encadenamiento hacia adelante
- **Estrategia**: Búsqueda exhaustiva hasta saturación
- **Persistencia**: Mantiene historial de inferencias
- **Explicación**: Capacidad de trazar el razonamiento

### Gestión del Conocimiento

- **Separación clara** entre conocimiento y razonamiento
- **Reglas modulares** y fácilmente extensibles
- **Base de conocimiento** independiente del motor

## Conclusión del Sistema

Este sistema experto demuestra la aplicación práctica de la inteligencia artificial simbólica en el dominio automotriz. La implementación logra separar efectivamente el conocimiento específico del dominio (reglas de diagnóstico) de la lógica de razonamiento general (motor de inferencia).
La principal fortaleza del sistema reside en su capacidad explicativa, permitiendo no solo llegar a un diagnóstico sino también mostrar el proceso de razonamiento completo. Esto lo hace valioso tanto para usuarios finales que quieren entender el problema, como para aprendices que desean comprender la lógica de diagnóstico.
