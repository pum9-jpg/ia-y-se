##  Instalación de Python

Para ejecutar correctamente el programa, es necesario tener **Python 3.10 o superior** instalado en tu sistema.
Existen tres métodos recomendados:

---

# 🚗 Sistema Experto de Diagnóstico Automotriz

## 🏁 Conclusión del Ejercicio

Este proyecto implementa un **mini sistema experto de diagnóstico automotriz** que ejemplifica los principios fundamentales de los Sistemas Expertos (SE).

### 1. Separación entre conocimiento y razonamiento
- La **Base de Conocimiento** está definida como una lista de reglas (`base_de_conocimiento_coche`), cada una con condiciones (`si`) y una conclusión (`entonces`).
- El **Motor de Inferencia** está implementado en la clase `SistemaExperto`, que procesa los hechos iniciales y aplica las reglas para deducir nuevas conclusiones.
- Esto refleja la **independencia entre el conocimiento del experto y la lógica de razonamiento**, un principio clave en los SE.

### 2. Manejo de conocimiento superficial
- El sistema no modela el funcionamiento interno del motor del coche, sino que utiliza **reglas simples basadas en síntomas observables**.  
- Este enfoque de **síntoma → causa** es lo que se denomina *conocimiento superficial*, típico en sistemas expertos iniciales.

### 3. Motor de Inferencia (encadenamiento hacia adelante)
- El método `razonar()` aplica **encadenamiento hacia adelante**: parte de los hechos iniciales (síntomas) y va activando reglas hasta que no se puedan deducir más conclusiones.  
- De esta forma, el sistema simula el razonamiento de un mecánico experto, infiriendo diagnósticos a partir de observaciones.

### 4. Capacidad de explicación
- El método `explicar_conclusion()` permite **trazar el razonamiento**: muestra qué regla se aplicó y qué condiciones se cumplieron para llegar a un diagnóstico.  
- Esta característica distintiva de los SE aumenta la **transparencia y confianza** en el sistema, ya que no solo da una respuesta, sino que explica cómo llegó a ella.

---

## 🚀 ¿Qué hace el sistema en la práctica?
1. Recibe **síntomas iniciales** del usuario (ejemplo: `coche_no_gira_llave`, `luces_debiles_o_muertas`).  
2. Aplica las reglas de la base de conocimiento para deducir posibles causas.  
3. Devuelve un **diagnóstico final** (ejemplo: `diagnostico_bateria_descargada`).  
4. Explica paso a paso **cómo se llegó a esa conclusión**, mostrando las reglas utilizadas.  

---