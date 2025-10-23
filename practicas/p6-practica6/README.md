Resumen - Unidad 4: Proceso Humano de Resolución de Problemas
🧠 4.1. El Sentido Común
Definición: Conocimiento práctico, implícito y compartido que usamos en la vida cotidiana

Ejemplos: Saber que los objetos caen si se sueltan, que el agua moja, etc.

Desafío en IA: Es extremadamente difícil replicar el sentido común en máquinas

Fragilidad de Sistemas Expertos: Pueden ser expertos en su dominio pero fallan en tareas simples por falta de sentido común

🔄 4.2. Método de Pareamiento (Matching)
Proceso fundamental de los motores de inferencia

Funcionamiento:

Compara hechos conocidos con condiciones de reglas

Si coinciden, activa la regla

Ejecuta la conclusión, añadiendo nuevos hechos

Ciclo: Matching → Activación → Nuevos hechos → Repeat

💭 4.3. Razonamiento
Definición: Proceso cognitivo para pensar lógicamente y formar conclusiones

Función: Manipular conocimiento existente para generar nuevo conocimiento

En IA: Simular este proceso humano en máquinas

🎯 4.4. Inferencia
Relación con razonamiento: La inferencia es un componente específico del razonamiento

Definición: Proceso paso a paso para derivar conclusiones lógicas

En Sistemas Expertos: El motor de inferencia ejecuta estos pasos

Analogía: Razonamiento = viaje completo, Inferencia = cada paso del viaje

📉 4.5. Razonamiento Deductivo
Dirección: De lo general a lo específico

Característica: Conclusiones garantizadas si las premisas son verdaderas

Formato (Modus Ponens):

Premisa 1: Si P, entonces Q

Premisa 2: P es verdadero

Conclusión: Q es verdadero

Ejemplo:

Si llueve, la calle se moja

Está lloviendo

∴ La calle está mojada

Aplicación: Base de los Sistemas Expertos clásicos

📈 4.6. Razonamiento Inductivo
Dirección: De lo específico a lo general

Característica: Conclusiones probables, no garantizadas

Formato (Generalización):

Observación 1: Caso A tiene propiedad X

Observación 2: Caso B tiene propiedad X

Observación N: Caso N tiene propiedad X

Conclusión: Todos los casos tienen propiedad X

Ejemplo:

Cuervo 1 es negro

Cuervo 2 es negro

Cuervo N es negro

∴ Todos los cuervos son negros

Aplicación: Base del Machine Learning y Aprendizaje Automático

💻 Implementación en Código
🔍 Parte Deductiva (Sistema Experto)
python
class SistemaExpertoDeductivo:
    def razonar(self, hechos):
        # Aplica encadenamiento hacia adelante
        # Matching: condiciones.issubset(hechos_deducidos)
        # Conclusión garantizada si reglas son correctas
🤖 Parte Inductiva (Machine Learning)
python
from sklearn.tree import DecisionTreeClassifier
modelo_inductivo = DecisionTreeClassifier()
modelo_inductivo.fit(X, y)  # Aprende de ejemplos
# Conclusiones probables, no garantizadas
📦 Librerías Utilizadas
Para la Parte Deductiva:
Python estándar: No requiere instalaciones adicionales

Conceptos: Sets, condicionales, loops

Para la Parte Inductiva:
bash
pip install scikit-learn pandas
scikit-learn: Librería principal de Machine Learning

DecisionTreeClassifier: Algoritmo que aprende reglas de datos

export_text: Visualiza reglas aprendidas

pandas: Manipulación y análisis de datos

DataFrame: Estructura tabular para los datos de entrenamiento

🎯 Diferencias Prácticas
Aspecto	Deductivo	Inductivo
Base	Reglas expertas	Datos/ejemplos
Conclusión	Garantizada	Probable
Instalación	Python puro	scikit-learn + pandas
Aplicación	Sistemas Expertos	Machine Learning
🎓 Conclusión Clave
Sistemas Expertos: Principalmente deductivos (aplican reglas predefinidas)

Machine Learning: Principalmente inductivo (aprende reglas de datos)

Complementariedad: Ambos enfoques son necesarios para IA robusta

Desafío permanente: Replicar el sentido común humano sigue siendo el "santo grial" de la IA

Herramientas: Python + scikit-learn permiten implementar ambos enfoques

