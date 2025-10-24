
## 📘 **README – Unidad 3: Sistema Experto de Diagnóstico Automotriz**

# 🧠 Unidad 3 – Los Sistemas Expertos: Definición y Conceptos

## ⚙️ Descripción
Este programa implementa un **Sistema Experto Automotriz** basado en un modelo de **encadenamiento hacia adelante**.  
Simula el razonamiento de un experto mecánico mediante un conjunto de reglas **SI...ENTONCES**, diagnosticando fallas comunes de un coche.

El sistema:
- Recibe **hechos iniciales** (síntomas observados).
- Usa un **motor de inferencia** para deducir nuevos hechos.
- Genera un **diagnóstico final**.
- Explica **cómo llegó** a esa conclusión.

---

## 🚀 Ejecución en VS Code
1. Guardar el código como `sistema_experto_coche.py`.
2. Abrir una terminal en VS Code y ejecutar:
   ```bash
   python sistema_experto_coche.py
   ```

3. El programa mostrará:

   * El proceso de razonamiento paso a paso.
   * Los hechos finales deducidos.
   * El diagnóstico más probable.
   * Una explicación detallada del razonamiento.

---

## 🧩 Funcionamiento

1. **Base de conocimiento:**
   Contiene 6 reglas con condiciones (causas) y conclusiones (efectos).
   Ejemplo:

   * *Si el coche no gira la llave → problema de batería o arranque.*
   * *Si huele a gasolina → posible problema de combustible.*

2. **Motor de inferencia:**
   Aplica las reglas que cumplan todas sus condiciones, agregando las conclusiones al conjunto de hechos conocidos.
   Repite el proceso hasta que no se puedan deducir más hechos.

3. **Capacidad de explicación:**
   Permite rastrear de forma recursiva cómo se llegó a un diagnóstico final, mostrando las reglas aplicadas y los hechos intermedios.

---

## 🧪 Ejemplo de salida

```bash
INICIANDO DIAGNÓSTICO CASO 1 -
- Proceso de Razonamiento -
Hecho añadido: 'problema_bateria_o_arranque' (Gracias a la regla: 'Regla 1: Problema de batería o motor de arranque')
Hecho añadido: 'diagnostico_bateria_descargada' (Gracias a la regla: 'Regla 3: Batería descargada confirmada')
- Fin del Proceso de Razonamiento -

Hechos Finales Deducidos: {'coche_no_gira_llave', 'luces_debiles_o_muertas', 'problema_bateria_o_arranque', 'diagnostico_bateria_descargada'}
Diagnóstico(s) Final(es): ['diagnostico_bateria_descargada']

- EXPLICACIÓN DEL DIAGNÓSTICO -
Se llegó a la conclusión 'diagnostico_bateria_descargada' por la 'Regla 3: Batería descargada confirmada'.
Esta regla establece que SI se cumplen las siguientes condiciones: ['problema_bateria_o_arranque', 'luces_debiles_o_muertas'], ENTONCES se deduce 'diagnostico_bateria_descargada'.
...
```


## 💡 Conclusión

El sistema experto reproduce el razonamiento humano de un mecánico mediante **reglas lógicas y explicaciones encadenadas**.
Esta práctica demuestra cómo la **Inteligencia Artificial simbólica** puede representar conocimiento, aplicar inferencias y justificar sus decisiones de forma transparente.


