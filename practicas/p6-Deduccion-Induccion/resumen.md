# 📚 Unidad 4: El Proceso Humano de Resolución de Problemas y el Proceso del Razonamiento
### Esta unidad explora los fundamentos del razonamiento humano para inspirar directamente el diseño de los motores de inferencia en los Sistemas Expertos. La meta es entender cómo piensan los humanos para poder construir máquinas que "piensen" 

## 🌍 El Sentido Común
### - Es el vasto cuerpo de conocimiento informal, implícito e inconsciente que los humanos utilizan constantemente.
### - Incluye verdades triviales 
### - Es extremadamente difícil de formalizar y representa uno de los mayores desafíos para la Inteligencia Artificial.

## ⬇️ Razonamiento Deductivo
### - Es el razonamiento que va de lo general a lo particular.
### - Se parte de reglas o principios generales (premisas) que se aplican a hechos específicos.
### - La conclusión es lógicamente cierta si las premisas son verdaderas.
``` bash
Ejemplo: Si todos los hombres son mortales, y Sócrates es hombre, entonces Sócrates es mortal.
```
### - Es la base de la mayoría de los Sistemas Expertos basados en reglas.

## ⬆️ Razonamiento Inductivo
### - Es el razonamiento que va de lo particular a lo general.
### - Se parte de ejemplos y observaciones específicas para generalizar un patrón o hipótesis.
### - La conclusión es probable, pero no garantizada.
### - Es el pilar fundamental del Aprendizaje Automático (Machine Learning) y la Ciencia de Datos.
``` bash
Ejemplo: He observado 100 cisnes y todos son blancos, por lo tanto, todos los cisnes son blancos.
```

## ❓ Razonamiento Abductivo
### - Es el razonamiento que busca la mejor explicación o causa para un efecto observado.
### - El proceso va de la conclusión (efecto) a la premisa (causa más probable).
### - La conclusión es una hipótesis.
### - Se utiliza comúnmente en sistemas de diagnóstico.
``` bash
Ejemplo: El césped está mojado (Efecto), la causa más probable es que llovió (Hipótesis).
```

## ✅ Razonamiento por Defecto
### - Permite llegar a conclusiones basadas en lo que se espera que sea verdad en ausencia de evidencia que pruebe lo contrario.
### - Es esencial para manejar información incompleta.
``` bash
Ejemplo: Los pájaros vuelan (Regla por defecto) $\rightarrow$ Piolín es un pájaro $\rightarrow$ Piolín vuela (a menos que se sepa que Piolín es un pingüino).
```
