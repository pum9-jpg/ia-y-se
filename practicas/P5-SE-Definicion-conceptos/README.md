# Sistemas Expertos y Representación del Conocimiento

Este proyecto recopila y ejemplifica tres prácticas clave en la Ingeniería del Conocimiento, centradas en la creación y el funcionamiento de **Sistemas Expertos (SE)**:

1.  **SE basado en Reglas de Producción** (Diagnóstico Ciclístico).
2.  **SE basado en Marcos o *Frames*** (Diagnóstico Ciclístico, Alternativo).
3.  **SE con Motor de Inferencia y Capacidad de Explicación** (Diagnóstico Automotriz Avanzado).

---
## 1. Reglas de Producción (SI-ENTONCES) y Marcos (Frames)

Estos primeros dos ejercicios demuestran las dos estructuras de conocimiento más comunes para representar el conocimiento de un experto.

### ⚙️ Reglas de Producción (Reglas SI-ENTONCES)

Implementa un sistema donde el conocimiento se almacena como una lista de reglas **`SI` (antecedentes) - `ENTONCES` (consecuente)**.

-   **Base de Conocimiento:** Se separa en dos conjuntos: `base_conocimiento_reglas` (síntomas → problema) y `base_conocimiento_soluciones` (problema → acción).
-   **Inferencia:** Utiliza **Encadenamiento Hacia Adelante** para buscar diagnósticos cuya condición se cumpla completamente con los hechos del usuario.

### 🖼️ Marcos (*Frames*)

Implementa una estructura de conocimiento orientada a objetos, donde los conceptos del dominio son representados por **Marcos** que contienen **Slots** (atributos).

-   **Base de Conocimiento:** `base_conocimiento_frames` contiene objetos (ej. `"ponchadura"`) con slots detallados (ej. `"sintomas"`, `"solucion"`, `"herramientas_necesarias"`).
-   **Inferencia:** La función de búsqueda compara los síntomas del usuario con el slot `"sintomas"` de cada *Frame* para identificar el objeto que describe el problema.

---
## 2. Motor de Inferencia y Capacidad de Explicación (Clase `SistemaExperto`)

Este ejercicio lleva la implementación a un nivel más avanzado, encapsulando la lógica en una clase `SistemaExperto` y centrándose en el diagnóstico de fallas automotrices.

### 🚗 Estructura Central: Clase `SistemaExperto`

La clase está diseñada para ser un motor de propósito general, que separa claramente el conocimiento (reglas) del mecanismo de razonamiento:

-   **`__init__(self, reglas)`:** Inicializa el sistema con la base de reglas externa.
-   **`razonar(self, hechos_iniciales)`:** Implementa el algoritmo de **Encadenamiento Hacia Adelante** (*Forward Chaining*). Itera repetidamente sobre las reglas hasta que no se puedan deducir nuevos hechos.
-   **`obtener_diagnosticos_finales()`:** Filtra los hechos deducidos para aislar solo aquellos que comienzan con `"diagnostico_"`.

### ❓ Capacidad Distintiva: Explicación

Una característica clave de los Sistemas Expertos es su capacidad para **explicar su razonamiento**.

-   **`self.historial_inferencia`:** Durante el razonamiento, se rastrea qué regla generó cada nuevo hecho.
-   **`explicar_conclusion(self, conclusion)`:** Utiliza un enfoque **recursivo** (similar al Encadenamiento Hacia Atrás) para desandar el camino de la inferencia, mostrando la regla final que condujo al diagnóstico y, luego, explicando cómo se obtuvieron los antecedentes de esa regla (hasta llegar a los hechos iniciales del usuario).

### Ejemplo de Trazabilidad

| Paso | Hecho Deducido | Regla Aplicada | Tipo |
| :--- | :--- | :--- | :--- |
| **Inicial** | `coche_no_gira_llave` | N/A | Hecho Inicial |
| **Intermedio** | `problema_bateria_o_arranque` | `Regla 1` | Hecho Deducido |
| **Final** | `diagnostico_bateria_descargada` | `Regla 3` | Diagnóstico Final |

---
## Conclusión Final

Estos ejercicios demuestran que la epresentación del conocimiento es el pilar de un Sistema Experto. Mientras que las Reglas de Producción y los Marcos ofrecen diferentes formas de estructurar la información (lógica vs. orientada a objetos), el verdadero poder del SE reside en su Motor de Inferencia. 