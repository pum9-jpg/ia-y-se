# 🧠 Sistema Experto para Diagnóstico de Fallas en un Coche

## 📋 Descripción General
Este programa implementa un **sistema experto** básico que simula el razonamiento de un mecánico para diagnosticar problemas en un coche.  
Utiliza una **base de conocimiento** con reglas tipo *"SI ... ENTONCES ..."* y un **motor de inferencia** que aplica razonamiento hacia adelante (*forward chaining*).

---

## ⚙️ Funcionamiento

### 1. Base de Conocimiento
La base de conocimiento contiene reglas que relacionan síntomas del coche con posibles causas o diagnósticos.  
Cada regla tiene tres partes:
- `nombre`: descripción breve de la regla.  
- `si`: lista de condiciones o hechos que deben cumplirse.  
- `entonces`: conclusión que se deduce si las condiciones son verdaderas.

**Ejemplo de regla:**
```python
{
    "nombre": "Regla 3: Bateria descargada confirmada",
    "si": ["problema_bateria_o_arranque", "luces_debiles_o_muertas"],
    "entonces": "diagnostico_bateria_descargada"
}
```

---

### 2. Motor de Inferencia
El motor de inferencia recorre todas las reglas y, cada vez que encuentra una cuyas condiciones se cumplen con los hechos actuales, **agrega la conclusión** a la lista de hechos.  
Esto se repite hasta que no haya nuevos hechos que añadir.

**Pseudocódigo del proceso:**
```
Mientras haya nuevos hechos:
    Para cada regla en la base:
        Si todas las condiciones de la regla están en los hechos:
            Agregar la conclusión a los hechos
```

El sistema también guarda un historial de qué regla generó cada conclusión, lo que permite **explicar el diagnóstico final**.

---

### 3. Ejecución del Caso de Uso
Se ingresa un conjunto de hechos iniciales, por ejemplo:
```python
hechos_del_usuario_1 = [
    "coche_no_gira_llave",
    "luces_debiles_o_muertas"
]
```
El motor de inferencia analiza los hechos y deduce nuevas conclusiones hasta llegar a un diagnóstico final.  

**Salida esperada:**
```
Diagnóstico(s) Final(es): ['diagnostico_bateria_descargada']
```

El sistema también puede explicar **cómo llegó** a esa conclusión, mostrando qué reglas se activaron durante el proceso.

---

## 💡 Conclusión
Este código demuestra de forma clara cómo un sistema experto puede razonar con base en hechos y reglas predefinidas.  
Permite entender la lógica detrás de los diagnósticos automatizados, sirviendo como un ejemplo práctico de inteligencia artificial simbólica.
