# Resumen: Proceso Humano de Resolución de Problemas y Razonamiento en IA

## 1. Razonamiento Humano e Inteligencia Artificial
Para crear máquinas que “piensen”, debemos entender cómo razonan los humanos.  
Los **Sistemas Expertos (SE)** imitan este proceso mediante motores de inferencia.

---

## 2. Sentido Común
Conjunto de conocimientos prácticos y compartidos (ej. saber que los objetos caen).  
**Desafío en IA:** difícil de replicar.  
**Consecuencia:** los SE son “frágiles”, funcionan bien en su dominio pero fallan en situaciones cotidianas.

---

## 3. Método de Pareamiento (Matching)
Proceso clave del motor de inferencia:
1. **Hechos:** información conocida.  
2. **Reglas:** base de conocimiento.  
3. **Matching:** el sistema compara hechos con reglas.  
4. **Activación:** si coincide, se ejecuta la regla y se añade un nuevo hecho.

---

## 4. Razonamiento e Inferencia
- **Razonamiento:** proceso global de pensar y sacar conclusiones.  
- **Inferencia:** pasos lógicos dentro del razonamiento.  
El motor de inferencia de un SE realiza estas operaciones.

---

## 5. Deducción
Va de lo **general a lo específico**.  
Conclusiones **seguras** si las premisas son verdaderas.  
**Ejemplo:**  
Si llueve → la calle se moja.  
Está lloviendo → la calle está mojada.

---

## 6. Inducción
Va de lo **específico a lo general**.  
Conclusiones **probables** basadas en observaciones.  
**Ejemplo:**  
Varios cuervos son negros → todos los cuervos son negros.  
Base del **Aprendizaje Automático (Machine Learning)**.

---

## 7. Ejercicio en Python
- **Sistema Deductivo:** usa reglas fijas → conclusión específica.  
- **Sistema Inductivo:** aprende de ejemplos → genera una regla general.

---

**Conclusión:**  
El razonamiento humano combina deducción e inducción.  
La IA intenta replicar ambos mediante **Sistemas Expertos** y **Machine Learning**.
