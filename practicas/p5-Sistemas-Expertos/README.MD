# Unidad 3: Los Sistemas Expertos, Definición y Conceptos

## 🧠 Sistema Experto de Diagnóstico Automotriz

Este proyecto implementa un **sistema experto** en Python capaz de **diagnosticar fallas comunes en un coche** basándose en reglas y hechos proporcionados por el usuario.  

El sistema utiliza un **motor de inferencia hacia adelante (forward chaining)** para deducir conclusiones (diagnósticos) a partir de una **base de conocimiento** y hechos iniciales.

---

## 📚 Estructura del Código

El programa se divide en **tres partes principales**:

---

### 🔹 **Parte 1: Base de Conocimiento**

Contiene un conjunto de **reglas** que representan el conocimiento de un mecánico experto.  
Cada regla tiene la siguiente estructura:

```python
{
    "nombre": "Regla 1: Problema de batería o motor de arranque",
    "si": ["coche_no_gira_llave"],
    "entonces": "problema_bateria_o_arranque"
}
```

- `"si"` → Lista de **condiciones** o hechos que deben cumplirse.  
- `"entonces"` → **Conclusión** que se deduce si se cumplen todas las condiciones.  
- `"nombre"` → Descripción de la regla.

📘 **Ejemplo:**  
Si el coche **no gira la llave**, se deduce que puede haber un **problema de batería o de arranque**.

---

### 🔹 **Parte 2: Motor de Inferencia (`SistemaExperto`)**

Esta clase implementa la lógica del razonamiento automático.  
Su función es **deducir nuevos hechos** a partir de los hechos iniciales y las reglas.

#### Principales métodos:

- `__init__(self, reglas)`  
  Inicializa el sistema con una lista de reglas.

- `razonar(self, hechos_iniciales)`  
  Aplica el motor de inferencia hacia adelante:
  1. Comienza con los hechos iniciales.
  2. Busca reglas cuyas condiciones se cumplan.
  3. Añade las conclusiones nuevas a la lista de hechos.
  4. Repite hasta que no haya nuevas deducciones.

- `obtener_diagnosticos_finales(self)`  
  Retorna las conclusiones que representan **diagnósticos finales** (comienzan con `"diagnostico_"`).

- `explicar_conclusion(self, conclusion)`  
  Genera una **explicación encadenada** del razonamiento, mostrando cómo se llegó a cada conclusión.

---

### 🔹 **Parte 3: Ejecución del Sistema**

En esta sección se define un **caso de uso**:

```python
hechos_del_usuario_1 = [
    "coche_no_gira_llave",
    "luces_debiles_o_muertas"
]
```

Luego se crea una instancia del sistema experto y se ejecuta el razonamiento:

```python
se_coche = SistemaExperto(base_de_conocimiento_coche)
hechos_finales_1 = se_coche.razonar(hechos_del_usuario_1)
diagnosticos_1 = se_coche.obtener_diagnosticos_finales()
```

Finalmente, se muestra el **diagnóstico** y una **explicación** de cómo se obtuvo.

---

## ⚙️ Ejecución

### 🔸 Requisitos
- Python 3.8 o superior

### 🔸 Instrucciones
1. Guarda el código en un archivo llamado `sistema_experto_coche.py`
2. Ejecuta el programa en la terminal:

```bash
python sistema_experto_coche.py
```

---

## 🧾 Ejemplo de Salida

```plaintext
# - Caso de Uso 1 -
# Hechos iniciales: El coche no gira la llave y las luces están muertas.

--  INICIANDO DIAGNÓSTICO CASO 1 -
- Proceso de Razonamiento -
Hecho añadido: 'problema_bateria_o_arranque' (Gracias a la regla:
'Regla 1: Problema de bateria o motor de arranque')
Hecho añadido: 'diagnostico_bateria_descargada' (Gracias a la regla:
'Regla 3: Bateria descargada confirmada')
- Fin del Proceso de Razonamiento -

Hechos Finales Deducidos: {'coche_no_gira_llave', 'luces_debiles_o_muertas', 
'problema_bateria_o_arranque', 'diagnostico_bateria_descargada'}
Diagnóstico(s) Final(es): ['diagnostico_bateria_descargada']

- EXPLICACIÓN DEL DIAGNÓSTICO -

Se llegó a la conclusión 'diagnostico_bateria_descargada' por la 'Regla 3: Bateria descargada confirmada'.
Esta regla establece que SI se cumplen las siguientes condiciones: ['problema_bateria_o_arranque', 'luces_debiles_o_muertas'], 
ENTONCES se deduce 'diagnostico_bateria_descargada'.
```

---

## 🧩 Explicación del Funcionamiento

1. **El usuario introduce hechos iniciales.**
   - Ejemplo: “el coche no gira la llave” y “las luces están muertas”.

2. **El sistema busca reglas que coincidan con esos hechos.**
   - Aplica la regla 1 → deduce “problema_bateria_o_arranque”.
   - Luego aplica la regla 3 → deduce “diagnostico_bateria_descargada”.

3. **El motor sigue infiriendo hasta que no hay más conclusiones posibles.**

4. **El sistema muestra los hechos finales y el diagnóstico.**

5. **Se explica cómo se llegó a la conclusión final.**

---

## 🧠 Conceptos Clave

| Concepto | Descripción |
|-----------|-------------|
| **Hecho** | Información conocida o proporcionada por el usuario. |
| **Regla** | Conocimiento experto que relaciona condiciones con conclusiones. |
| **Motor de inferencia** | Lógica que aplica las reglas para deducir nuevos hechos. |
| **Diagnóstico** | Conclusión final que identifica el problema del coche. |

---

## 🚗 Posibles Extensiones

- Añadir más reglas para cubrir más tipos de fallas.  
- Permitir entrada interactiva del usuario.  
- Implementar una interfaz gráfica (por ejemplo, con Tkinter).  
- Guardar los diagnósticos en un archivo de registro.

---

## CONCLUSION

Con este proyecto se aprendió cómo un sistema experto puede llegar razonar sobre información y tomar decisiones similares a las de un humano. Al construir este mini sistema de diagnóstico de coches, se llego a comprender cómo se aplican reglas, se procesan hechos y se generan explicaciones claras para llegar a conclusiones confiables.