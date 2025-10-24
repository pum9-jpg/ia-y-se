# Recomendador de Bebidas ☕

Este proyecto muestra dos formas diferentes de resolver un mismo problema en Python: **recomendar una bebida según las preferencias del usuario**.  
Los ejemplos forman parte del **Capítulo 1** del curso *Inteligencia Artificial y Sistemas Expertos*.


## 📂 Archivos

### 1. `enfoque_convencional.py`
Implementa la lógica de decisión **de forma directa**, con estructuras `if-elif-else`.  
La lógica y las condiciones están escritas dentro del código, por lo que **si cambia una regla, hay que modificar el programa**.

**Ejecutar:**
```bash
python enfoque_convencional.py
```



### 2. `enfoque_ia_reglas.py`
Usa un enfoque **basado en reglas**, separando el *conocimiento* (las reglas) de la *lógica de inferencia*.  
El motor de inferencia busca coincidencias entre las condiciones del usuario y la base de conocimiento.

**Ejecutar:**
```bash
python enfoque_ia_reglas.py
```

---

## 🧩 Conclusión

El **enfoque convencional** representa cómo se programa de forma tradicional: las decisiones están "cableadas" en el código. Es como si nosotros le hubieramos dicho que hacer paso a paso.
En cambio, el **enfoque de IA basado en reglas** imita cómo razona un experto: las reglas se pueden editar sin tocar la lógica del programa. Es decir le damos las condiciones y el **PROGRAMA** "razona" para encontrar el caso que coincide con su conocimiento que le definimos.

En resumen:  
- El **enfoque convencional** es más simple, pero menos flexible.  
- El **enfoque basado en reglas** es más adaptable y cercano a cómo funcionan los **Sistemas Expertos** en Inteligencia Artificial.

---

💡 *Este ejercicio muestra la diferencia entre programar con algoritmos fijos y programar con conocimiento que puede crecer o modificarse fácilmente.*
