# Unidad 5: Agentes Inteligentes

Esta unidad introduce el concepto de **agentes inteligentes**, una pieza clave en la Inteligencia Artificial moderna. Un agente es cualquier entidad capaz de **percibir su entorno** mediante sensores y **actuar sobre él** con actuadores.

## 1. ¿Qué es la Inteligencia Artificial?
La IA se entiende como el **estudio y diseño de agentes racionales**, aquellos que eligen acciones óptimas para maximizar su rendimiento con base en sus percepciones y conocimiento previo.

## 2. Fundamentos de la Inteligencia Artificial
La IA se apoya en múltiples disciplinas: filosofía, matemáticas, economía, neurociencia, psicología, ingeniería computacional y lingüística.

## 3. Agentes y su entorno
El ciclo percepción-acción define su funcionamiento. Se usa el modelo **PEAS**:
- **Performance:** Criterio de éxito del agente.
- **Environment:** Contexto donde actúa.
- **Actuators:** Dispositivos que ejecutan acciones.
- **Sensors:** Dispositivos que perciben el entorno.

## 4. Tipos de Entornos
Los entornos pueden ser:
- Observables o Parcialmente observables.
- Deterministas o Estocásticos.
- Episódicos o Secuenciales.
- Estáticos o Dinámicos.
- Discretos o Continuos.
- De un solo agente o Multiagente.

## 5. Estructura de los Agentes
Existen diferentes estructuras:
1. **Agente Reactivo Simple:** Actúa por reglas directas.
2. **Agente Basado en Modelos:** Usa memoria interna.
3. **Agente Basado en Objetivos:** Persigue metas definidas.
4. **Agente Basado en Utilidad:** Evalúa la satisfacción de sus acciones.
5. **Agente que Aprende:** Mejora con la experiencia.

## 6. Ejercicio Práctico: Mundo de la Aspiradora
Se implementaron dos agentes con diferente estructura:

### 🧹 Agente Reactivo Simple
Decide solo con base en la percepción actual (no tiene memoria).  
Archivo: `agente_reactivo_simple.py`

### 🤖 Agente Basado en Modelos
Mantiene un modelo interno del mundo para evitar acciones redundantes.  
Archivo: `agente_basado_en_modelos.py`

## 7. Conclusiones
| Tipo de Agente | Características | Eficiencia |
|----------------|-----------------|-------------|
| Reactivo Simple | Rápido pero sin memoria; puede repetir acciones. | Baja |
| Basado en Modelos | Usa memoria y evita repeticiones. | Alta |

Los agentes basados en modelos demuestran mayor racionalidad y eficiencia, representando un paso hacia sistemas inteligentes más avanzados.
