# Unidad 4: El Proceso Humano de Resolución de Problemas y el Proceso del Razonamiento

Esta unidad explica cómo los humanos razonan y cómo la Inteligencia Artificial intenta replicar este proceso. Los temas centrales son:

## 1. El sentido común
El sentido común es el conocimiento práctico que las personas usamos para interpretar el mundo. Replicarlo en las máquinas es un desafío complejo, ya que los sistemas expertos solo operan con conocimiento explícito.

## 2. Método de Pareamiento (Matching)
Es el proceso en el que el motor de inferencia compara hechos conocidos con las condiciones de las reglas en la base de conocimiento. Si se cumple una regla, se activa y genera nuevos hechos.

## 3. Razonamiento e Inferencia
El razonamiento es el proceso global de pensar y llegar a conclusiones; la inferencia es el mecanismo paso a paso que realiza esas deducciones. En IA, el motor de inferencia ejecuta esas operaciones.

## 4. Deducción e Inducción
- **Razonamiento Deductivo:** Parte de reglas generales y llega a conclusiones específicas (garantizadas).
- **Razonamiento Inductivo:** Parte de ejemplos específicos para formular reglas generales (probables).

## 5. Aplicación Práctica en Python
Se presentan dos enfoques implementados:

### Sistema Deductivo
Usa reglas predefinidas para deducir conclusiones a partir de hechos (como en un Sistema Experto).  
Archivo: `sistema_deductivo.py`

### Sistema Inductivo
Aprende a partir de ejemplos utilizando un modelo de Machine Learning (Árbol de Decisión).  
Archivo: `sistema_inductivo.py`

## Conclusión
| Característica | Razonamiento Deductivo | Razonamiento Inductivo |
|----------------|------------------------|------------------------|
| Punto de partida | Reglas generales | Ejemplos y datos |
| Proceso | Aplicación de reglas | Generalización de patrones |
| Resultado | Conclusión cierta | Modelo predictivo |
| Uso principal | Sistemas Expertos | Machine Learning |

La unidad muestra cómo la IA combina ambos tipos de razonamiento para emular el pensamiento humano en la resolución de problemas.
