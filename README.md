# Unidad 3 — Los Sistemas Expertos, Definición y Conceptos

## 3.1 Concepto de Sistema Experto
Un **Sistema Experto (SE)** utiliza conocimiento especializado y un motor de inferencia
para resolver problemas de forma similar a un experto humano.

### Componentes principales:
- **Base de Conocimiento:** Contiene hechos, reglas y heurísticas.
- **Motor de Inferencia:** Aplica las reglas para deducir conclusiones.
- **Interfaz de Usuario y Módulo de Explicación:** Permiten la interacción y justifican los resultados.

---

## 3.2 Conocimiento superficial y profundo
- **Superficial:** Basado en experiencia práctica y reglas simples.
- **Profundo:** Modela principios causales y permite razonamiento en situaciones nuevas o complejas.

---

## 3.3 Características distintivas
- Competencia de experto.  
- Separación entre conocimiento y control.  
- Manejo de incertidumbre.  
- Capacidad de explicación.  
- Especialización en un dominio concreto.

---

## 3.4 Tipos de Sistemas Expertos
- Diagnóstico  
- Interpretación  
- Predicción  
- Diseño y Configuración  
- Planificación  
- Monitoreo y Control  
- Instrucción y Depuración

---

## Ejercicio Práctico — Sistema Experto de Diagnóstico

**Objetivo:** Diagnosticar por qué un automóvil no enciende.

### Fases del proyecto:
1. **Definir la Base de Conocimiento:**  
   Contiene reglas superficiales (síntoma → causa).  
2. **Construir el Motor de Inferencia:**  
   Implementado con encadenamiento hacia adelante.  
3. **Agregar la Capacidad de Explicación:**  
   Justifica cómo se llegó a cada conclusión.

### Archivo incluido
- `sistema_experto_diagnostico.py`: Implementación completa del sistema experto.

---

## Conclusión
Este proyecto ejemplifica cómo los **Sistemas Expertos** combinan:
- Razonamiento automatizado  
- Representación estructurada del conocimiento  
- Capacidad de explicación  

Logrando un modelo funcional que simula la toma de decisiones de un experto humano en un dominio específico.
